from flask import Flask, request, jsonify, make_response
app = Flask(__name__)

#Routes
@app.route("/", methods=['POST'])
def index():
    data = {
        "name" : "Ayodeji",
        "status" : "Learning Flask",
        "route" : "/"
    }
    res = make_response(jsonify(data))
    return res

#Users route
@app.route("/users", methods=['POST'])
def userRoute():
    users = [
        {
            "name" : "John",
            "email" : "john@example.com",
        },
        {
            "name" : "Doe",
            "email" : "doe@example.com",
        },
        {
            "name" : "Mary",
            "email" : "mary@example.com",
        },
        {
            "name" : "Jane",
            "email" : "jane@example.com"
        }
    ]

    #header type
    headers = {"Content-Type": "application/json"}

    #This is the response variabele
    return make_response(jsonify(users), 200, headers=headers)


if(__name__) == "__main__":
    app.run(debug=True)