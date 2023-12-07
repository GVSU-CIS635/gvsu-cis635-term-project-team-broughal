from collections import Counter

def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.readlines()

def write_recommendations(recommendations):
    with open('ad_recommendations.txt', 'w') as file:
        for line_count, recommendation in enumerate(recommendations, start=1):
            file.write(f"{recommendation}\n")

def get_highest_count_items(line):
    items = line.strip().split(', ')[-10:]
    item_count = Counter(items)
    max_count = max(item_count.values())
    highest_count_items = [item for item, count in item_count.items() if count == max_count]
    return highest_count_items, max_count

# Read the file and find the item(s) with the highest count per line
file_data = read_file('all_user_data.txt')
recommendations = []

for line in file_data:
    highest_count_items, max_count = get_highest_count_items(line)
    
    # If there is a tie between two or more items
    if len(highest_count_items) > 1:
        recommendations.append(f"{line.strip().split(', ')[0]}, {', '.join(highest_count_items)}")
    else:
        recommendations.append(f"{highest_count_items[0]}")

# Write the item(s) with the highest count per line to ad_recommendations.txt
write_recommendations(recommendations)
