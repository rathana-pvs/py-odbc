import logging

import pytest

from connection import connect, close_session


@pytest.mark.order(7)
def test_fetchmany():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('select * from game')
    result = cursor.fetchmany(10)
    print("query: select * from game, size of fetchmany(10)")
    assert len(result) == 10
    for index, row in enumerate(result):
        print("index: {}, row: {}".format(index, row))
