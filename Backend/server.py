from flask import Flask,request,jsonify
import pymongo
import os
app = Flask(__name__)

DOMAIN = 'localhost'
PORT = 27017

client = pymongo.MongoClient('mongodb://db:27017/')

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
    app.run(host='0.0.0.0',port=3000)