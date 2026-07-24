from testdata.product_data import (
    create_product_data, update_product_data
)
import allure
from utils.allure_helper import (
    attach_request,
    attach_response,
    attach_sql
)

@allure.feature("Product API")
@allure.story("Get Products")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("Verify get all products successfully.")
def test_get_products(product_api):
    # 呼叫API
    response = product_api.get_products()
    attach_response(response)
    # 驗證API
    assert response.status_code == 200
    jsonData = response.json()
    assert isinstance(jsonData, list)
    assert len(jsonData) > 0
    first_product = jsonData[0]
    assert "id" in first_product
    assert "name" in first_product
    assert "price" in first_product
    assert "stock" in first_product

@allure.feature("Product API")
@allure.story("Create Product")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Verify create product successfully.")
def test_create_product(product_api, mysql):
    product = create_product_data()
    attach_request(product)
    # 呼叫API
    response = product_api.create_product(product)
    attach_response(response)
    # 驗證API
    assert response.status_code == 201
    jsonData = response.json()
    assert jsonData["name"] == product["name"]
    # 驗證DB
    sql ="""
    SELECT * FROM products
    WHERE name = %s 
    """
    attach_sql(sql)
    result = mysql.query_one(sql,(product["name"],))
    assert result is not None
    assert result["name"] == product["name"]
    assert result["price"] == product["price"]

@allure.feature("Product API")
@allure.story("Get Product")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("Verify get product successfully.")    
def test_get_product(product_api, mysql):
    
    # 建立商品
    product = create_product_data()
    create_response = product_api.create_product(product)

    # 驗證建立成功
    assert create_response.status_code == 201
    
    # 取得建立後的商品資訊
    Create_jsonData = create_response.json()
    
    # 取得商品id
    product_id = Create_jsonData["id"]

    # 呼叫 GET API
    response = product_api.get_product(product_id)

    attach_response(response)

    # 驗證 GEI API
    assert response.status_code == 200
    jsonData = response.json()
    assert jsonData["id"] == product_id
    assert jsonData["name"] == product["name"]

    # 驗證 DB
    sql ="""
    SELECT * FROM products
    WHERE id = %s
    """
    attach_sql(sql)

    result = mysql.query_one(sql, (product_id,))
    assert result is not None
    assert result["name"] == product["name"]
    assert result["price"] == product["price"]

@allure.feature("Product API")
@allure.story("Update Product")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Verify update product successfully.")
def test_update_product(product_api, mysql):

    # 建立商品
    product = create_product_data()

    create_response = product_api.create_product(product)
    assert create_response.status_code == 201
    product_id = create_response.json()["id"]

    # 更新資料
    update_data = update_product_data()
    attach_request(update_data)
    update_response = product_api.update_product(
        product_id, 
        update_data
        )
    attach_response(update_response)
    assert update_response.status_code == 200
    
    # 再查一次API
    get_response = product_api.get_product(product_id)
    assert get_response.status_code == 200
    jsonData = get_response.json()
    assert jsonData["name"] == update_data["name"]
    assert jsonData["price"] == update_data["price"]

    # 驗證DB
    sql = """
    SELECT * FROM products
    WHERE id = %s
    """
    attach_sql(sql)
    result = mysql.query_one(sql, (product_id,))
    assert result is not None
    assert result["name"] == update_data["name"]
    assert result["price"] == update_data["price"]

@allure.feature("Product API")
@allure.story("Delete Product")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Verify delete product successfully.")

def test_delete_product(product_api, mysql):

    # 建立商品
    product = create_product_data()

    create_response = product_api.create_product(product)
    assert create_response.status_code == 201
    product_id = create_response.json()["id"]

    # 刪除商品
    delete_response = product_api.delete_product(product_id)
    attach_response(delete_response)
    assert delete_response.status_code == 204

    # 再查一次API
    get_response = product_api.get_product(product_id)
    attach_response(get_response)
    assert get_response.status_code == 404

    # 驗證DB
    sql = """
    SELECT * FROM products
    WHERE id = %s
    """
    attach_sql(sql)
    result = mysql.query_one(sql,(product_id,))
    assert result is None







