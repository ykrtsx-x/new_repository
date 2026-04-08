import pytest
import requests

BASE_URL = "https://ru.yougile.com/api-v2"

LOGIN = ""
PASSWORD = ""
COMPANY_ID = ""


@pytest.fixture
def token():
    url = f"{BASE_URL}/auth/keys"

    payload = {
        "login": LOGIN,
        "password": PASSWORD,
        "companyId": COMPANY_ID
    }

    response = requests.post(url, json=payload)
    return response.json()["key"]


@pytest.fixture
def api(token):
    from api_client import YougileAPI
    return YougileAPI(token)


@pytest.fixture
def created_project(api):
    response = api.create_project("Test Project")
    project_id = response.json()["id"]
    return project_id
