import csv

# open the CSV file
with open('weather.csv', 'r') as file:
    reader = csv.DictReader(file)

    # initialize variables
    highest_temp = float('-inf')
    lowest_temp = float('inf')
    total_temp = 0
    count = 0
    temp_count = {}
    most_common_temp = None
    most_common_count = 0

    # iterate over each row in the CSV file
    for row in reader:
        # convert temperature value to float
        temp = float(row['Temperature (C)'])

        # update highest and lowest temperatures
        if temp > highest_temp:
            highest_temp = temp
        if temp < lowest_temp:
            lowest_temp = temp

        # update total temperature and count
        total_temp += temp
        count += 1

        # update temperature count dictionary
        if temp in temp_count:
            temp_count[temp] += 1
        else:
            temp_count[temp] = 1

        # update most common temperature
        if temp_count[temp] > most_common_count:
            most_common_temp = temp
            most_common_count = temp_count[temp]

    # calculate average temperature
    average_temp = total_temp / count

    # print results
    print(f'Highest temperature: {highest_temp}')
    print(f'Lowest temperature: {lowest_temp}')
    print(f'Average temperature: {average_temp}')
    print(f'Most common temperature: {most_common_temp} (count: {most_common_count})')


