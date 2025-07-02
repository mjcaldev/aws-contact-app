import json
import uuid
import boto3
from datetime import datetime

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("ContactFormMessages")

def lambda_handler(event, context):
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Allow-Methods": "OPTIONS,POST"
    }

    # Handle preflight request
    if event.get("httpMethod") == "OPTIONS":
        return {
            "statusCode": 200,
            "headers": headers,
            "body": ""
        }

    try:
        body = json.loads(event.get("body", "{}"))

        # Validate required fields
        for field in ("name", "email", "message"):
            if field not in body:
                return {
                    "statusCode": 400,
                    "headers": headers,
                    "body": json.dumps({"error": f"Missing field: {field}"})
                }

        item = {
            "id": str(uuid.uuid4()),
            "name": body["name"],
            "email": body["email"],
            "message": body["message"],
            "timestamp": datetime.utcnow().isoformat()
        }

        table.put_item(Item=item)

        return {
            "statusCode": 200,
            "headers": headers,
            "body": json.dumps({"message": "Contact form submitted successfully!"})
        }

    except Exception as e:
        print("Error:", e)
        return {
            "statusCode": 500,
            "headers": headers,
            "body": json.dumps({"error": "Internal server error"})
        }