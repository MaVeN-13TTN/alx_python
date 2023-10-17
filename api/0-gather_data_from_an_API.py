import requests
import sys

def get_todo(id: int):
    url = f'https://jsonplaceholder.typicode.com/users/{id}'
    url_2 = f'https://jsonplaceholder.typicode.com/users/{id}/todos'
    
    try:
        x = requests.get(url)
        x.raise_for_status()  # Check for HTTP request errors
        json_data = x.json()
        EMPLOYEE_NAME = json_data['name']
        
        y = requests.get(url_2)
        y.raise_for_status()  # Check for HTTP request errors
        json_data_2 = y.json()
        
        TOTAL_NUMBER_OF_TASKS = len(json_data_2)
        NUMBER_OF_DONE_TASKS = 0
        
        for i in json_data_2:
            if i['completed'] == True:
                NUMBER_OF_DONE_TASKS += 1
        
        print(f'Employee {EMPLOYEE_NAME} is done with tasks ({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):')
        for i in json_data_2:
            if i['completed'] == True:
                print(f"\t {i['title']}")

    except requests.exceptions.RequestException as e:
        print("An error occurred while making the HTTP request:")
        print(e)

if __name__ == "__main":
    if len(sys.argv) != 2:
        print("Usage: python your_script_name.py <user_id>")
    else:
        id = int(sys.argv[1])
        get_todo(id)
