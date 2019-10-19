import csv
'''
This file just reads the csv file contents and organizes it into nested lists
'''
class Extract:
    def __init__(self, location_name, location, longitude, latitude):
        self.longtitude = longitude
        self.latitude = latitude
        self.location_name = location_name
        self.location = (location_name,longitude,latitude)
    
    def get_location(self, location, longitude, latitude):
        return self.location

def num_sites(n):
    if n <= 4:
        return 1
    return num_sites(n - 4) + 1

def get_column_csv(filename):  
    input_csvfile = csv.reader(open(filename, "r"))
    row1 = next(input_csvfile)

    temp_list = [[] for _ in range(num_sites(len(row1) - 5))]

    row_count = 0
    element_count = 0

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
