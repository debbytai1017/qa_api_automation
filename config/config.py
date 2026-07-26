import os

BASE_URL = os.getenv(
    "BASE_URL",
    "http://127.0.0.1:8000/api"
)

MYSQL_CONFIG = {
    "host": os.getenv("DB_HOST", "127.0.0.1"),
    "user": os.getenv("DB_USERNAME", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_DATABASE", "practice"),
}