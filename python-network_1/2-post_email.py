import sys
from urllib import requests

def main():
    # Get the URL and email from command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]
    
    # Data to be sent in the POST request
    data = {'email': email}
    
    # Send a POST request with the email parameter to the provided URL
    response = requests.post(url, data=data)
    
    # Display the body of the response
    print(response.text)

if __name__ == "__main__":
    main()
