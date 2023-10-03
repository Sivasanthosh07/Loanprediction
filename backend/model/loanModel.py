import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
def predict(inputs):
    API_KEY = os.getenv('API_KEY')
    token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
    API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
    mltoken = token_response.json()["access_token"]
    print(mltoken)
    header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}
    # NOTE: manually define and pass the array(s) of values to be scored in the next line
    payload_scoring = {"input_data": [{"fields": ["no_of_dependents", "education", "self_employed", "income_anum", "loan_ammount", "loan_term", "cibil_score", "bank_asset_value"], "values": [inputs]}]}
    response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/8c6d6928-bb3f-404b-ae28-77fb005d5c87/predictions?version=2021-05-01', json=payload_scoring,
    headers={'Authorization': 'Bearer ' + mltoken})    
    print("Scoring response")
    print(response_scoring.json())
    predictions=response_scoring.json()
    print(predictions["predictions"][0]["values"][0][0])
    return predictions["predictions"][0]["values"][0][0]

