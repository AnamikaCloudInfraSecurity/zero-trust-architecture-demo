import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    try:
        s3.put_object(
            Bucket='zero-trust-secure-bucket',
            Key='test.txt',
            Body='Zero Trust Access Verified'
        )

        return {
            "statusCode": 200,
            "body": json.dumps("✅ Access granted (Authorized)")
        }

    except Exception as e:
        return {
            "statusCode": 403,
            "body": json.dumps(f"❌ Access denied: {str(e)}")
        }