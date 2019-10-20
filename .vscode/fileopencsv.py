import csv
from GeoMagneticData import *

#recursively gathers the number of sites, incrementing by 1 each time n is decremented.
def num_sites(n):
    if n <= 4:
        return 1
    return num_sites(n - 4) + 1

#recursively gathers the day of the index provided, incrementing by 1 each time n is decremented.
def day(n):
    if (n < 24):
        return 1
    return 1 + day(n - 24)

#recursively gathers the hour of the index provided, returning n + 1 when n is less than 24 after the decrements.
def hour(n):
    if (n < 24):
        return n + 1
    return hour(n - 24)

def get_column_csv(filename):  
    #open a file and skip the header
    input_csvfile = csv.reader(open(filename, "r"))
    row1 = next(input_csvfile)
    #gather the amount of lists we'll need
    temp_list = [[] for _ in range(num_sites(len(row1) - 5))]
    #counters for the iteration
    row_count = 0
    element_count = 0
    #iterate through the rows/columns, appending if we get a value and increasing our row count.
    for row in input_csvfile:
        for element in row:
            if element == "" or row_count < 3 or "-" in element:
                continue
            else:
                temp_list[element_count].append(float(element))
                element_count += 1
        row_count += 1
        element_count = 0
    return temp_list
    
def headers(filename):
    input_csvfile = csv.reader(open(filename, "r"))
    #skip the first two lines and make a temp_data a nested list
    next(input_csvfile)
    row2 = next(input_csvfile)
    temp_data = get_column_csv(filename)
    # Create geo_list to hold regular statistics values
    geo_list = []
    geo_class_list = []
    first = True
    num_index = 0
    for data in row2:
        i = 0
        # skip over blanks and the first loop
        if(data == "" or first):
            first = False
            continue
        else:
            # add all data that is not a blank
            geo_list.append(data)
        # once we have three values
        if(len(geo_list) == 3):
            # create the class
            geo_class_list.append(GeoMagneticData(geo_list[0], geo_list[1], geo_list[2], num_index))
            geo_list = []
            for i in range(len(temp_data)):
                # add statistical values to the class
                geo_class_list[num_index].add(temp_data[num_index][i])
            num_index += 1
    return geo_class_list

def get_row_csv(filename):
    input_csvfile = csv.reader(open(filename, "r"))
    #ignore the header
    for i in range(4):
        next(input_csvfile)
    row_list = []
    #begin iteration through the csv
    for row in input_csvfile:
        temp = []
        #create a temp list and append only values into the row
        for element in row:
            if(element == "" or "-" in element):
                continue
            else:
                temp.append(float(element))
        #append the temp list into the row list
        row_list.append(temp)
    return row_list

def export_csv_file(header,data_set,filename):
    new_file = open(filename, "w")
    #write the headers into the first row
    new_file.write(",")
    for index in range(len(header)):
        new_file.write(str(header[index]))
    #write the remaining rows in the data_set into the csv file
    new_file.write("\n")
    for index in range(len(data_set)):
        for element in range(len(data_set[index])):
            new_file.write(str(data_set[index][element]))
            new_file.write(",")
        new_file.write("\n")
    new_file.close()