def generate_final_recommendations():
    
    with open('ad_recommendations.txt', 'r') as ad_file:
        ad_lines = ad_file.readlines()

    with open('weather_cold.txt', 'r') as cold_file:
        cold_items = cold_file.readline().strip().split(', ')
    with open('weather_mid.txt', 'r') as mid_file:
        mid_items = mid_file.readline().strip().split(', ')
    with open('weather_warm.txt', 'r') as warm_file:
        warm_items = warm_file.readline().strip().split(', ')

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

    with open('final_rec.txt', 'w') as final_file:
        for item in final_recommendations:
            final_file.write("%s\n" % item)

generate_final_recommendations()
