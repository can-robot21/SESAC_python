import requests

url = "http://www.example.com"

response = requests.get(url)

print(response.status_code)
print(response.text)