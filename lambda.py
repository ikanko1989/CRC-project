"Lambda function for dynamoDB get/update item from table"
import json
import boto3

# Create a DynamoDB resource object
client = boto3.resource("dynamodb")
# Access the VisitorCounter table
table = client.Table("VisitCounter")


def lambda_handler(event, context):
    result = table.get_item(Key={"ID": "1"})
    counter = result["Item"]["views"]
    counter = int(counter) + 1
    print(counter)
    table.put_item(Item={"ID": "1", "views": counter})

    # Serialize the response body as JSON
    body = {"views": counter}
    return {"statusCode": 200, "body": json.dumps(body)}


"""""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """""" ""


"""
"some examples of lambda;"
"Lambda function for dynamoDB interaction"
import json
import boto3

client = boto3.client("dynamodb")


def lambda_handler(event, context):
    table = client.Table("VisitCounter")
    print(table.Count)


import boto3

client = boto3.client("dynamodb")


def lambda_handler(event, context):
    result = client.scan(TableName="VisitCounter")
    for item in result["Items"]:
        print(item)
    return result["Items"]


"Lambda function for dynamoDB print table content"

import boto3
import json

client = boto3.client("dynamodb")


def lambda_handler(event, context):
    result = client.scan(TableName="VisitCounter")
    body = json.dumps(result["Items"])
    for item in result["Items"]:
        print(item)
    return {"statusCode": 200, "body": body}


"Lambda function for dynamoDB put in items in table"

import json
import boto3

client = boto3.client("dynamodb")


def lambda_handler(event, context):
    result = client.put_item(
        TableName="VisitCounter",
        Item={
            "ID": {
                "S": "2",
            },
            "Timestamp": {
                "N": "2",
            },
            "Count": {
                "N": "2",
            },
        },
    )

    return {"status": "200", "body": json.dumps(result)}
"""
