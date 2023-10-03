


import requests,json
from dotenv import load_dotenv
load_dotenv()
import os

def extract_info(text,question):
   url = "https://us-south.ml.cloud.ibm.com/ml/v1-beta/generation/text?version=2023-05-29"
   API_KEY = os.getenv("API_KEY")
   token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
       API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
   mltoken = token_response.json()["access_token"]
   payload = json.dumps({

    "model_id": "google/flan-ul2",
    "input": "Answer the following question using only information from the article. Article: ###"+text+".### \\n\\nQuestion:\\n"+ question+"",
    "parameters": {
        "decoding_method": "greedy",
        "max_new_tokens": 100,
        "min_new_tokens": 0,
        "stop_sequences": [],
        "repetition_penalty": 2
    },
    "project_id": "b8fd838c-df56-4a3b-beaf-d68ff9965a48"
    })
   headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer '+mltoken
   }
   response = requests.request("POST", url, headers=headers, data=payload)
   print(response)
   summary=response.json()
    
   print(summary)
   summary = summary["results"][0]["generated_text"]
   return summary