import json
import os

# Load region from environment variable
REGION = os.getenv('REGION')

# Read the JSON file
with open('out.json', 'r') as f:
    data = json.load(f)

# Print the key-value pairs
for key, values in data.items():
    if isinstance(values, dict) and 'value' in values:
        # Check if the value is a dictionary containing 'value' key
        value = values['value']
        if key == 'User_Pool_Domain':
            # Prefix and suffix the value with the specified URL
            value = f"https://{value}.auth.{REGION}.amazoncognito.com"
            print(f"{key}: {value}")
        elif isinstance(value, list):
            # If the value is a list, print the first item
            print(f"{key}: {value[0]}")
        else:
            # If the value is not a list, print it directly
            print(f"{key}: {value}")



# OLD
# import json

# # Read the JSON file
# with open('out.json', 'r') as f:
#     data = json.load(f)

# # Print the key-value pairs
# for key, values in data.items():
#     if isinstance(values, list):
#         # If the value is a list, print each value separately
#         for value in values:
#             print(f"{key}: {value}")
#     else:
#         # If the value is not a list, print it directly
#         print(f"{key}: {values}")


# NEW
# import json

# # Read the JSON file
# with open('out.json', 'r') as f:
#     data = json.load(f)

# # Print the key-value pairs
# for key, values in data.items():
#     if isinstance(values, dict) and 'value' in values:
#         # Check if the value is a dictionary containing 'value' key
#         value = values['value']
#         if isinstance(value, list):
#             # If the value is a list, print the first item
#             print(f"{key}: {value[0]}")
#         else:
#             # If the value is not a list, print it directly
#             print(f"{key}: {value}")

# NEW 2
# import json
# from dotenv import load_dotenv
# import os

# # Load environment variables from .env file
# dotenv_path = os.path.join(os.path.dirname(__file__), 'env_file.env')
# load_dotenv(dotenv_path)

# # Load region from environment variable
# REGION = os.getenv('REGION')


# # Read the JSON file
# with open('out.json', 'r') as f:
#     data = json.load(f)

# # Print the key-value pairs
# for key, values in data.items():
#     if isinstance(values, dict) and 'value' in values:
#         # Check if the value is a dictionary containing 'value' key
#         value = values['value']
#         if key == 'User_Pool_Domain':
#             # Prefix and suffix the value with the specified URL
#             value = f"https://{value}.auth.{REGION}.amazoncognito.com"
#             print(f"{key}: {value}")
#         elif isinstance(value, list):
#             # If the value is a list, print the first item
#             print(f"{key}: {value[0]}")
#         else:
#             # If the value is not a list, print it directly
#             print(f"{key}: {value}")

