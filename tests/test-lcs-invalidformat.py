import requests

# This file tests an invalid request to our API - incorrect format of the request
# Should return Error code 400, message: Request is not in the correct format

# Set URL of API
url = 'http://localhost:8080/lcs'

# Set the payload to send to the API
data = {
    "strings": [
        {"word": "comcast"},
        {"word": "comcastic"},
        {"word": "broadcaster"}
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