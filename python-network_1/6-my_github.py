import requests
import sys
username = sys.argv[1]
password = sys.argv[2]
url = "https://api.github.com/user"
headers = {
    "Authorization": "Basic " + base64.b64encode(username + ":" + password).decode("utf-8")
}
response = requests.get(url, headers=headers)
if response.status_code == 200:
    print(response.json()["id"])
else:
    print("Error:", response.status_code)
    