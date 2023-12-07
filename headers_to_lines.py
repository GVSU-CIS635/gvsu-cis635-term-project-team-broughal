import os

class Lines:
    def convert_headers_to_lines(input_file, output_file):
        try:
            with open(input_file, 'r') as file:
                values = file.read().strip().split(',')
                with open(output_file, 'w') as out_file:
                    for value in values:
                        out_file.write(value.strip() + '\n')
        except FileNotFoundError:
            print("File not found. Please check the file path.")
        except Exception as e:
            print(f"Error: {e}")
    input_file_path = "header_rows.py"  
    output_file_path = "data_headers.py"  
    convert_headers_to_lines(input_file_path, output_file_path)

    #this deletes header_rows.py as we no longer need it
    def process_and_delete_file(input_file):
        try:
            predefined_file_to_delete = "header_rows.py"
            os.remove(predefined_file_to_delete)
        except FileNotFoundError:
            print("File not found. Please check the file path.")
        except Exception as e:
            print(f"Error: {e}")
    input_file_path = "header_rows.py"
    process_and_delete_file(input_file_path)
