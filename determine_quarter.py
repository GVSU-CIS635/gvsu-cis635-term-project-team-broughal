import csv

def get_year_quarter_value_from_csv(csv_file_path, target_txt_file_path):
    try:
        line_number = None
        with open(target_txt_file_path, 'r') as target_file:
            lines = target_file.readlines()

            for line in lines:
                if "Year Quarter - Column " in line:
                    line_number = int(line.split('Column ')[1])
                    #print (line_number)
                    break
            
            if line_number is None:
                print("Unable to find 'Year Quarter - Column ' in the target columns file.")
                return None

        with open(csv_file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            csv_data = list(csv_reader)
            if line_number > len(csv_data[1]):
                print("The line number exceeds the number of columns in the CSV.")
                return None
            value = csv_data[1][line_number - 1]
            return value

    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None
csv_file_path = "nike_user_data.csv" 
target_txt_file_path = "target_columns.txt" 

result = get_year_quarter_value_from_csv(csv_file_path, target_txt_file_path)
    
def find_quarter_from_result(result):
    quarters = {
        "Winter": ["Q1"], 
        "Spring": ["Q2"],
        "Summer": ["Q3"], 
        "Fall": ["Q4"] 
    }

    for quarter, keywords in quarters.items():
        if any(keyword.lower() in result.lower() for keyword in keywords):
            return quarter

    return "No matching quarter found"

result_from_csv = result 
matching_quarter = find_quarter_from_result(result_from_csv)
csv_file_path = "nike_user_data.csv" 
target_txt_file_path = "target_columns.txt" 

result = get_year_quarter_value_from_csv(csv_file_path, target_txt_file_path)

result_from_csv = result 

matching_quarter = find_quarter_from_result(result_from_csv)

with open('quarter.txt', 'w') as file:
    file.write(matching_quarter)
