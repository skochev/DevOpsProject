import pymysql

def add_user(user_id, username):
    schema_name = "projectdb"
    # Establishing a connection to DB
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='user', passwd='password', db=schema_name)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    # Inserting data into table
    cursor.execute(f"INSERT into {schema_name}.users (name, id) VALUES ('{username}', {user_id})")

    cursor.close()
    conn.close()
