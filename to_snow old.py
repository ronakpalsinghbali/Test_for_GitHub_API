# import json
# import os
# from dotenv import load_dotenv


# # # Load environment variables from .env file
# dotenv_path = os.path.join(os.path.dirname(__file__), 'env_file.env')
# load_dotenv(dotenv_path)

# # Load region from environment variable
# REGION = os.getenv('REGION')

# # Read the JSON file
# with open('terraform-output-dev-infra.json', 'r') as f:
#     data = json.load(f)

# # Specify the keys of interest
# keys_of_interest = ['User_Pool_Client_ID', 'User_Pool_Client_secret', 'User_Pool_Domain', 'rest_api_invoke_url']

# # Initialize the output dictionary with the action key-value pair
# output = {
#     "action": "createInfra"
# }

# # Add the specified keys and their values to the output dictionary
# for key in keys_of_interest:
#     if key in data and isinstance(data[key], dict) and 'value' in data[key]:
#         value = data[key]['value']
#         if key == 'User_Pool_Domain':
#             value = f"https://{value}.auth.{REGION}.amazoncognito.com/oauth2/token"
#         output[key] = value

# # Print the output dictionary as a JSON string
# print(json.dumps(output, indent=4))







import json
import os
import requests
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), 'env_file.env')
load_dotenv(dotenv_path)
# Load region from environment variable
REGION = os.getenv('REGION')
# Define your webhook URL
WEBHOOK_URL = os.getenv('WEBHOOK_URL')

# Read the JSON file
with open('./terraform-output-dev-infra.json', 'r') as f:
    data = json.load(f)

# Specify the keys of interest
keys_of_interest = ['User_Pool_Client_ID', 'User_Pool_Client_secret', 'User_Pool_Domain', 'rest_api_invoke_url']

# Initialize the output dictionary with the action key-value pair
output = {
    "action": "createInfra"
}

# Add the specified keys and their values to the output dictionary
for key in keys_of_interest:
    if key in data and isinstance(data[key], dict) and 'value' in data[key]:
        value = data[key]['value']
        if key == 'User_Pool_Domain':
            value = f"https://{value}.auth.{REGION}.amazoncognito.com/oauth2/token"
        output[key] = value

# Convert the output dictionary to JSON string
output_json = json.dumps(output, indent=4)


# Send the JSON output to the webhook URL
response = requests.post(WEBHOOK_URL, json=output)

# Check if the request was successful
if response.status_code == 200:
    print("Output sent to SNOW successfully!")
else:
    print("Failed to send output to SNOW. Status code:", response.status_code)
