import os

# this goes through and deletes the files that we used temporarily while finding out with advertisement to recommend
class Delete_Extras:
    def process_and_delete_file(input_file):
        try:
            predefined_file_to_delete = "ad_recommendations.txt"
            os.remove(predefined_file_to_delete)
        except FileNotFoundError:
            print("File not found. Please check the file path.")
        except Exception as e:
            print(f"Error: {e}")
    input_file_path = "ad_recommendations.txt"
    process_and_delete_file(input_file_path)

    def process_and_delete_file(input_file):
        try:
            predefined_file_to_delete = "ad_recommendations.txt"
            os.remove(predefined_file_to_delete)
        except FileNotFoundError:
            print("File not found. Please check the file path.")
        except Exception as e:
            print(f"Error: {e}")
    input_file_path = "ad_recommendations.txt"
    process_and_delete_file(input_file_path)

    def process_and_delete_file(input_file):
        try:
            predefined_file_to_delete = "all_user_data.txt"
            os.remove(predefined_file_to_delete)
        except FileNotFoundError:
            print("File not found. Please check the file path.")
        except Exception as e:
            print(f"Error: {e}")
    input_file_path = "all_user_data.txt"
    process_and_delete_file(input_file_path)

    def process_and_delete_file(input_file):
        try:
            predefined_file_to_delete = "data_headers.py"
            os.remove(predefined_file_to_delete)
        except FileNotFoundError:
            print("File not found. Please check the file path.")
        except Exception as e:
            print(f"Error: {e}")
    input_file_path = "data_headers.py"
    process_and_delete_file(input_file_path)

    def process_and_delete_file(input_file):
        try:
            predefined_file_to_delete = "final_rec.txt"
            os.remove(predefined_file_to_delete)
        except FileNotFoundError:
            print("File not found. Please check the file path.")
        except Exception as e:
            print(f"Error: {e}")
    input_file_path = "final_rec.txt"
    process_and_delete_file(input_file_path)

    def process_and_delete_file(input_file):
        try:
            predefined_file_to_delete = "quarter.txt"
            os.remove(predefined_file_to_delete)
        except FileNotFoundError:
            print("File not found. Please check the file path.")
        except Exception as e:
            print(f"Error: {e}")
    input_file_path = "quarter.txt"
    process_and_delete_file(input_file_path)

    def process_and_delete_file(input_file):
        try:
            predefined_file_to_delete = "target_columns.txt"
            os.remove(predefined_file_to_delete)
        except FileNotFoundError:
            print("File not found. Please check the file path.")
        except Exception as e:
            print(f"Error: {e}")
    input_file_path = "target_columns.txt"
    process_and_delete_file(input_file_path)

