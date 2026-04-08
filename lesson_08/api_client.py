import requests

BASE_URL = "https://ru.yougile.com/api-v2"


class YougileAPI:

    def __init__(self, token):
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def create_project(self, title):
        url = f"{BASE_URL}/projects"
        payload = {"title": title}
        return requests.post(url, json=payload, headers=self.headers)

    def get_project(self, project_id):
        url = f"{BASE_URL}/projects/{project_id}"
        return requests.get(url, headers=self.headers)

    def update_project(self, project_id, title):
        url = f"{BASE_URL}/projects/{project_id}"
        payload = {"title": title}
        return requests.put(url, json=payload, headers=self.headers)
