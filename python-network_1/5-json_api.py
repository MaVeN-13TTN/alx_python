import requests
import sys
if len(sys.argv) == 2:
    q = sys.argv[1]
else:
    q = ""
response = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})
if response.status_code == 200:
    if response.json():
        print("[{}] {}".format(response.json()["id"], response.json()["name"]))
    else:
        print("No result")
else:
    print("Not a valid JSON")