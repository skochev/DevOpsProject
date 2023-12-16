import pymysql

schema_name = "projectdb"

# Establishing a connection to DB
conn = pymysql.connect(host='127.0.0.1', port=3306, user='user', passwd='password', db=schema_name)
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

# Deleting data from table
cursor.execute(f"DELETE FROM {schema_name}.users WHERE user_id = 6")

cursor.close()
conn.close()
