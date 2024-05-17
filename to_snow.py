import json
import os
from dotenv import load_dotenv


# # Load environment variables from .env file
dotenv_path = os.path.join(os.path.dirname(__file__), 'env_file.env')
load_dotenv(dotenv_path)

# Load region from environment variable
REGION = os.getenv('REGION')

# Read the JSON file
with open('out.json', 'r') as f:
    data = json.load(f)

# Specify the keys of interest
keys_of_interest = ['User_Pool_Client_ID', 'User_Pool_Client_secret', 'User_Pool_Domain', 'rest-api-invoke-url']

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

# Print the output dictionary as a JSON string
print(json.dumps(output, indent=4))