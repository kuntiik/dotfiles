import argparse

from flask import Flask, request, Response, stream_with_context
from flask_cors import CORS
from peft import AutoPeftModelForCausalLM
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, TextIteratorStreamer
from threading import Thread
from dotenv import dotenv_values
import openai
import re
import sqlite3
import json
from handlers import check_prompt_safety, check_response_safety, DBHandler
from handlers import data_to_history


openai.api_key = dotenv_values()['OPENAI_API_KEY']



parser = argparse.ArgumentParser()
parser.add_argument("--model_path_or_id", 
                    type=str, 
                    default = "NousResearch/Llama-2-7b-hf", 
                    required = False,
                    help = "Model ID or path to saved model")

parser.add_argument("--lora_path", 
                    type=str, 
                    default = None, 
                    required = False,
                    help = "Path to the saved lora adapter")

args = parser.parse_args()

if args.lora_path:
    # load base LLM model with PEFT Adapter
    model = AutoPeftModelForCausalLM.from_pretrained(
        args.lora_path,
        low_cpu_mem_usage=True,
        torch_dtype=torch.float16,
        load_in_4bit=True,
    )
    tokenizer = AutoTokenizer.from_pretrained(args.lora_path)
else:
    model = AutoModelForCausalLM.from_pretrained(
        args.model_path_or_id,
        low_cpu_mem_usage=True,
        torch_dtype=torch.float16,
        load_in_4bit=True
    )
    tokenizer = AutoTokenizer.from_pretrained(args.model_path_or_id)

app = Flask(__name__)
CORS(app)
# db = DBHandler()

@app.route("/get_session_history", methods= ['POST'])
def get_session_history():
    data = request.get_json(force=True)
    history = {1: [
        {'user': 'user', 'content': "User message"},
        {'user': 'bot', 'content': "A response from the bot"}
        ]}
    return {history: history.get(data['id'], [])}

@app.route("/get_sessions")
def get_sessions():
    db = DBHandler()
    return {"sessions": [{'id': id, 'name': name} for id, name in zip(*db.names_and_ids)]}

INPUT_SAFETY = False

@app.route("/generate", methods = ['POST'])
def generate():
    data = request.get_json(force=True)
    db = DBHandler()
    print(f"Database ids: {db.ids}")
    if db.contains_id(data['id']):
        conversation = db.fetch_id(data['id'])
        history = data_to_history(conversation['data'])
    else:
        history = ""
    
    print(f"Current history is {history}")

    prompt = f"""### Instruction:
    Use the following Input and come up with a structured response in the style of Ned Flanders given the context. Be concise!
    ### Context:
    {history}

    ### Input:
    {data['prompt']}

    ### Response:
    """
    if INPUT_SAFETY and check_prompt_safety(data['prompt']):
        return {"generated_text": "Your input is harmful, offensive or dangerous. This incident will be recorded!"}
    
    # Tokenize the input
    input_ids = tokenizer(
        prompt,
        return_tensors="pt", 
        truncation=True).input_ids.cuda()
    
    generation_kwargs = dict(
        input_ids = input_ids,
        max_new_tokens=data['parameters'].get('max_new_tokens', 100), 
        do_sample=data['parameters'].get('do_sample', True),
        top_p=data['parameters'].get('top_p', 0.9),
        temperature=data['parameters'].get('temperature', 0.7),
        use_cache=True
    )

    outputs = model.generate(**generation_kwargs)
    
    # return {"generated_text" : tokenizer.batch_decode(outputs, skip_special_tokens=True)[0][len(data['prompt']):]}
    output_text = tokenizer.batch_decode(outputs.detach().cpu().numpy(), skip_special_tokens=True)[0][len(prompt):]
    db.update_by_id(data['id'], {'chatPrompt': data['prompt'], 'botMessage': output_text})
    print("database ids: ", db.ids)
    # history += f"QESTION={data['prompt']}\nANSWER={output_text}"
    return {"generated_text" : output_text}

app.run(host="0.0.0.0", port = 7861)
