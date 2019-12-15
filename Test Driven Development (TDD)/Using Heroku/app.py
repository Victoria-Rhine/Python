from flask import Flask, jsonify, abort, request, url_for
from datetime import datetime

app = Flask(__name__)

activity_log = [
    {
        'id': 0,
        'user_id': 1,
        'username': 'Arya Stark',
        'timestamp': datetime.utcnow(),
         'details': "Defender of Winterfell",
    },
    {
        'id': 1,
        'user_id': 2,
        'username': 'Sansa Stark',
        'timestamp': datetime.utcnow(),
        'details': "Queen in the North",
    },
    {
        'id': 2,
        'user_id': 3,
        'username': 'Daenerys Tarygaryen',
        'timestamp': datetime.utcnow(),
        'details': "The Mad Queen",
    },    
]

# return a single activity entry corresponding to the specified id
@app.route('/api/activities/<int:id>', methods=["GET"])
def activity(id):
    if id < 0 or id >= len(activity_log):
        abort(404)
    return jsonify(activity_log[id])

 # returns the most recent "n" activity entries, where "n" is a service-defined variable
@app.route('/api/activities', methods=['GET'])
def activities():
    return jsonify({'activities': activity_log})

# add a simple hello world endpoint
@app.route('/')
def hello_world():
    return 'Hello, World!'
