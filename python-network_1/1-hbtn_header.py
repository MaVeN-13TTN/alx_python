"""takes in a URL, sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the response.

Usage: ./1-hbtn_header.py <URL>
"""
# Import the requests module 
import requests
import sys
url = str(sys.argv[1])
response = requests.get('http://' + url) # Send GET Request
print ("X-Request-ID;", response.headers['x-requestid'])



