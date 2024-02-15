import mysql.connector
 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="vyvi1234" 
)
 
print(mydb) # <mysql.connector.connection_cext.CMySQLConnection object>