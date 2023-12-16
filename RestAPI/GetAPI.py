import requests

# Executing get request
res = requests.get('http://127.0.0.1:5000/data/1')

# Printing response from the request
if res.ok:
    print(f"{res.json()} Code: 200")
else:
    print(f"{res.json()} Code: 500")
