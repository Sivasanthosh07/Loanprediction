from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from model import loanModel
class getLoanStatus(Resource):
    
    
    def post(self):
        data=request.get_json()
        dependents=data["dependents"]
        eduction=data["education"]
        employment=data["employment"]
        anual_income=int(data["income"])*12
        loan_ammount=data["loan_ammount"]
        loan_term=data["loan_term"]
        cibil=data["cibil"]
        bank_balance=data["bankbalance"]
        features=[dependents,eduction,employment,anual_income,loan_ammount,loan_term,cibil,bank_balance]
        prediction = loanModel.predict(features)
        print(prediction)
        if prediction == 0:
            return jsonify({"status":"Your loan is approved"})
        else:
            return jsonify({"status":"Loan rejected"})
