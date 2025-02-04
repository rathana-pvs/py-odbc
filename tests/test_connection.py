import logging

import pytest

from connection import connect

conn_str = "driver={CUBRID Driver};server=localhost;port=33000;uid=dba;pwd=;db_name=demodb;"


# def test_connect():
#     print("connected to database")
#     assert connect() is not None

