# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from routes import loanStatus
from routes import getDataFromLLm
# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)


api.add_resource(loanStatus.getLoanStatus, '/getLoanstatus')
api.add_resource(getDataFromLLm.llmData, '/getData')



# driver function
if __name__ == '__main__':

	app.run(debug = True)
