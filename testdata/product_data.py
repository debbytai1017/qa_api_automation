from utils.random_data import generate_product_name

# 定義function每呼叫一次重新建立新的product name
def create_product_data():
    return {
    "name": generate_product_name(),
    "price" :32000,
    "stock": 30
}

def update_product_data():
    return {
    "name": generate_product_name(),
    "price": 38000,
    "stock": 40
}

# CREATE_PRODUCT_CASES = [
#     {
#         "name": "Pixel",
#         "price": 32000,
#         "stock": 40
#     },
#     {
#         "name": "iPhone",
#         "price": 45000,
#         "stock": 30
#     },
#     {
#         "name": "Galaxy",
#         "price": 28000,
#         "stock": 35
#     }
# ]