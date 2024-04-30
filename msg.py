# import requests
# import json

# # Read JSON data from file
# with open("out.json", "r") as json_file:
#     json_data = json.load(json_file)

# # Your Adaptive Card JSON template
# adaptive_card_json = f"""
# {{
#   "type": "message",
#   "attachments": [
#     {{
#       "contentType": "application/vnd.microsoft.card.adaptive",
#       "content": {{
#         "type": "AdaptiveCard",
#         "body": [
#           {{
#             "type": "TextBlock",
#             "text": "Cloudwatch Logs ARN: {json_data['cloudwatch_logs_arn']}"
#           }},
#           {{
#             "type": "TextBlock",
#             "text": "Cloudwatch Logs Name: {json_data['cloudwatch_logs_name']}"
#           }},
#           {{
#             "type": "TextBlock",
#             "text": "DB Instance Endpoint: {json_data['db_instance_endpoint']}"
#           }},
#           {{
#             "type": "TextBlock",
#             "text": "Event Rule ARN: {json_data['event_rule_arn']}"
#           }},
#           {{
#             "type": "TextBlock",
#             "text": "Event Rule Name: {json_data['event_rule_name']}"
#           }},
#           {{
#             "type": "TextBlock",
#             "text": "Function Name: {json_data['function_name']}"
#           }},
#           {{
#             "type": "TextBlock",
#             "text": "Invoke ARN: {json_data['invoke_arn']}"
#           }},
#           {{
#             "type": "TextBlock",
#             "text": "Lambda ARN: {json_data['lambda_arn']}"
#           }},
#           {{
#             "type": "TextBlock",
#             "text": "REST API Invoke URL: {json_data['rest-api-invoke-url']}"
#           }},
#           {{
#             "type": "TextBlock",
#             "text": "Secret ARN: {json_data['secret_arn']}"
#           }},
#           {{
#             "type": "TextBlock",
#             "text": "Secret ID: {json_data['secret_id']}"
#           }},
#           {{
#             "type": "TextBlock",
#             "text": "Secret ID Version ID: {json_data['secret_id_version_id']}"
#           }},
#           {{
#             "type": "TextBlock",
#             "text": "Secret Replica: {json_data['secret_replica']}"
#           }},
#           {{
#             "type": "TextBlock",
#             "text": "Secret Tags All: {json_data['secret_tags_all']}"
#           }},
#           {{
#             "type": "TextBlock",
#             "text": "Secret Version ID: {json_data['secret_version_id']}"
#           }},
#           {{
#             "type": "TextBlock",
#             "text": "Version: {json_data['version']}"
#           }}
#         ],
#         "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
#         "version": "1.0"
#       }}
#     }}
#   ]
# }}
# """

# # Your webhook URL
# webhook_url = "https://cloudeq.webhook.office.com/webhookb2/b3640a0c-c584-4cbf-86e9-f21a977cdbe7@dbd61555-f8c0-4db8-83e3-d55f7565507d/IncomingWebhook/1302baa57b0c4ca9ad18085c06b585a4/c4ddcb12-279b-4bf8-adf0-5d89e3df88ba"

# headers = {
#     "Content-Type": "application/json"
# }

# response = requests.post(webhook_url, headers=headers, data=adaptive_card_json)

# if response.status_code == 200:
#     print("Success")
# else:
#     print(f"Error: {response.status_code}")
#     print(response.text)



import requests

# Your Adaptive Card JSON template
adaptive_card_json = """
{
  "type": "message",
  "attachments": [
    {
      "contentType": "application/vnd.microsoft.card.adaptive",
      "content": {
        "type": "AdaptiveCard",
        "body": [
          {
            "type": "TextBlock",
            "text": "Message Text"
          }
        ],
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
        "version": "1.0"
      }
    }
  ]
}
"""

# Your webhook URL
webhook_url = "https://cloudeq.webhook.office.com/webhookb2/b3640a0c-c584-4cbf-86e9-f21a977cdbe7@dbd61555-f8c0-4db8-83e3-d55f7565507d/IncomingWebhook/1302baa57b0c4ca9ad18085c06b585a4/c4ddcb12-279b-4bf8-adf0-5d89e3df88ba"

headers = {
    "Content-Type": "application/json"
}

# Read JSON data from file
with open("out.json", "r") as json_file:
    json_data = json_file.read()

response = requests.post(webhook_url, headers=headers, data=json_data)

if response.status_code == 200:
    print("Success")
else:
    print(f"Error: {response.status_code}")
    print(response.text)
