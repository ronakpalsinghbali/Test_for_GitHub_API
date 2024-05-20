import requests

# Define the API endpoint URL
url = 'https://cloudeqincdemo1.service-now.com/oauth_token.do'

# Define the payload (data to be sent to the API)
payload = {
    'grant_type': 'password',
    'client_id': '0a63458468a76d108b99e8b45659c490',
    'client_secret': '[bq1UE6!{x',
    'username': 'AutoparkWebservices',
    'password': 'Autopark@120'
}

# Make a POST request to the API with the payload
response = requests.post(url, data=payload)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the response JSON
    response_json = response.json()
    
    # Print the entire response
    print(response_json)
    
    # Extract and print the access token
    access_token = response_json.get('access_token')
    print("Access Token:", access_token)
else:
    print("Failed to generate token. Status code:", response.status_code)
