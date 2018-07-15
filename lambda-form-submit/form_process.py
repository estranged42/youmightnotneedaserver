# This python lambda function will process the input from a POST event from an API Gateway
# endpoint, and generate an email to a user.

import os
import subprocess
import datetime
import dateutil.tz
import dateutil.parser
import logging
import json
import boto3

sns = boto3.client('sns')

# Convert a datetime object into milleseconds from the unix epoch
def unix_time_millis(dt):
    epoch = datetime.datetime.fromtimestamp(0, dateutil.tz.gettz('UTC') )
    return int( (dt - epoch).total_seconds() * 1000.0 )

def lambda_handler(event, context):
    rootlogger = logging.getLogger()
    rootlogger.setLevel(logging.INFO)
    logging.info("-" * 100)
    logging.info(json.dumps(event, indent=2))
    
