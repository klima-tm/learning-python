import requests

response = requests.get("https://api.github.com/users/klima-tm")

print(response.status_code)
print(response.json())
data = response.json()
print(data["login"]), print(data["public_repos"]), print(data["created_at"])