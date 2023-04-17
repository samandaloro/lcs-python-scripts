import requests

# This file tests an invalid request to our API - empty POST body
# Should return Error code 400, message: POST body cannot be empty

# Set URL of API
url = 'http://localhost:8080/lcs'

# Send a POST request to the API
response = requests.post(url)

# If successful, print the response
if response.status_code == 200:
    print(response.json())
# If unsuccessful, print the status code and error message
else:
    print(f'Error: {response.status_code} - {response.text}')