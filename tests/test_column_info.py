import logging

import pytest

from connection import connect, close_session


@pytest.mark.order(10)
def test_column_info():
    conn = connect()
    cursor = conn.cursor()
    results = cursor.columns(table="game")
    print("column of game table")
    for index, row in enumerate(results):
        print("%s.%s" % (index+1, row))

@pytest.mark.order(12)
def test_foreign_key():
    conn = connect()
    cursor = conn.cursor()
    results = cursor.foreignKeys(table="athlete")
    print("foreign key of athlete table")
    for index, row in enumerate(results):
        print("%s.%s" % (index+1, row))


