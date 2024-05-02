import json

# Read the JSON file
with open('out.json', 'r') as f:
    data = json.load(f)

# Print the key-value pairs
for key, values in data.items():
    if isinstance(values, list):
        # If the value is a list, print each value separately
        for value in values:
            print(f"{key}: {value}")
    else:
        # If the value is not a list, print it directly
        print(f"{key}: {values}")



