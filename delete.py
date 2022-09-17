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

sql = "DELETE FROM users WHERE id = %s"
data = (1,)

cursor.execute(sql, data)
connection.commit()

recordsaffected = cursor.rowcount

cursor.close()
connection.close()

print(recordsaffected, " registros excluidos")
