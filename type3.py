
# import os
# import requests
# import json

# # Read JSON data from file
# with open("out.json", "r") as json_file:
#     json_data = json.load(json_file)

# # Define an empty string to store the concatenated data
# output_string = ""

# # Concatenate all key-value pairs into a single string
# for key, value in json_data.items():
#     if isinstance(value, list):
#         for v in value:
#             output_string += f"{key}: {v}\n"
#     else:
#         output_string += f"{key}: {value}\n"

# # Retrieve webhook URL from environment variable
# webhook_url = os.getenv('WEBHOOK_URL')

# # Send the concatenated data to the webhook
# payload = {"text": output_string}
# headers = {"Content-Type": "application/json"}
# response = requests.post(webhook_url, headers=headers, json=payload)

# if response.status_code == 200:
#     print("Success")
# else:
#     print(f"Error: {response.status_code}")
#     print(response.text)
