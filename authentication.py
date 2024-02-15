from database import ConnectToDatabase

def import_user_password_table():  
    pw = "vyvi1234"
    # Database name
    db = "mysql_python"

    Database = ConnectToDatabase('localhost','root',pw,)

    q1 = """SELECT * FROM USER_PASSWORD;"""

    connection = Database.create_db_connection(db)

    return Database.read_query(connection,q1)


def check_username_password(user,passwd):
    results = import_user_password_table()
    for value in results:
        print(value[0],value[1])
        if(user == value[0] and passwd == value[1]):
            return True
    return False

# check_username_password('ivin','124523432')
