import json

def lambda_handler(event, context):
    products = [
        {"id": 1, "name": "iPhone", "price": 999.99}
    ]

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(products)
    }
