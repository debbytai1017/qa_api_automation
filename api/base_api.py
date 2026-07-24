import requests
from config.config import BASE_URL
from utils.logger import log_api

class BaseAPI:

    def __init__(self):
        self.headers = {
            "Content-Type": "application/json"
        }
    def get(self, endpoint):
        response = requests.get(
            f"{BASE_URL}{endpoint}",
            headers=self.headers,
            timeout=10
        )
        log_api(
            method="GET",
            url=f"{BASE_URL}{endpoint}",
            headers=self.headers,
            request_body={},
            response=response
            )
        return response
    
    def post(self, endpoint, data):
        response = requests.post(
            f"{BASE_URL}{endpoint}",
            json=data,
            headers=self.headers,
            timeout=10
        )
        log_api(
            method="POST",
            url=f"{BASE_URL}{endpoint}",
            headers=self.headers,
            request_body=data,
            response=response
            )
        return response
    
    def put(self, endpoint, data):
        response = requests.put(
            f"{BASE_URL}{endpoint}",
            json=data,
            headers=self.headers,
            timeout=10
        )
        log_api(
            method="PUT",
            url=f"{BASE_URL}{endpoint}",
            headers=self.headers,
            request_body=data,
            response=response
            )
        return response
    
    def delete(self, endpoint):
        response = requests.delete(
            f"{BASE_URL}{endpoint}",
            headers=self.headers,
            timeout=10
        )
        log_api(
            method="DELETE",
            url=f"{BASE_URL}{endpoint}",
            headers=self.headers,
            request_body={},
            response=response
            )
        return response