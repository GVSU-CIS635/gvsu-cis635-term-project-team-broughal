def create_recommendations_csv():
    with open('recommendations.csv', 'w') as rec_file:
        rec_file.write('First Name,Last Name,Account Email,Ad Recommendation\n')

    with open('final_rec.txt', 'r') as rec_file:
        recommendations = rec_file.readlines()

    
    with open('target_columns.txt', 'r') as target_file:
        lines = target_file.readlines()
        first_name_col = None
        last_name_col = None
        email_col = None
        for line in lines:
            if 'First Name - Column' in line:
                first_name_col = int(line.split()[-1])
            elif 'Last Name - Column' in line:
                last_name_col = int(line.split()[-1])
            elif 'Account Email - Column' in line:
                email_col = int(line.split()[-1])

    with open('nike_user_data.csv', 'r') as data_file:
        header = data_file.readline().strip().split(',')
        data = [line.strip().split(',') for line in data_file]

    with open('recommendations.csv', 'a') as rec_output_file:
        for row_index, row in enumerate(data):
            if first_name_col and last_name_col and email_col:
                first_name = row[first_name_col - 1]
                last_name = row[last_name_col - 1]
                email = row[email_col - 1]
                recommendation = recommendations[row_index].strip()

                rec_output_file.write(f'{first_name},{last_name},{email},{recommendation}\n')

create_recommendations_csv()

print("The CSV file 'recommendations.csv' has the recommended advertisements for each user from 'nike_user_data.csv'")
