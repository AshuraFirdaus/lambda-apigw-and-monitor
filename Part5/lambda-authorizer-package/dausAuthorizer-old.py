import jwt
import json

def lambda_handler(event, context):
    token = event['headers']['Authorization']
    secret = 'FillInYourSecretHere'  # Fill this with your secret key from the linux openssl rand command
    # fill it with your secret key from the linux openssl rand command

    try:
        # Decode the JWT token
        decoded_token = jwt.decode(token, secret, algorithms=['HS256'])
        user_id = decoded_token['user_id']  # assuming user_id is a field in the token
    except:
        # If the token is invalid, return a 401 Unauthorized response
        return {
            'statusCode': 401,
            'body': json.dumps({'message': 'You are unauthorized to access this resource.'}),
        }

    # If the token is valid, allow the request to proceed with the user_id as the principal
    return {
        'principalId': user_id,
        'policyDocument': {
            'Version': '2012-10-17',
            'Statement': [
                {
                    'Action': 'execute-api:Invoke',
                    'Effect': 'Allow',
                    'Resource': event['methodArn']
                }
            ]
        }
    }
# This Lambda function is an authorizer for API Gateway that checks the JWT token in the Authorization header.
# It decodes the token using a secret key and retrieves the user_id from it.
# 2025 - Ashura Firdaus
# If the token is valid, it returns a policy document allowing access to the API.