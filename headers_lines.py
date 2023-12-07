def search_and_write_to_file(file_path, target_values):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            with open("target_columns.txt", 'w') as output_file:
                for target_value in target_values:
                    found = False
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
                                found = True
                                string_to_write = f"{target_value} - Column {line_number}\n"
                                output_file.write(string_to_write)
                                break
                            index = end + 1
                    if not found:
                        string_to_write = f"Value '{target_value}' not found in the file.\n"
                        output_file.write(string_to_write)

    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"Error: {e}")

file_path = "data_headers.py"
target_values_to_find = ["First Name", "Last Name", "City", "State", "Account Email", "Year Quarter", "Size", "Item 1", "Item 2", "Item 3", "Item 4", "Item 5", "Item 6", "Item 7", "Item 8", "Item 9", "Item 10"]

search_and_write_to_file(file_path, target_values_to_find)
