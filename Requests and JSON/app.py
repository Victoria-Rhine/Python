import requests

resp = requests.get('https://jsonplaceholder.typicode.com/todos/')
if resp.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /tasks/ {}'.format(resp.status_code))
for todo_item in resp.json():
    print('{} {}'.format(todo_item['userId'], todo_item['id']))
