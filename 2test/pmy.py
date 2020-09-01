import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user="fail",
        password="2ban",
        database="fail2ban"
)
print(mydb)
