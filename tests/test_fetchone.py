import logging

import pytest

from connection import connect, close_session

@pytest.mark.order(8)
def test_fetchone():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('select * from game')
    result = cursor.fetchone()
    print("select * from game")
    print("result: %s", result)
    cursor.close()
    assert result is not None
