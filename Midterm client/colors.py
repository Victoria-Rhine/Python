import json
import requests

resp=requests.get('https://reqres.in/api/unknown')

json_data = resp.json()

for value in json_data:
    if(value == 'data'):
        print(value)

