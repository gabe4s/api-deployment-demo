from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/test', methods = ['GET'])
def index():
    return "updated 4"

@app.route('/', methods = ['GET'])
def index():
    return jsonify({'input': request.args.get('input')})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)