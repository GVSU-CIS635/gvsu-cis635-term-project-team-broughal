def search_value_in_python_file(file_path, target_value):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

            for line_number, line in enumerate(lines, start=1):
                index = 0
                while True:
                    start = line.find('"', index)
                    if start == -1:
                        break
                    end = line.find('"', start + 1)
                    if end == -1:
                        break

                    value = line[start + 1:end]
                    if value == target_value:
                        return
                    index = end + 1

                    def write_to_text_file(line_number, output_file):
                        line_number = str(line_number)
                        try:
                            with open(output_file, 'w') as file:
                                file.write(line_number)
                               
                            #print(f"Column {line_number}")
                        except Exception as e:
                            print(f"Error: {e}")
                    line_number = line_number + 1
                    #target_value_to_find = "Item 3 - Line "
                    #target_value_to_find = str(target_value_to_find)
                    value_from_generator = line_number 
                    output_file_path = "target_columns.txt" 
                    write_to_text_file(value_from_generator, output_file_path)

            print(f"Value '{target_value}' not found in the file.")

    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"Error: {e}")

file_path = "data_headers.py"  
target_value_to_find = "Year Quarter"

search_value_in_python_file(file_path, target_value_to_find)

