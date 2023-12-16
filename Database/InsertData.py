import datetime

import pymysql
schema_name = "projectdb"

# Establishing a connection to DB
conn = pymysql.connect(host='127.0.0.1', port=3306, user='user', passwd='password', db=schema_name)
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

user_name = 'John'
user_id = 2
date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Inserting data into table
cursor.execute(f"INSERT into projectdb.users (user_id, user_name, creation_date) VALUES ({user_id}, '{user_name}', "
               f"'{date}')")

cursor.close()
conn.close()
