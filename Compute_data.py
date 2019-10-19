import statistics

def compute_mean(ALL_data_sets):
    mean_data_set = []

    for row in ALL_data_sets:
        mean_data_set.append(statistics.mean(row))

    return mean_data_set

def compute_standard_deviation(ALL_data_sets):
    stdev_data_set = []

    for row in ALL_data_sets:
        stdev_data_set.append(statistics.stdev(row))

    return stdev_data_set


def remove_outliers(ALL_data_sets, mean_data_set): #REMOVING THE OUTLIERS OF THE DATA
    data_set_no_outliers = []

    column_count = 0

    for row in ALL_data_sets:
        temp_data = []
        for element in row:
            if element >= mean_data_set[column_count]: #if data points are above or equal to the mean value
                temp_data.append(element) #append the data points into the list
            
        data_set_no_outliers.append(temp_data) #append it to another list making it a nested list
        column_count += 1

    return data_set_no_outliers

def just_outliers(ALL_data_sets, mean_data_set): #KEEP JUST THE OUTLIERS OF THE DATA
    data_set_just_outliers = []

    column_count = 0

    for row in ALL_data_sets:
        temp_data = []
        for element in row:
            if element < mean_data_set[column_count]: # if data points are below the mean value
                temp_data.append(element) #append the data points into the list
            
        data_set_just_outliers.append(temp_data) #append it to another list making it a nested list
        column_count += 1

    return data_set_just_outliers