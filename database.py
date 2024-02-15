import mysql.connector
from mysql.connector import Error

class ConnectToDatabase:
    def __init__(self, host_name, user_name, user_password):
        # Constructor to initialize the connection parameters
        self.host_name = host_name
        self.user_name = user_name
        self.password = user_password

    def create_server_connection(self):
        # Method to create a connection to the MySQL server
        try:
            connection = mysql.connector.connect(
                host=self.host_name,
                user=self.user_name,
                passwd=self.password
            )
            print("MySQL Database connection successful")
            return connection
        except Error as err:
            raise RuntimeError(f"Error connecting to MySQL server: {err}")

    def create_database(self, connection, query):
        # Method to create a database using the provided query
        try:
            with connection.cursor() as cursor:
                cursor.execute(query)
            print("Database created successfully")
        except Error as err:
            raise RuntimeError(f"Error creating database: {err}")

    def create_db_connection(self, db_name):
        # Method to create a connection to a specific MySQL database
        try:
            connection = mysql.connector.connect(
                host=self.host_name,
                user=self.user_name,
                passwd=self.password,
                database=db_name
            )
            print("MySQL database connection successful")
            return connection
        except Error as err:
            raise RuntimeError(f"Error connecting to MySQL database: {err}")

    def execute_query(self, connection, query, data=None):
        # Method to execute a query that modifies the database (e.g., INSERT, UPDATE, DELETE)
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, data)
            connection.commit()
            print("Query was successful")
        except Error as err:
            raise RuntimeError(f"Error executing query: {err}")

    def read_query(self, connection, query, data=None):
        # Method to execute a query that retrieves data from the database (e.g., SELECT)
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, data)
                result = cursor.fetchall()
                return result
        except Error as err:
            raise RuntimeError(f"Error executing query: {err}")

    def close(self, connection):
        connection.close()
