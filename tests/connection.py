import pyodbc
import logging



conn_str = "driver={CUBRID Driver};server=localhost;port=33000;uid=dba;pwd=;db_name=demodb;"

def connect():
    # logging.basicConfig(level=logging.INFO)
    conn = None
    try:
        conn = pyodbc.connect(conn_str)
        return conn
    except pyodbc.Error as e:
        print("Error:", e)
        # logging.error("Error connecting to database", e)

def close_session(conn, cursor):

    if cursor is not None:
        cursor.close()

    if conn is not None:
        conn.close()