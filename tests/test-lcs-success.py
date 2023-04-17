import requests

# This file tests a valid request to our API using the example given in the project description
# Should return code 200

# Set URL of API
url = 'http://localhost:8080/lcs'

# Set the payload to send to the API
data = {
    "setOfStrings": [
        {"value": "comcast"},
        {"value": "comcastic"},
        {"value": "broadcaster"}
    ]
}

# Send a POST request to the API with the payload data
response = requests.post(url, json=data)

# If successful, print the response
if response.status_code == 200:
    print(response.json())
# If unsuccessful, print the status code and error message
else:
    print(f'Error: {response.status_code} - {response.text}')