import requests as rq
from requests.exceptions import Timeout

url = input(
    "Insert a site address (URL)'\n\t >> "
)
if not 'https://' in url and not 'http://' in url:
    url = "https://"+url

try:
    with rq.get(url=url, timeout=5) as response:
        try:
            response.raise_for_status()
        except ConnectionError as e:
            print(f"Seems there is a problem with your network connection.\n{e}")
        else:
            if response.status_code == 200:
                print(f"Website is Online!✅ (status code: {response.status_code})")
            else:
                print(f"Website is Offline!❌ (status code: {response.status_code})")
except Timeout as e: 
    print(f"Request timeout. please try again.\n\t\tError message: {e}")
