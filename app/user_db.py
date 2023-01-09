import sqlite3
import os.path

def init_db():
    database = r"login.db"
    if (os.path.isfile(database) != True): 
        create_users_table()
        insert_user(1, "admin", "p@$$w0rd")    

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Exception as e:
        print(e)
    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_users_table():    
    database = r"login.db"
    sql_create_table = """ CREATE TABLE IF NOT EXISTS users (
                           id       int,
                           username text,
                           password text
                           ); """
    # create a database connection
    conn = create_connection(database)
    # create tables
    if conn is not None:
        create_table(conn, sql_create_table)
        conn.commit()
    else:
        print("Error! cannot create the database connection.")


def insert_user(id, username, password):
    database = r"login.db"
    conn = create_connection(database)
    if conn is not None:
        sqlite_insert_query = ("INSERT INTO users (id,username,password)\n" +
                               "VALUES(\""+str(id)+"\"," +
                               "\""+username+"\"," +
                               "\""+password+"\");")
        print(sqlite_insert_query)
        cursor = conn.cursor()
        count = cursor.execute(sqlite_insert_query)
        conn.commit()
        print("Record inserted successfully into table POSITION:", cursor.rowcount)
        cursor.close()
    else:
        print("oops.")
