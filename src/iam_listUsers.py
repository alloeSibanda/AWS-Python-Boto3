import json
import boto3

def lambda_handler(event, context):
    iam = boto3.client('iam')
    response = iam.list_users()

    users = response['Users']
    for user in users:
        print("IAM User Name:", user['UserName'])
