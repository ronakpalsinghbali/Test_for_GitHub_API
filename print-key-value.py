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




# import json

# # Read the JSON file
# with open('out.json', 'r') as f:
#     data = json.load(f)

# # Print the key-value pairs
# for key, values in data.items():
#     if isinstance(values, list):
#         # If the value is a list, print each value separately
#         for value in values:
#             # Convert list item to string, remove square brackets and single quotes
#             value_str = str(value).strip("[]").replace("'", "")
#             print(f"{key}: {value_str}")
#     else:
#         # If the value is not a list, print it directly
#         print(f"{key}: {values}")

import json

# Read the JSON file
with open('out.json', 'r') as f:
    data = json.load(f)

# Define an empty list to store the concatenated data
output_list = []

# Concatenate all key-value pairs into a single string
for key, values in data.items():
    if isinstance(values, list):
        # If the value is a list, print each value separately
        for value in values:
            # Convert list item to string, remove square brackets and single quotes
            value_str = str(value).strip("[]").replace("'", "")
            output_list.append(f"{key}: {value_str}")
    else:
        # If the value is not a list, print it directly
        output_list.append(f"{key}: {values}")

# Join the list elements into a single string
output_string = "\n".join(output_list)

# Print the data with double quotes at the start and end
print(f'"{output_string}"')
