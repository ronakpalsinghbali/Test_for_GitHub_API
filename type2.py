
import os
import requests
import json

# Read JSON data from file
with open("out.json", "r") as json_file:
    json_data = json.load(json_file)

# Define the Adaptive Card JSON template
adaptive_card_json = {
    "type": "message",
    "attachments": [
        {
            "contentType": "application/vnd.microsoft.card.adaptive",
            "content": {
                "type": "AdaptiveCard",
                "body": [
                    {
                        "type": "TextBlock",
                        "size": "Medium",
                        "weight": "Bolder",
                        "text": "The infra has been deployed"
                    }
                ],
                "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
                "version": "1.0"
            }
        }
    ]
}

# Add key-value pairs to the Adaptive Card body
for key, value in json_data.items():
    adaptive_card_json["attachments"][0]["content"]["body"].append({
        "type": "TextBlock",
        "text": f"- {key}: {value}"
    })

# Retrieve webhook URL from environment variable
webhook_url = os.getenv('WEBHOOK_URL')

# Send the Adaptive Card to the webhook
headers = {"Content-Type": "application/json"}
response = requests.post(webhook_url, headers=headers, json=adaptive_card_json)

if response.status_code == 200:
    print("Success")
else:
    print(f"Error: {response.status_code}")
    print(response.text)
