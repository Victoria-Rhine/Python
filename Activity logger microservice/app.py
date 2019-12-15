from flask import Flask, jsonify, abort, request, url_for
from datetime import datetime
from mongoengine import connect, StringField, IntField, Document, DateTimeField, queryset_manager
import json, os, urllib, pymongo, time
from bson.objectid import ObjectId

app = Flask(__name__)

mongo_uri = os.getenv('DB_HOST')
sleep_time = os.getenv('SLEEP_TIME', default=0)

connect(host=mongo_uri, port=27017)

class ActivityLog(Document):
    user_id = IntField(required=True)
    username = StringField(required=True, max_length=64)
    timestamp = DateTimeField(default=datetime.utcnow)
    details = StringField(required=True)

    @queryset_manager
    def objects(self, queryset):
        return queryset.order_by('-timestamp')


# return all activities
@app.route('/api/activities/', methods=["GET"])
def activities():
    logs = ActivityLog.objects[:10]
    json_logs = json.loads(logs.to_json())
    return jsonify({'activities': json_logs})

# return a single activity
@app.route('/api/activities/<string:str_id>', methods=["GET"])
def activity(str_id):
    if ObjectId.is_valid(str_id):
        log_id = ActivityLog.objects(id=str_id).first()
        if log_id is None:
            abort(404)
        log_id_json = json.loads(log_id.to_json())
    return jsonify(log_id_json)

# create a new activity entry
@app.route('/api/activities/', methods=["POST"])
def create_activity():
    if not request.json:
        abort(400)
    new_activity = request.get_json()
    if ('user_id' not in new_activity or 'username' not in new_activity or 'details' not in new_activity):
        abort(400)
    new_log = ActivityLog(
            user_id=new_activity['user_id'],
            username=new_activity['username'],
            timestamp=new_activity['timestamp'],
            details=new_activity['details']
    ).save()
    time.sleep(int(sleep_time))
    new_log_json = json.loads(new_log.to_json())
    return jsonify(new_log_json), 201
