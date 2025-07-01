import json
import uuid
import boto3
from datetime import datetime

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("ContactFormMessages")

def lambda_handler(event, context):
    try:
        body = json.loads(event.get("body", "{}"))

        # Validate required fields
        for field in ("name", "email", "message"):
            if field not in body:
                return {
                    "statusCode": 400,
                    "body": json.dumps({"error": f"Missing field: {field}"})
                }

        # Construct the item
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
            "body": json.dumps({"message": "Contact form submitted successfully!"})
        }

    except Exception as e:
        print("Error:", e)
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Internal server error"})
        }