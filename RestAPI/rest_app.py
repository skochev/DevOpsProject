from flask import Flask, request
import pymysql
import datetime
import os
import signal

schema_name = "projectdb"
app = Flask(__name__)

# Establishing a connection to DB
conn = pymysql.connect(host='127.0.0.1', port=3306, user='user', passwd='password', db=schema_name)
# Getting a cursor from Database
cursor = conn.cursor()
conn.autocommit(True)

# Supported methods
@app.route('/data/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'GET':
        # Executing sql query to get the user if there is one
        cursor.execute(f"SELECT * FROM {schema_name}.users WHERE user_id = {user_id};")
        row = cursor.fetchone()

        # Checking if user_id exists
        if not row:
            return {'status': 'error', 'reason': 'no such id'}, 500  # status code
        else:
            return {'status': 'ok', 'user_name': row[1]}, 200  # status code

    elif request.method == 'POST':
        # Getting the json data payload from request
        request_data = request.json

        # Executing sql query to get the user if there is one
        cursor.execute(f"SELECT * FROM {schema_name}.users WHERE user_id = {user_id};")
        row = cursor.fetchone()

        # Checking if user_id already exists
        if not row:
            # Treating request_data as a dictionary to get a specific value from key
            user_name = request_data.get('user_name')
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Executing sql query to insert new user
            cursor.execute(f"INSERT into {schema_name}.users (user_id, user_name, creation_date) VALUES ({user_id}, '{user_name}', '{date}')")

            return {'status': 'ok', 'user added': user_name}, 200  # status code
        else:
            return {'status': 'error', 'reason': 'id already exists'}, 500  # status code

    elif request.method == 'PUT':
        # Getting the json data payload from request
        request_data = request.json

        # Executing sql query to get the user if there is one
        cursor.execute(f"SELECT * FROM {schema_name}.users WHERE user_id = {user_id};")
        row = cursor.fetchone()

        # check if user_id already exists
        if not row:
            return {'status': 'error', 'reason': 'no such id'}, 500  # status code
        else:
            # Treating request_data as a dictionary to get a specific value from key
            user_name = request_data.get('user_name')

            # Executing sql query to insert new user
            cursor.execute(f"UPDATE {schema_name}.users SET user_name = '{user_name}' WHERE user_id = {user_id}")

            return {'status': 'ok', 'user_updated': user_name}, 200  # status code

    elif request.method == 'DELETE':
        # Executing sql query to get the user if there is one
        cursor.execute(f"SELECT * FROM {schema_name}.users WHERE user_id = {user_id};")
        row = cursor.fetchone()

        # Checking if user_id already exists
        if not row:
            return {'status': 'error', 'reason': 'no such id'}, 500  # status code
        else:
            # Executing sql query to delete the user
            cursor.execute(f"DELETE FROM {schema_name}.users WHERE user_id = {user_id}")

            return {'status': 'ok', 'user_deleted': user_id}, 200  # status code


@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'


app.run(host='127.0.0.1', debug=True, port=5000)
cursor.close()
conn.close()
