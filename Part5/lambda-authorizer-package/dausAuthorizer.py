import jwt

def lambda_handler(event, context): 
# Lambda function to authorize API requests using JWT
    secret = 'FillInYourSecretHere'
    # fill it with your secret key from the linux openssl rand command
# This secret should be stored securely, e.g., in AWS Secrets Manager or Parameter Store.
    try:
        token = event.get('authorizationToken') 
        decoded_token = jwt.decode(token, secret, algorithms=['HS256'])
        user_id = decoded_token.get('user_id', 'anonymous')
    except Exception:
        raise Exception("Unauthorized") 
# If the token is invalid or decoding fails, raise an exception
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
        },
        'context': {
            'user_id': user_id
        }
    }
# This function decodes the JWT token, extracts the user ID, and returns an IAM policy document that allows access to the API method specified in the event.
# If the token is invalid, it raises an "Unauthorized" exception.
