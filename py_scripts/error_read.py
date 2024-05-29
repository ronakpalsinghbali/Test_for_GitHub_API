import json
import re

def remove_escape_codes(text):
    # Regular expression to match ANSI escape codes
    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
    # Remove escape codes from the text
    return ansi_escape.sub('', text)

def read_error_log(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                if "Error:" in line:
                    # Clean up the line to remove any leading/trailing whitespace and unwanted characters
                    error_message = line.strip()
                    # Remove ANSI escape codes
                    error_message = remove_escape_codes(error_message)
                    # Split the error message to get the key-value pair
                    error_parts = error_message.split(": ", 1)
                    if len(error_parts) == 2:
                        key, value = error_parts
                        # Create the dictionary with the specified action and error
                        error_dict = {
                            "action": "createInfra",
                            "Error": value
                        }
                        # Print the dictionary as a JSON-like string
                        print(json.dumps(error_dict, indent=2))
                    else:
                        print("Error: Unable to parse the error message correctly.")
                    break  # Stop after the first error message
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

if __name__ == "__main__":
    # Replace 'error_test.log' with the actual path to your error log file if necessary
    log_file_path = '../error.log'
    read_error_log(log_file_path)




# {
#   "action": "createInfra",
#   "User_Pool_Client_IErrorD": "expected cidr_block to contain a valid Value, got: 172.16.0.0/ with err: invalid CIDR address: 172.16.0.0/",
# }