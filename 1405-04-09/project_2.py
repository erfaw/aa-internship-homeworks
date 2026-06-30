import requests as rq

url = input(
    "Insert a site address (URL)\nURL format must be 'https://<site address>'"
)

with rq.get(url=url, timeout=10) as response:
    response.raise_for_status()
    if response.status_code == 200:
        print("Website is Online!✅")
    else:
        print("Website is Offline!❌")
