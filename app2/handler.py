import json
import os 
import sys
import uuid
from urllib.parse import unquote_plus


#   def create_thumbnail(event, context):
#       body = {
#        "message": "Go Serverless v1.0! Your function executed successfully!",
#        "input": event,
#    }

#    response = {"statusCode": 200, "body": json.dumps(body)}

#    print(response)

#    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
#    """
#    return {
#        "message": "Go Serverless v1.0! Your function executed successfully!",
#        "event": event
    }
#    """


s3_client = boto3.client("s3")


def create_thumbnail(event, context):
    try:
        for record in event["Records"]:
            bucket = record["s3"]["bucket"]["name"]
            key = unquote_plus(record["s3"]["object"]["key"])
            print(f"The object name is {bucket}/{key}")
    except Exception as e:
        print(e)
