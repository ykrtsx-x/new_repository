import requests

url = "https://ru.yougile.com/api-v2/auth/keys"

payload = {
    "login": "",
    "password": "",
    "companyId": ""
}

response = requests.post(url, json=payload)

print(response.status_code)
print(response.text)
