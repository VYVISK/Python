from  database import ConnectToDatabase

#Put our MySQL Terminal password
pw = "vyvi1234"
# Database name
db = "mysql_python"

Database = ConnectToDatabase('localhost','root',pw)

connection = Database.create_server_connection()


Username_password_table = """
CREATE TABLE USER_PASSWORD(
username varchar(255) PRIMARY KEY,
password varchar(255)
);"""

connection = Database.create_db_connection(db)
Database.execute_query(connection,Username_password_table)

#insert data 

data_orders = """
INSERT INTO USER_PASSWORD VALUES
('sreekku','12345678'),
('vyvi','87654321');"""


Database.execute_query(connection,data_orders)
connection.close()