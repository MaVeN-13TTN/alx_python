import sys
from urllib import requests

def main():
    # Get the URL from command-line argument
    url = sys.argv[1]
    
    # Send a GET request to the provided URL
    response = requests.get(url)
    
    # Display the body of the response
    print(response.text)
    
    # Check if the status code is greater than or equal to 400
    if response.status_code >= 400:
        print("Error code:", response.status_code)

if __name__ == "__main__":
    main()
