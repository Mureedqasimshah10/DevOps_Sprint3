from operator import imod
from pickle import TRUE
import aws_cdk as core
import aws_cdk.assertions as assertions
from aws_cdk.assertions import Match

from sprint3.sprint3_stack import Sprint3Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in sprint3/sprint3_stack.py
# def test_sqs_queue_created():
#     app = core.App()
#     stack = Sprint3Stack(app, "sprint3")
#     template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
def test_lambda_created():
    app = core.App()
    # Below two lines are synthsizing it
    stack = Sprint3Stack(app, "sprint3")
    template = assertions.Template.from_stack(stack)
    # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.assertions/Template.html
    template.resource_count_is("AWS::Lambda::Function", 2)

def test_SNS_created():
    app = core.App()
    stack = Sprint3Stack(app, "sprint3")
    template = assertions.Template.from_stack(stack)
    # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.assertions/Template.html
    # Assert that we have created two subscription
    template.resource_count_is("AWS::SNS::Subscription", 2)

def test_dynamoDB_created():
    app = core.App()
    stack = Sprint3Stack(app, "sprint3")
    template = assertions.Template.from_stack(stack)
    # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.assertions/Template.html
    # Assert that we have created a table
    template.resource_count_is("AWS::DynamoDB::Table", 1)


def test_DynamoDBTable_created():
    app = core.App()
    stack = Sprint3Stack(app, "sprint3")
    template = assertions.Template.from_stack(stack)
    # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.assertions/Template.html
    template.has_resource_properties("AWS::DynamoDB::Table", 
   {
                 "KeySchema": [
                   {
                     "AttributeName": "MetricName",
                     "KeyType": "HASH"
                   },
                   {
                     "AttributeName": "Timestamp",
                     "KeyType": "RANGE"
                   }
                 ],
                 "AttributeDefinitions": [
                   {
                     "AttributeName": "MetricName",
                     "AttributeType": "S"
                   },
                   {
                     "AttributeName": "Timestamp",
                     "AttributeType": "S"
                   }
                 ],
                 "ProvisionedThroughput": {
                   "ReadCapacityUnits": 5,
                   "WriteCapacityUnits": 5
                 }
               },
    )

def test_creats_alarm():
    app = core.App()
    stack = Sprint3Stack(app, "sprint3")
    template = assertions.Template.from_stack(stack)
    # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.assertions/Template.html
    template.has_resource_properties("AWS::CloudWatch::Alarm",
        {
            "Namespace": "mureedwh_lambda",
            "MetricName": Match.any_value(),
            "Dimensions": [
                {
                    "Name": "URL",
                    "Value": Match.any_value(),
                },
            ],
        },
    )

def test_subscription():
    app = core.App()
    stack = Sprint3Stack(app, "sprint3")
    template = assertions.Template.from_stack(stack)
    # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.assertions/Template.html
    template.has_resource_properties("AWS::SNS::Subscription",
            {
                 "Protocol": "lambda",
                 "TopicArn": {
                   "Ref": "Alarmnotification0FD235A9"
                 },
                 "Endpoint": {
                   "Fn::GetAtt": [
                     "QasimDynamoDBLambda6B63579A",
                     "Arn"
                   ]
                 }
               }
      )

def test_lambda_property():
    app = core.App()
    stack = Sprint3Stack(app, "sprint3")
    template = assertions.Template.from_stack(stack)
    # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.assertions/Template.html
    template.has_resource_properties("AWS::IAM::Role",
        {
                 "ManagedPolicyArns": [
                   {
                     "Fn::Join": [
                       "",
                       [
                         "arn:",
                         {
                           "Ref": "AWS::Partition"
                         },
                         ":iam::aws:policy/CloudWatchFullAccess"
                       ]
                     ]
                   },
                   {
                     "Fn::Join": [
                       "",
                       [
                         "arn:",
                         {
                           "Ref": "AWS::Partition"
                         },
                         ":iam::aws:policy/AmazonDynamoDBFullAccess"
                       ]
                     ]
                   }
                 ]
               }
        
    )

def test_to_json():
    app = core.App()
    stack = Sprint3Stack(app, "sprint3")
    template = assertions.Template.from_stack(stack)

    # https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.assertions/Template.html
    # Assert that the CloudFormation template deserialized into an object
    template.to_json()
