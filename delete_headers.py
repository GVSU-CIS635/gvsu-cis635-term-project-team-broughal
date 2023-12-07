import os

class Headers:
    def add_quotes_to_values(input_file, output_file):
        try:
            with open(input_file, 'r') as file_input:
                lines = file_input.readlines()
                quoted_values = [[f'"{val.strip()}"' for val in line.split(',')] for line in lines]
                with open(output_file, 'w') as file_output:
                    for row in quoted_values:
                        file_output.write(','.join(row) + '\n')
        except FileNotFoundError:
            print("File not found. Please check the file path.")
        except Exception as e:
            print(f"Error: {e}")
    input_file_path = "headers.py"
    output_file_path = "header_rows.py"
    add_quotes_to_values(input_file_path, output_file_path)

    #this deletes headers.py as we no longer need it
    def process_and_delete_file(input_file):
        try:
            predefined_file_to_delete = "headers.py"
            os.remove(predefined_file_to_delete)
        except FileNotFoundError:
            print("File not found. Please check the file path.")
        except Exception as e:
            print(f"Error: {e}")
    input_file_path = "headers.py"
    process_and_delete_file(input_file_path)
