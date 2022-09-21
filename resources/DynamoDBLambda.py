import boto3
import json
import os

def lambda_handler(event, context):
    
    dynamodb = boto3.resource('dynamodb')
    tableName = os.environ["Alarm_key"]
    table = dynamodb.Table(tableName)

    message = json.loads(event['Records'][0]['Sns']['Message'])
    
    table.put_item(
        Item={
            'MetricName': message["Trigger"]["MetricName"],
            'Timestamp': event['Records'][0]['Sns']['Timestamp'],
            'Region': message["Region"],
            'AlarmReason': message["NewStateReason"],
            'URL': message["Trigger"]["Dimensions"][0]["value"],
        },
    )
