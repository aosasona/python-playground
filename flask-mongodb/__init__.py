from flask import Flask, request, make_response, jsonify
from flask_mongoengine import MongoEngine

app = Flask(__name__)

@app.route('/', methods=["POST"])
def index():
    #Send a response
    responseBody = [
        {
            "name": "John Doe",
            "email" : "john@example.com",
        },
        {
            "name" : "Mary Jane",
            "email" : "mary@example.com",
        }
    ]
    res = make_response(jsonify(responseBody))

    return res

# GET and OUTPUT JSON request
@app.route('/json', methods=["POST"])
def jsonResponse():
    res =  jsonify(request.get_json())
    return res

# Check if a request body is json
@app.route('/test-json', methods=["POST"])
def isJson():
    resJson = request.is_json
    return f"{resJson}"

if __name__ == "__main__":
    app.run(debug=True)