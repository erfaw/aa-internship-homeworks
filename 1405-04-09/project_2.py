import requests as rq

url = input(
    "Insert a site address (URL)\nURL format must be 'https://<site address>'\n\t >> "
)

with rq.get(url=url, timeout=10) as response:
    response.raise_for_status()
    if response.status_code == 200:
        print(f"Website is Online!✅ (status code: {response.status_code})")
    else:
        print(f"Website is Offline!❌ (status code: {response.status_code})")
