
# Welcome to My Sprint3 project!

This is a Sprint3 project for a multi-satge pipeline deployment and configuration with atutomatic rollback for my Web Health Monitoring Application.

## Acknowledgements

I would like to thank Dr. Ayesha Binte Ashfaq for being helpful thorugout this week and for her precious time. In addition, I would like to thank `SkipQ` to give the golden opportunity to do this project.

## Objective

The objective of this Sprint3 is to build up on Sprint2 and create a multi-stage pipeline having Beta/Gamma and Prod stage using CDK and also deploy the project code in one or multiple regions. The core objectives are listed as follows:

* The Each stage must have bake Times, code-review, and test blockers.
* Write unit/integration tests for the web crawler.
* Emit CloudWatch metrics and alarms for the operational health of the web crawler, including memory and time-to-process each crawler run.
* Automate rollback to the last build if metrics are in alarm. Manage README files and run-books in markdown on GitHub.

## Environment Setup

* Installing the Linux Subsystem on Windows.
* Downloading VS Code as the IDE and it's extension "WSL-Remote" to run VS Code within the Linux Subsystem.
* Installing Python3.
* Installing the AWS Command Line Interface Version 2 (AWS CLI V2).
* Cloning this Github repository.
* Installing Node Version Manager (NVM) to download and install Node.js and Node Packet Manager (npm) to install   Javascript packages.
* Installing the aws-cdk package via NPM.
* Installing and creating a virual environment on the Linux Console and installing the required dependencies.

## How to Run

* Open the ubuntu terminal and clone the git repository using git clone
* Confirm that your working directory is Sprint3
* Activate the virtual environment using command source .venv/bin/activate
* Now pip run requirements.txt file to install all required packages
* Configure the aws using aws configure and add your email and username to global configuration using command git config --global user.email "your-email.gmail.com" and git config --global user.name "your-name".
* Synth and Deploy the project on Consile using cdk synth and cdk deploy.

## TECHNOLOGIES USED

* AWS CI/CD Pipeline
* AWS CloudWatch
* AWS CodeBuild
* AWS CodePipeline
* AWS CloudWatch
* Github
* The full procedure to setup AWS and RUN the Sprint3 is given in next step.

## What we achieve

The end goal of this sprint was to automate the build and deploy process of th Web Health Monitoring application using a multi-stage pipeline. For this purpose, I created a multi-stage pipeline architecture and added source and build artifact. I created alpha stage for unit testing and prod stage for manual approval and added them to the pipeline. The unit tests were created for alpha stage to check each unit of the application before deployment. At the end, I created metric and alarm at deployment satge and configured the Lambda deployment and rollback using deployment groups.

## AWS Console

* Go to the AWS Console and monitore logs of WHLambda function for Availability and Latency.
* Go to the AWS Console and monitore logs of DBLambda function for records (if you print them).
* Go to the AWS DynamoDB database and check the item tables for records.
* Go to the AWS CodePipeline and check the deployment of all stages.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation
 * `source .venv/bin/activate` activate virtual environment
 * `pip install -r requirements.txt` install requirements

 ## Refrences

 * https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Query.html#:~:text=and%20Indexes%3A%20.NET-,Key%20Condition%20Expressions%20for%20Query,-To%20specify%20the
 * https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_sns_subscriptions/EmailSubscription.html
 * https://docs.aws.amazon.com/lambda/index.html
 * https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html
 * https://docs.aws.amazon.com/cdk/api/v1/python/aws_cdk.aws_dynamodb/TableProps.html
 * https://docs.aws.amazon.com/cdk/api/v1/docs/@aws-cdk_core.RemovalPolicy.html

 # Author
 * Mureed Qasim Shah

Enjoy!
