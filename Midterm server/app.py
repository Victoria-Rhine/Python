from flask import Flask, request, url_for

app = Flask(__name__)

@app.route('/api/intdata/<int:id>', methods=["GET"])
def activity(id):
    if(id % 2 == 0):
        response = { "Even":"true", "Inverted":id*-1}
        return response
    if(id % 2 != 0):
        response = { "Even":"false", "Inverted":id*-1 }
        return response
