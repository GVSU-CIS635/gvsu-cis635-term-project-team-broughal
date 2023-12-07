import csv

states = {
    "Warm": ["AL", "AR", "AZ", "FL", "GA", "HI", "LA", "MS", "NM", "OK", "SC", "TX"], # 12 total states
    "Mid": ["CA", "DC", "IA", "IN", "KS", "MO", "NC", "NE", "NV", "OH", "TN", "VA", "WV"], # 12 total states plus Washington DC
    "Cold": ["AK", "CO", "CT", "DE", "ID", "IL", "KY", "MA", "MD", "ME", "MI", "MN", "MT", "ND", "NH", "NJ", "NY", "OR", "PA", "RI", "SD", "UT", "VT", "WA", "WI", "WY"] # 26 total states
}

def get_state_category(state_value):
    for category, state_list in states.items():
        if state_value in state_list:
            return category
    return "Unknown"  # This is just in case the data for some reason has a non US state

csv_file_path = "nike_user_data.csv"
target_txt_file_path = "target_columns.txt"

def get_item_value_from_csv(item_number, line_data):
    try:
        line_number = None
        results = [] 
        with open(target_txt_file_path, 'r') as target_file:
            lines = target_file.readlines()

            for line in lines:
                if f"Item {item_number} - Column " in line:
                    line_number = int(line.split('Column ')[1])
                    break
            
            if line_number is None:
                print(f"Unable to find 'Item {item_number} - Column ' in the target columns file.")
                return None

        if line_number > len(line_data):
            print("The line number exceeds the number of columns in the CSV.")
            return None
        value = line_data[line_number - 1]
        results.append(value) 
        return results 

    except Exception as e:
        print(f"Error: {e}")
        return None

with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader) # this skips the header row in nike_user_data.csv
    
    with open('all_user_data.txt', 'w') as file:
        with open(target_txt_file_path, 'r') as target_file:
            lines = target_file.readlines()
            for line in lines:
                if "State - Column " in line:
                    state_column_number = int(line.split('Column ')[1])
                    break
            
            if 'state_column_number' not in locals():
                print("Unable to find 'State - Column ' in the target columns file.")
                exit(1)
        
        for row in csv_reader:
            results_list = [] 
            state_value = row[state_column_number - 1].strip() if len(row) > state_column_number else None
            state_category = get_state_category(state_value)
            
            if state_category != "Unknown":
                file.write(f"{state_category}, ")
                
                for item_number in range(1, 11):
                    result = get_item_value_from_csv(item_number, row)
                    if result:
                        results_list.extend(result) 
                
                file.write(', '.join(results_list) + '\n')
            else:
                print("State column index exceeds row length in CSV.")
