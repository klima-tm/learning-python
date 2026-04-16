import requests

usernames = ["klima-tm", "levelsio", "ajeetdsouza"]

def get_github_user(username):
    response = requests.get(f"https://api.github.com/users/{username}")
    if response.status_code == 200:
        return response.json()
    return None

users = []
for username in usernames:
    data = get_github_user(username)
    if data:
        users.append(data)
        print(f"Fetched: {username}")

print(f"\nTotal users fetched: {len(users)}")

def save_report(users):
    with open("report.txt", "w") as file:
        file.write("GitHub User Comparison Report\n")
        file.write("=" * 40 + "\n\n")
        for user in users:
            file.write(f"Username: {user.get('login', 'N/A')}\n")
            file.write(f"Repos: {user.get('public_repos', 'N/A')}\n")
            file.write(f"Followers: {user.get('followers', 'N/A')}\n")
            file.write(f"Created: {user.get('created_at', 'N/A')}\n")
            file.write("-" * 40 + "\n")

save_report(users)
print("Report saved to report.txt")