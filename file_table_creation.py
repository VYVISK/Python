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

Database.close(connection)