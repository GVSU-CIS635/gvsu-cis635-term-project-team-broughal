def add_quotes_to_values(input_file, output_file):
    try:
        with open(input_file, 'r') as file_input:
            lines = file_input.readlines()

            # Adding quotation marks around each value
            quoted_values = [[f'"{val.strip()}"' for val in line.split(',')] for line in lines]

            with open(output_file, 'w') as file_output:
                for row in quoted_values:
                    file_output.write(','.join(row) + '\n')
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"Error: {e}")

# Provide the path of the input CSV file
input_file_path = "headers.py"

# Provide the path of the output file where quoted values will be saved
output_file_path = "header_rows.py"

# Call the function to add quotation marks to each value
add_quotes_to_values(input_file_path, output_file_path)
