import pymysql
from flask import Flask
import os
import signal

schema_name = "projectdb"
app = Flask(__name__)

# Establishing a connection to DB
conn = pymysql.connect(host='127.0.0.1', port=3306, user='user', passwd='password', db=schema_name)
# Getting a cursor from Database
cursor = conn.cursor()
#testing

# accessed via <HOST>:<PORT>/get username
@app.route("/get_user_name/<int:user_id>")
def get_user(user_id):
    try:
        with conn.cursor() as cursor:
            # Executing sql query to get the user if there is one
            cursor.execute(f"SELECT * FROM {schema_name}.users WHERE user_id = {user_id};")
            row = cursor.fetchone()
            if row is None:
                raise ValueError("<H1 id='error'>" + 'no such user:' + user_id + "</H1>")

            user_name = row[1]
            return "<H1 id='user'>" + user_name + "</H1>"

    except ValueError as ve:
        print(f"Error: {ve}")
        return "<H1 id='error'>" + 'no such user: ' + f"{user_id}" + "</H1>"

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return "<H1 id='error'>" + 'no such user: ' + f"{user_id}" + "</H1>"


@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'

app.run(host='127.0.0.1', debug=True, port=5001)
cursor.close()
conn.close()
