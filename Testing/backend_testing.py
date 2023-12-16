import requests
import pymysql

schema_name = "projectdb"
user_id = '5'

# Executing post request
postRequest = requests.post(f'http://127.0.0.1:5000/data/{user_id}', json={"user_name": "Mark"})
# Printing response from the request
print("JSON Payload from POST method:")
if postRequest.ok:
    print(f"{postRequest.json()} Code: 200")
else:
    print(f"{postRequest.json()} Code: 500")

# Submitting a GET request to make sure status code is 200 and data equals to the posted data.
getRequest = requests.get(f'http://127.0.0.1:5000/data/{user_id}')
# Printing response from the request
print("JSON Payload from GET method:")
if getRequest.ok:
    print(f"{getRequest.json()} Code: 200")
else:
    print(f"{getRequest.json()} Code: 500")

# Establishing a connection to DB
conn = pymysql.connect(host='127.0.0.1', port=3306, user='user', passwd='password', db=schema_name)
# Getting a cursor from Database
cursor = conn.cursor()

# Getting all data from table “users” and checking posted data was stored inside DB (users table).
cursor.execute(f"SELECT * FROM {schema_name}.users;")

# Iterating table and printing all users
print("List of all users in the database:")
for row in cursor:
    user_value = row[1]
    print(user_value)

cursor.close()
conn.close()
