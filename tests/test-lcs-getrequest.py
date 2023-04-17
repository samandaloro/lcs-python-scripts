import requests

# This file tests an invalid request to our API - GET request instead of POST
# Should return Error code 405, message: Request must be a POST

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
response = requests.get(url, json=data)

# If successful, print the response
if response.status_code == 200:
    print(response.json())
# If unsuccessful, print the status code and error message
else:
    print(f'Error: {response.status_code} - {response.text}')