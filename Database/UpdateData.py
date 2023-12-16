import pymysql

schema_name = "projectdb"

# Establishing a connection to DB
conn = pymysql.connect(host='127.0.0.1', port=3306, user='user', passwd='password', db=schema_name)
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

# Updating data inside the table
cursor.execute(f"UPDATE {schema_name}.users SET user_name = 'Steven' WHERE user_id = 1")

cursor.close()
conn.close()
