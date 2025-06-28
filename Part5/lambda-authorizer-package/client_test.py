import requests

ENDPOINT = 'https://nmrp4dt8bj.execute-api.ap-southeast-3.amazonaws.com/PROD/v2/helloworld'
TOKEN = 'FillYourJWTTokenHere'  # Replace with your actual JWT token from the JWT.io

headers = {
    'Authorization': TOKEN
}

response = requests.get(ENDPOINT, headers=headers)
print(response.status_code)
print(response.text)
