import pymysql

schema_name = "projectdb"

# Establishing a connection to DB
conn = pymysql.connect(host='127.0.0.1', port=3306, user='user', passwd='password', db=schema_name)
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

# Creating table
statementToExecute = "CREATE TABLE `" + schema_name + ("`.`users`(`user_id` INT NOT NULL,`user_name` VARCHAR(50) NOT "
                                                       "NULL, PRIMARY KEY (`user_id`), `creation_date` VARCHAR(50));")
cursor.execute(statementToExecute)

cursor.close()
conn.close()
