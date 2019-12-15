from flask import Flask, jsonify,  abort

app = Flask(__name__)


votes = [
	{
		'post_id': 0,
		'vote_count': -1,
	},
	{
		'post_id': 1,
		'vote_count': 5,
	},
	{
		'post_id': 2,
		'vote_count': 42,
	},
]

@app.route('/api/votes', methods=["GET"])
def posts():
    return jsonify ({'blog': votes})

@app.route('/api/votes/<int:post_id>', methods=["GET"])
def post(post_id):
    if post_id < 0 or post_id > len(votes):
        abort(404)
    return jsonify (votes[post_id])
