import json
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

sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
data = ('PEDRO', 'PEDRO@TESTE.COM')

cursor.execute(sql, data)
connection.commit()

userId = cursor.lastrowid

cursor.close()
connection.close()

print("Um novo usuario foi cadastrado com o ID:", userId)
