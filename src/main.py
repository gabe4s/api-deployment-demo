import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    return jsonify({'input': request.args.get('input')})

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)