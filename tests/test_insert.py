from datetime import date
import random

import pyodbc
import pytest

from connection import connect, close_session

table_name = "test_table_python"



@pytest.mark.order(1)
def test_drop_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS " + table_name)
    print("DROP TABLE IF EXISTS " + table_name)
    conn.commit()
    cursor.close()
    conn.close()

@pytest.mark.order(2)
def test_create_table():
    conn = connect()
    cursor = conn.cursor()
    create_table_query = f'''
    CREATE TABLE {table_name} (
          game_id INT primary key,
          player1_id INT NOT NULL,
          player2_id INT NOT NULL,
          score INT NOT NULL,
          region_code CHAR(3),
          status CHAR(1),
          game_date DATE NOT NULL
        )
    '''
    cursor.execute(create_table_query)
    conn.commit()
    cursor.close()
    conn.close()
    print("create table " + table_name + " successfully")

@pytest.mark.order(3)
def test_insert():
    insert_value = (random.randint(2000, 2500), 20022, 14346, 30136, 'NGR', 'B', date(2004, 8, 20))
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(f'INSERT INTO {table_name} VALUES (?, ?, ?, ?, ?, ?, ?)', insert_value)
    print("insert value:", insert_value)
    conn.commit()
    cursor.close()
    conn.close()

@pytest.mark.order(4)
def test_insert_many():
    insert_value = [(random.randint(2000, 2500), 20022, 14346, 30136, 'NGR', 'B', date(2004, 8, 20)),
                     (random.randint(2100, 2500), 20020, 14346, 30136, 'NGR', 'B', date(2004, 8, 21))]
    conn = connect()
    cursor = conn.cursor()
    cursor.executemany(f'INSERT INTO {table_name} VALUES (?, ?, ?, ?, ?, ?, ?)', insert_value)
    print("insert values:", insert_value)
    conn.commit()
    cursor.close()
    conn.close()

@pytest.mark.order(5)
def test_rollback():
    print("Should be error and rollback")
    conn = connect()
    cursor = conn.cursor()
    insert_value = (random.randint(2000, 2500), 20022, 14346, 30136, 'NGR', 'B', date(2004, 8, 20))
    try:
        cursor.execute(f'INSERT INTO {table_name} VALUES (?, ?, ?, ?, ?, ?, ?)', insert_value)
        cursor.execute(f'INSERT INTO {table_name} VALUES (?, ?, ?, ?, ?, ?, ?)', insert_value)
        conn.commit()
        assert False
    except pyodbc.Error as e:
        print(e)
        conn.rollback()
        print("Error and rollback the transaction")
        assert True
    cursor.close()
    conn.close()

