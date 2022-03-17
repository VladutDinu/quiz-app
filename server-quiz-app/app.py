import ssl
from flask import Flask, request
from flask_cors import CORS
from pymongo import MongoClient
import pymongo

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
link =''
with open('link.txt', 'r') as file:
    link = file.read()

CLIENT = MongoClient(link, ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
DB = CLIENT.answerdb

@app.route('/api/register_answ', methods=['POST'])
def register_answ():
    if request.is_json:
        json_obj = request.get_json()
        DB.Answers.insert_one(json_obj)
    else:
        return "Request object is not JSON"
    return "OK"

@app.route('/api/get_q', methods=['GET'])
def get_q():
    data = DB.questions.find()
    q_a={"q":[], "a":[]}
    for x in data:
        q_a["q"].append(x['q'])
        q_a["a"].append(x["a"])

    return q_a

@app.route('/api/get_right_answ', methods=['GET'])
def get_right_answ():
    data = DB.rightanswers.find()
    q_a={"q":[], "a":[]}
    for x in data:
        q_a["q"].append(x['q'])
        q_a["a"].append(x["a"])

    return q_a

@app.route('/api/get_answ', methods=['GET'])
def get_answ():
    answers = DB.Answers.find()
    for a in answers:
        print(a)
    return "OK"

if __name__ == '__main__':
    app.run(port=8081, debug=True)