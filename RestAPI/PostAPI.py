import requests

# Executing post request
res = requests.post('http://127.0.0.1:5000/data/6', json={"user_name": "Mark"})

# Printing response from the request
if res.ok:
    print(f"{res.json()} Code: 200")
else:
    print(f"{res.json()} Code: 500")
