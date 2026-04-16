import requests

def get_github_user(username):
    response = requests.get(f"https://api.github.com/users/{username}")
    if response.status_code == 200:
        return response.json()
    else:
        return None

def save_to_file(data, filename):
    with open(filename, "w") as file:
        for key, value in data.items():
            file.write(f"{key}: {value}\n")

username = "klima-tm"
user_data = get_github_user(username)

if user_data:
    save_to_file(user_data, "github_profile.txt")
    print("Saved successfully")
else:
    print("User not found")
#New block
def print_summary(data):
    fields = ["login", "public_repos", "followers", "created_at"]
    for field in fields:
        print(f"{field}: {data.get(field, 'N/A')}")

print_summary(user_data)