import mysql.connector

import json

config = open('./database/config.json')
config = json.load(config)
connection = mysql.connector.connect(
    host=config['host'],
    user=config['user'],
    password=config['password'],
    database=config['database']
)
cursor = connection.cursor()

sql = "UPDATE users SET name = %s, email = %s WHERE id = %s"
data = ('PEDRO2', 'PEDRO2@TESTE.COM', 1)

cursor.execute(sql, data)
connection.commit()

recordsaffected = cursor.rowcount

cursor.close()
connection.close()

print(recordsaffected, " registros alterados")
