from flask import Flask,request,jsonify
from data_processing import *
app = Flask(__name__)

@app.route('/post', methods=["POST"])
def testpost():
    input_json = request.get_json(force=True) 
    MovieName = input_json['Title']
    dictToReturn = PipelineModel(MovieName)
    return jsonify(dictToReturn)