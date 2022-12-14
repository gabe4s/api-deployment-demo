from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def index():
    return jsonify({'input': request.args.get('input')})

@app.route('/hello', methods = ['GET'])
def hello():
    return "Hello DevOps Team"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)