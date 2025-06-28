import requests

ENDPOINT = 'https://nmrp4dt8bj.execute-api.ap-southeast-3.amazonaws.com/PROD/v2/helloworld'
TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxNDA2MjAwMTI0IiwibmFtZSI6Ik11aGFtYWQgRmlyZGF1cyIsImFkbWluIjp0cnVlLCJpYXQiOjE3NDg3MTA4MDAsImV4cCI6MTc4MDI0NjgwMH0.GWBEGfAvFhNAwhVGUH80LHZWAbSIGVIpeWkL1FwLaMM'

headers = {
    'Authorization': TOKEN
}

response = requests.get(ENDPOINT, headers=headers)
print(response.status_code)
print(response.text)
