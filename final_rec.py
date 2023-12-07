def generate_final_recommendations():
    # Function to read and process the recommendation files

    # Reading ad_recommendations.txt file
    with open('ad_recommendations.txt', 'r') as ad_file:
        ad_lines = ad_file.readlines()

    # Reading weather files
    with open('weather_cold.txt', 'r') as cold_file:
        cold_items = cold_file.readline().strip().split(', ')
    with open('weather_mid.txt', 'r') as mid_file:
        mid_items = mid_file.readline().strip().split(', ')
    with open('weather_warm.txt', 'r') as warm_file:
        warm_items = warm_file.readline().strip().split(', ')

    # Processing recommendations and generating final recommendations
    final_recommendations = []

    for line in ad_lines:
        values = line.strip().split(', ')
        if values[0] == 'Warm':
            for item in warm_items:
                if item in values[1:]:
                    final_recommendations.append(item)
                    break
        elif values[0] == 'Mid':
            for item in mid_items:
                if item in values[1:]:
                    final_recommendations.append(item)
                    break
        elif values[0] == 'Cold':
            for item in cold_items:
                if item in values[1:]:
                    final_recommendations.append(item)
                    break
        else:
            final_recommendations.append(values[0])

    # Writing final recommendations to final_rec.txt file
    with open('final_rec.txt', 'w') as final_file:
        for item in final_recommendations:
            final_file.write("%s\n" % item)


# Uncomment the following line to call the function directly
generate_final_recommendations()
