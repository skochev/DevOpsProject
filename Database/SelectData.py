import pymysql

schema_name = "projectdb"

# Establishing a connection to DB
conn = pymysql.connect(host='127.0.0.1', port=3306, user='user', passwd='password', db=schema_name)

# Getting a cursor from Database
cursor = conn.cursor()

# Getting all data from table “users”
cursor.execute(f"SELECT * FROM {schema_name}.users;")

# Iterating table and printing all users
for row in cursor:
    user_value = row[1]
    print(user_value)

cursor.close()
conn.close()
