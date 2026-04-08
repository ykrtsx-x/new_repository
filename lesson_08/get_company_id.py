import requests

url = "https://ru.yougile.com/api-v2/auth/companies"

payload = {
    "login": "",
    "password": "",
    "name": "newCompany"
}
headers = {"Content-Type": "application/json"}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)
