import requests as rq
from requests.exceptions import HTTPError

GITHUB_LINK = r"https://api.github.com/users"


username = input("Insert a GitHub username please:\n\t>> ")
try:
    with rq.get(f"{GITHUB_LINK}/{username}", timeout=5) as response:
        response.raise_for_status()
        data = response.json()
except HTTPError as e:
    print(e)
else:
    print(f"""
====RESULT====
Login : {data["login"]}
---
Name : {data["name"]}
---
Bio : {data["bio"]}
---
Followers : {data["followers"]}
---
Following : {data["following"]}
---
Public Repositories: {data["public_repos"]} | {data["repos_url"]} 
---
Created At : {data["created_at"]}
==============
    """)
