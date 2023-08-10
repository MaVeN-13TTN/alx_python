'''
Python script that fetches https://alu-intranet.hbtn.io/status. 
The script uses the requests package to make the request and then prints the body of the response.
'''
import requests

if __name__ == "__main__":
    # Define the URL to fetch
    url = "https://alu-intranet.hbtn.io/status"
    
    # Send an HTTP GET request to the specified URL
    response = requests.get(url)
    
    # Print the header for the response body
    print("Body response:")
    
    # Print the type of the response content
    print("\t- type:", type(response.text), end="$\n")
    
    # Print the content of the response body
    print("\t- content:", response.text, end="$\n")
