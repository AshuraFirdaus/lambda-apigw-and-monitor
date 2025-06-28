import jwt
import json

def lambda_handler(event, context):
    token = event['headers']['Authorization']
    secret = 'PmvCtfr1Hy4mA5QhTARjywokZRh4KjEyGfkXdGvULMVMhJHj79h3L14CTwB5WN5n9PtMfdazGSgNRJlb97ni7GBlphKCo6rLT4SN36kBi7UIIkw6H8sSgS5WmmdcG7UT7t8LfIGbIxJ9nzEOH5uNiZhWFLQKdaNIHckEdF1E8cDfjDfbvrSENvLCq2NNfOYh5MOdDrXy5gmhl0de12T5VMvOeC9WlcT2M1wKjdSKZWUZwzivVN3xrZ4EUM3DIcv1rWVYeKSF8hp7SJbEhT52ntHwuUI1jxGvHF7XtVHtZXWUV8oKdbPTuVuZkVA8LQEKsuHnndNj8AGcmCxDp0yGiA=='  # This is a placeholder for your secret key
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