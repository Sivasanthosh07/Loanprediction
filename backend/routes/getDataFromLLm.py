from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import re
from helpers.extract_info import extract_info
from helpers.processDocs import process
from helpers.res import response
class llmData(Resource):
    
    
    def post(self):
        if 'files' not in request.files:
            return {"message": "No file uploaded"}
        files = request.files.getlist('files')
        for file in files:
   
            print(file.filename)
            
        text=process(uploaded_files=files)
        print(text)
        print("Process Started")
        income=extract_info(text,"what is salary of this month?")
        input=re.sub(",", '', income)
        ans=re.findall(r"\d+\.\d+", input)
        anual_income=int(float(ans[0]))
        anual_income*=12
        bank_asset=extract_info(text,"what is the Closing balance?")
        aadhar=extract_info(text,"what is the Aadhaar number which is of 12 digits,not the Enrollment no or VID?")
        pan=extract_info(text,"give me the PAN or e-Permenant number or value which is of 10 characters all are in capital letters from income tax department?")
        Name=extract_info(text,"give me the  full Name from aadhar or pan?")
        Addresss=extract_info(text,"give me the  Address?")
        accountNo=extract_info(text,"give the bank account no?")
        print("Process finished")
        return jsonify({
            "income": income,
            "bankbalance": bank_asset,
            "aadhar": aadhar,
            "pan": pan,
            "Name":Name,
            "address":Addresss,
            "accountNo":accountNo
        })
        
        
    