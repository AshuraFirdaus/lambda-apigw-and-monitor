#Scrapped
#  import boto3
# import json
# import requests

# # Replace this 3 below with your own values from your AWS Lambda Authorizer and API Gateway
# # Make sure you have the necessary permissions to invoke the Lambda function and access the API Gateway endpoint
# AUTHORIZER_ARN = 'arn:aws:lambda:ap-southeast-3:537144582764:function:dausAuthorizer'
# ENDPOINT = 'https://nmrp4dt8bj.execute-api.ap-southeast-3.amazonaws.com/PROD/v2/helloworld'
# TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxNDA2MjAwMTI0IiwibmFtZSI6Ik11aGFtYWQgRmlyZGF1cyIsImFkbWluIjp0cnVlLCJpYXQiOjE3NDg3MTA4MDAsImV4cCI6MTc4MDI0NjgwMH0.GWBEGfAvFhNAwhVGUH80LHZWAbSIGVIpeWkL1FwLaMM'

# # Create a Boto3 client for invoking Lambda functions
# session = boto3.Session(profile_name='firdaus07')
# lambda_client = session.client('lambda', region_name='ap-southeast-3')
# #lambda_client = boto3.client('lambda', region_name='ap-southeast-3')

# # Invoke the Lambda Authorizer with the JWT token
# response = lambda_client.invoke(
#     FunctionName=AUTHORIZER_ARN,
#     InvocationType='RequestResponse',
#     Payload='{"headers": {"Authorization": "%s"}, "methodArn": "%s"}' % (TOKEN, ENDPOINT)
# )

# # Parse the response from the Lambda Authorizer
# auth_response = response['Payload'].read().decode('utf-8')
# auth_response = json.loads(auth_response)

# print(auth_response)

# # # Check if the request is authorized
# # if auth_response['policyDocument']['Statement'][0]['Effect'] == 'Allow':
# #     # If authorized, make a request to the API Gateway endpoint with the JWT token
# #     headers = {'Authorization': TOKEN}
# #     response = requests.get(ENDPOINT, headers=headers)
# #     print(response.text)
# # else:
# #     # If unauthorized, print an error message
# #     print('You are unauthorized to access this resource.')

# #     print(auth_response)

# if 'policyDocument' in auth_response and \
#    auth_response['policyDocument']['Statement'][0]['Effect'] == 'Allow':
#     headers = {'Authorization': TOKEN}
#     response = requests.get(ENDPOINT, headers=headers)
#     print(response.text)
# else:
#     print("Unauthorized or Authorizer error occurred.")

