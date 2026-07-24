import uuid
def generate_product_name():
    # 建立隨機字串id並取前8碼
    random_id = str(uuid.uuid4())[:8]
    return f"Pixel_{random_id}"