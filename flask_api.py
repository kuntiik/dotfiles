import argparse

from flask import Flask, request, Response, stream_with_context
from flask_cors import CORS
from peft import AutoPeftModelForCausalLM
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, TextIteratorStreamer
from threading import Thread


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

@app.route("/get_sessions")
def get_sessions():
    return [
        {'id': 1, 'name': 'foo1'},
        {'id': 2, 'name': 'foo2'},
            ]

@app.route("/get_session_history", methods= ['POST'])
def get_session_history():
    data = request.get_json(force=True)

@app.route("/generate", methods = ['POST'])
def generate():
    pass

app.run(host="0.0.0.0", port = 7861)
