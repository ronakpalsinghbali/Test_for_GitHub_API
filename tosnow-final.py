import json
import os
import requests

# from dotenv import load_dotenv
# Load environment variables from .env file
# dotenv_path = os.path.join(os.path.dirname(__file__), 'env_file.env')
# load_dotenv(dotenv_path)

# Define the API endpoint URL for token generation
token_url = os.getenv('TOKEN_URL')

# Define the payload (data to be sent to the API) for token generation
token_payload = {
    'grant_type': os.getenv('GRANT_TYPE'),
    'client_id': os.getenv('CLIENT_ID'),
    'client_secret': os.getenv('CLIENT_SECRET'),
    'username': os.getenv('SNOW_USERNAME'),
    'password': os.getenv('SNOW_PASSWORD')
}

# Make a POST request to the API to generate the token
token_response = requests.post(token_url, data=token_payload)

# Check if the token request was successful (status code 200)
if token_response.status_code == 200:
    # Parse the token response JSON
    token_response_json = token_response.json()
    
    # Extract the access token from the token response
    access_token = token_response_json.get('access_token')
    
    # Define the second API endpoint URL and other necessary parameters
    snow_url = os.getenv('SNOW_URL')
    region = os.getenv('REGION')

    # Read the JSON file containing data for the second API call
    with open('./terraform-output-dev-infra.json', 'r') as f:
        data = json.load(f)

    # Specify the keys of interest from the JSON file
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
                value = f"https://{value}.auth.{region}.amazoncognito.com/oauth2/token"
            output[key] = value

    # Convert the output dictionary to JSON string
    output_json = json.dumps(output, indent=4)

    # Define headers for the second API call with the access token
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    # Send the JSON output to the SNOW URL with the headers
    snow_response = requests.post(snow_url, json=output, headers=headers)

    
    print(snow_response.json())

else:
    print("Failed to generate token. Status code:", token_response.status_code)
