import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    return jsonify({'input': request.args.get('input')})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)