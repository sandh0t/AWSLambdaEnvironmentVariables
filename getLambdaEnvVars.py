##!/usr/bin/python

# Color constants
OK = '\033[92m'
INFO = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'

import subprocess
import sys
import argparse


parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument('-p', '--profile', help='Enter the AWS Profile Name')
args = parser.parse_args()

def list_lambda_variables(profile):
    command = f"aws lambda list-functions --query 'Functions[*].FunctionName' --profile {profile}" + " | awk -F'\"' '{print $2}'"
    get_lambdas = subprocess.run(command, stdout=subprocess.PIPE, text=True, shell=True)

    if get_lambdas.returncode != 0:
        print(f"Error: {get_lambdas.stderr}")
        return
    
    lambda_list = get_lambdas.stdout.splitlines()
    for elem in lambda_list:
        if elem != None and elem != "":
            command = f"aws lambda get-function-configuration --function-name {elem} --query 'Environment.Variables' --profile {profile}"
            get_lambda_vars = subprocess.run(command, stdout=subprocess.PIPE, text=True, shell=True)
            
            if "{" in get_lambda_vars.stdout:
                print(OK + "[+] Found Environment Variables in Lambda Function: " + ENDC + INFO + elem + ENDC)
                print(get_lambda_vars.stdout)
  


if not args.profile:
        print(FAIL + '[-] Enter the AWS Profile name, using -p, check -h for more details' + ENDC)
        sys.exit(0)

list_lambda_variables(args.profile)
