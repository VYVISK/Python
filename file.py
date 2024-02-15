import database as db

pw = "vyvi1234"

Database = db.ConnectToDatabase('localhost', 'root', pw)

connection = Database.create_server_connection()

query_create_table = """CREATE TABLE IF NOT EXISTS files (
    id INT PRIMARY KEY AUTO_INCREMENT,
    filename VARCHAR(255) NOT NULL,
    file_data LONGBLOB
);"""

db_name = "mysql_python"

connection = Database.create_db_connection(db_name)

Database.execute_query(connection, query_create_table)

with open(r"C:\Users\sheeja\Downloads\catpicturess(4).jpg", 'rb') as file:
    file_data = file.read()

insert_query = """INSERT INTO files (filename, file_data) VALUES (%s, %s)"""
data = ('catpic.jpg', file_data)

Database.execute_query(connection, insert_query, data)
