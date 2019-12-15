from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Data to serve with our API
POSTS = {
    "0": {
        "user_id": 1,
        "username": "Phineas the Cat",
        "timestamp": get_timestamp(),
        "details": "New post - hello, world",
        "location": "location of single activity"
    },
    "1": {
        "user_id": 2,
        "username": "Sam the Cat",
        "timestamp": get_timestamp(),
        "details": "upvoted a post",
        "location": "location of single activity"
    },
    "2": {
        "user_id": 3,
        "username": "Sawyer the Cat",
        "timestamp": get_timestamp(),
        "details": "downvoted a post",
        "location": "location of single activity"
    }
}

# Create a handler for our read (GET) posts
def read():
    """
    This function responds to a request for /api/posts
    with the complete lists of posts

    :return:        sorted list of posts
    """
    # Create the list of people from our data
    return [POSTS[key] for key in sorted(POSTS.keys())]
