def read_error_log(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if "Error:" in line:
                    print(line.strip())
                    break  # Stop after the first error message
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

if __name__ == "__main__":
    # Replace 'error_test.log' with the actual path to your error log file if necessary
    log_file_path = 'error.log'
    read_error_log(log_file_path)
