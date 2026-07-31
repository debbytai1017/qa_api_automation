import pytest
import os
import platform
import sys
from pathlib import Path
from api.product_api import ProductAPI
from database.mysql_helper import MySQLHelper

@pytest.fixture
def product_api():
    return ProductAPI()

@pytest.fixture
def mysql():
    return MySQLHelper()

def pytest_sessionfinish(session, exitstatus):
    """測試結束後建立 Allure Environment 資訊"""

    results_dir = Path("allure-results")
    results_dir.mkdir(exist_ok=True)

    environment_data = {
        "Python Version": sys.version.split()[0],
        "Operating System": platform.system(),
        "Test Framework": "pytest",
        "API Client": "requests",
        "Backend": "Laravel 13",
        "Database": "MySQL 8.0",
        "Report": "Allure Report",
        "Execution": (
            "GitHub Actions"
            if os.getenv("GITHUB_ACTIONS") == "true"
            else "Local"
        ),
    }

    content = "\n".join(
        f"{key} = {value}"
        for key, value in environment_data.items()
    )

    environment_file = results_dir / "environment.properties"
    environment_file.write_text(content, encoding="utf-8")