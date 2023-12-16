import requests

# Executing delete request
res = requests.delete('http://127.0.0.1:5000/data/6')

# Printing response from the request
if res.ok:
    print(f"{res.json()} Code: 200")
else:
    print(f"{res.json()} Code: 500")
