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


import os
import json

# Read JSON data from file
with open("out.json", "r") as json_file:
    json_data = json.load(json_file)

# Define an empty list to store the concatenated data
output_list = []

# Concatenate all key-value pairs into a single string
for key, value in json_data.items():
    if isinstance(value, list):
        # Convert list items to strings
        value_str = ", ".join(map(str, value))
        output_list.append(f"{key}: {value_str}")
    else:
        output_list.append(f"{key}: {value}")

# Join the list elements into a single string
output_string = "\n".join(output_list)

# Print the concatenated data
print(output_string)

