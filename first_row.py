import csv

def append_first_row_as_strings(input_file):
    predefined_output_file = "headers.py"
    try:
        with open(input_file, 'r') as csv_input:
            csv_reader = csv.reader(csv_input)
            first_row = next(csv_reader)
            first_row_strings = [str(value) for value in first_row]
            with open(predefined_output_file, 'a', newline='') as csv_output:
                csv_writer = csv.writer(csv_output)
                csv_writer.writerow(first_row_strings)
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except StopIteration:
        print("The file is empty or does not contain any rows.")
    except Exception as e:
        print(f"Error: {e}")
input_file_path = input("Please enter the CSV file: ")

append_first_row_as_strings(input_file_path)
