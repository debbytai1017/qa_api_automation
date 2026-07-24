import pytest
from api.product_api import ProductAPI
from database.mysql_helper import MySQLHelper

@pytest.fixture
def product_api():
    return ProductAPI()

@pytest.fixture
def mysql():
    return MySQLHelper()