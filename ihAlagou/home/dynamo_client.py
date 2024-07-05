# dynamo_client.py
import boto3
from django.conf import settings

dynamodb = boto3.resource(
    'dynamodb',
    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    region_name=settings.AWS_REGION_NAME
)

table = dynamodb.Table('raspiData_v1')  # Substitua pelo nome da sua tabela



def get_items():
    response = table.scan()
    return response.get('Items', [])

