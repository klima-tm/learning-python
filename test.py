import requests
response = requests.get("https://api.github.com/users/tdinh-me")
print(response.status_code)
print(response.json())