import requests
from requests.exceptions import HTTPError
import json

for url in ["https://api.github.com/invalid", "https://api.github.com"]:
    try:
        response  = requests.get(url)
        response.raise_for_status()
    except HTTPError as httperr:
        print(f"HTTP error occured: {httperr}")
    except Exception as err:
        print(f"Another error occured: {err}")
    else: print("Success!!!")


response1  = requests.get("https://api.github.com/invalid")
print(response1.content)
content = response1.content
print(response1.json())
print(json.loads(response1.text))
print(123, response1.content.decode("utf-8"))

response2 = requests.get("http://example.com")
print(f"\n{response2.content.decode('utf-8')}")

print(response2.headers)
print(response2.headers["ETag"])
"""
response.content is a byte object thus it is applicable to use .json()
However, response.text is a str object, so use json.loads(response.text)
"""

res = requests.get("http://example.com")
print(res.headers)
# res.headers["content-type"]
#
# len(res.json()["items"])
