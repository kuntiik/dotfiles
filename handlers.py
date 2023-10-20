from dotenv import dotenv_values
import openai
import re
import sqlite3
import json

def check_prompt_safety(prompt):
    openai.api_key = dotenv_values()['OPENAI_API_KEY']
    pattern = r'\b(?i)(yes\.|yes)\b'
    prompt_check = "QESTION={\n" + prompt + "/n}/nIs the QUESTION offensive, harmful or dangerous? Answer YES or NO only!"
    try:
        chat = openai.ChatCompletion.create( 
            model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt_check}]
        ) 
        response = chat['choices'][0]['message']['content']
        if len(re.findall(pattern, response)) > 0:
            return True
        return False
    except Exception as e:
        return False

def sumarize_history(history, length=250):
    openai.api_key = dotenv_values()['OPENAI_API_KEY']
    prompt_summarize = "SENTENCES={\n" + history + "/n}/nSumarize the text in SENTENCES to make it shorter than " + str(length) + " words"

    try:
        chat = openai.ChatCompletion.create( 
            model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt_summarize}]
        ) 
        return chat['choices'][0]['message']['content']
    except Exception as e:
        return ""

def check_response_safety(response):
    openai.api_key = dotenv_values()['OPENAI_API_KEY']
    pattern = r'\b(?i)(yes\.|yes)\b'
    prompt_check = "RESPONSE={\n" + response + "/n}/nIs the RESPONSE offensive, harmful, dangerous or does it contain bias? Answer YES or NO only!"
    try:
        chat = openai.ChatCompletion.create( 
            model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt_check}]
        ) 
        response = chat['choices'][0]['message']['content']
        if len(re.findall(pattern, response)) > 0:
            return True
        return False
    except Exception as e:
        return False

def data_to_history(data):
    history = ""
    for inp_resp in data:
        history += f"QESTION={inp_resp['chatPrompt']}\nANSWER={inp_resp['botMessage']}\n"
    return history



class DBHandler:
    def __init__(self) -> None:
        self.conn = sqlite3.connect('my_test_database.db')
        self.cursor = self.conn.cursor()
        self.table = "history"
        self.cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {self.table} (
                id STRING PRIMARY KEY,
                data TEXT
            )''')
    
    @property
    def ids(self):
        self.cursor.execute(f'SELECT id FROM {self.table}')
        return [row[0] for row in self.cursor.fetchall()]

    @property
    def names_and_ids(self):
        self.cursor.execute(f'SELECT id FROM {self.table}')
        ids = [row[0] for row in self.cursor.fetchall()]
        self.cursor.execute(f'SELECT data FROM {self.table}')
        all_data = [row[0] for row in self.cursor.fetchall()]
        names = [json.loads(data)['data'][0].get('chatPrompt', 'No name') for data in all_data]
        return names, ids
    
    def contains_id(self, id):
        return id in self.ids
    
    def fetch_id(self, id):
        self.cursor.execute(f'SELECT data FROM {self.table} WHERE id = ?', (id,))
        data_str = self.cursor.fetchone()
        if data_str:
            return json.loads(data_str[0])
        else:
            return 
    
    def update_by_id(self, id, conversation):
        data = self.fetch_id(id)
        if data:
            data['data'].append(conversation)
            updated_data_str = json.dumps(data)
            self.cursor.execute(f'UPDATE {self.table} SET data = ? WHERE id = ?', (updated_data_str, id))
        else:
            updated_data_str = json.dumps({'data' : [conversation]})
            self.cursor.execute(f'INSERT INTO {self.table} (id, data) VALUES (?, ?)', (id, updated_data_str))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
