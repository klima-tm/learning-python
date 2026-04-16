import requests

def get_github_user(username):
    response = requests.get(f"https://api.github.com/users/{username}")
    if response.status_code == 200:
        return response.json()
    else:
        return None

print(get_github_user("klima"))