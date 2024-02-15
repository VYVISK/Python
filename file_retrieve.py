import database as db

pw = "vyvi1234"

# Create a database connection
Database = db.ConnectToDatabase('localhost', 'root', pw)

# Create server connection
connection = Database.create_server_connection()

# Specify the database name
db_name = "mysql_python"

# Create database connection
connection_db = Database.create_db_connection(db_name)

# Create a cursor
cursor = connection_db.cursor()

# Execute the SELECT query
cursor.execute("SELECT filename, file_data FROM files WHERE id = %s", (1,))
result = cursor.fetchone()

if result:
    filename, file_data = result
    with open(r"C:\Users\sheeja\OneDrive\Desktop\hello.jpg", 'wb') as file:
        file.write(file_data)

# Close cursor and connections
cursor.close()
# Database.close_connection(connection_db)
# Database.close_connection(connection)
