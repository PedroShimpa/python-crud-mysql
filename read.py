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

sql = "SELECT id, name, email, created FROM users"
cursor.execute(sql)
results = cursor.fetchall()


cursor.close()
connection.close()

for result in results:
    print(result)
