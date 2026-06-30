import requests as rq

GITHUB_LINK = r"https://api.github.com/users"

username = input("Insert a GitHub username please:\n\t>> ")

with rq.get(f"{GITHUB_LINK}/{username}", timeout=5) as response:
    data = response.json()

print(data)
