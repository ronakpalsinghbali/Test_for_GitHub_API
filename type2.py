
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
webhook_url = "https://cloudeq.webhook.office.com/webhookb2/b3640a0c-c584-4cbf-86e9-f21a977cdbe7@dbd61555-f8c0-4db8-83e3-d55f7565507d/IncomingWebhook/1302baa57b0c4ca9ad18085c06b585a4/c4ddcb12-279b-4bf8-adf0-5d89e3df88ba"

# Send the Adaptive Card to the webhook
headers = {"Content-Type": "application/json"}
response = requests.post(webhook_url, headers=headers, json=adaptive_card_json)

if response.status_code == 200:
    print("Success")
else:
    print(f"Error: {response.status_code}")
    print(response.text)
