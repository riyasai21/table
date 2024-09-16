import mysql.connector

connection = mysql.connector.connect(
    host='local host',
    darabase='udp',
    user='root',
    password='admin'
    )
if connection.is_connected():
    print("successfully connected to the database")