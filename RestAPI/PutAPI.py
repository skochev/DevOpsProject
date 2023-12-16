import requests

# Executing put request
res = requests.put('http://127.0.0.1:5000/data/121', json={"user_name": "Tony"})

# Printing response from the request
if res.ok:
    print(f"{res.json()} Code: 200")
else:
    print(f"{res.json()} Code: 500")
