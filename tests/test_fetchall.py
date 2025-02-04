import logging

import pytest

from connection import connect, close_session

@pytest.mark.order(6)
def test_fetchall():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('select * from game')
    result = cursor.fetchall()
    print("query: select * from game")
    print("size: %d" % len(result))
    assert result is not None
    assert len(result) > 0
