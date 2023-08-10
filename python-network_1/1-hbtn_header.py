import sys
from urllib import requests

def main():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        return
    
    # Get the URL from the command-line argument
    url = sys.argv[1]
    
    # Send an HTTP GET request to the provided URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the value of the 'X-Request-Id' header from the response
        x_request_id = response.headers.get('X-Request-Id')
        
        # Check if the 'X-Request-Id' header is present in the response
        if x_request_id:
            # Print the value of the 'X-Request-Id' header
            print(x_request_id)
        else:
            print("X-Request-Id not found in response headers.")
    else:
        print("Request failed with status code:", response.status_code)

if __name__ == "__main__":
    main()
