from api.base_api import BaseAPI

class ProductAPI(BaseAPI):

    # @staticmethod
    def get_products(self):
        return self.get("/products")
    
    def get_product(self, product_id):
        return self.get(
             f"/products/{product_id}"
             )

    def create_product(self, data):
        return self.post(
            "/products", data
        )
    
    def update_product(self, product_id, data):
        return self.put(
            f"/products/{product_id}", data
        )
    
    def delete_product(self, product_id):
        return self.delete(
            f"/products/{product_id}"
        )