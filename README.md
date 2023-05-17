# AWS Lambda Environment Variable List Script

This Python script allows you to list the environment variables for all Lambda Functions within a specific AWS account. It provides a convenient way to retrieve and analyze the environment configurations to find  hardcoded secrets or exposed credentials.

## Prerequisites
Before running the script, ensure you have the following prerequisites:

Python 2.x/3.x installed on your system
AWS CLI configured with valid credentials for the desired AWS account


## Usage

'''
python getLambdaEnvVars.py -p aws_profile
'''

License
This project is licensed under the MIT License. Feel free to use and modify the script according to your needs.

Disclaimer
Please use this script responsibly and ensure that you have the necessary permissions and legal rights to access and retrieve environment variables for Lambda Functions within your AWS account.

Note: This script only retrieves environment variables and does not modify or delete any resources in your AWS account.
