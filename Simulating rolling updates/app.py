import time, requests

count = 0

while(count < 40):
    r = requests.get('http://0.0.0.0:8080/api/version')
    data=r.json()
    print(data['version'][0])
    time.sleep(1)
    count+=1
