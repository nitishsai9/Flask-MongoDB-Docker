from flask import Flask,request,jsonify
from pymongo import MongoClient
import os
app = Flask(__name__)

DOMAIN = 'localhost'
PORT = 27017

client = MongoClient('mongodb://localhost:27017/')

db=client['mydatabase']
todos = db["tods"]


@app.route("/",methods=['POST'])
def home():
    if request.method == 'POST':
        title=request.form.get('title')
        desc= request.form.get('desc')
        todos.insert_one({'title': title, 'body':desc})
        return jsonify(message="success")

    
if __name__ == "__main__":
    app.run(port=3000)