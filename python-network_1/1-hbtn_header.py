"""takes in a URL, sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the response.

Usage: ./1-hbtn_header.py <URL>
"""
# Import the requests module
from urllib import requests

# Define the URL to fetch
url = 'https://alu-intranet.hbtn.io/status'

# Send a GET request to the URL
response = requests.get(url)

# Check if the response status code is 200 (OK)
if response.status_code == 200:
    # Parse the JSON data from the response
    data = response.json()
    
    # Display the header for the response body
    print("Body response:")
    
    # Display the type of the data
    print("\t- type:", type(data))
    
    # Display the content of the data
    print("\t- content:", data)
else:
    # Display an error message along with the status code
    print("Error:", response.status_code)
