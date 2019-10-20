import csv
from GeoMagneticData import *


class Extract:
    def __init__(self, longitude, latitude, locname):
        self.longtitude = longitude
        self.latitude = latitude
        self.locname = locname
        self.location = (locname, latitude, longitude)

    def get_location(self, location, latitude, longitude, locname):
        return self.location

def num_sites(n):
    if (n <= 4):
        return 1
    return num_sites(n - 4) + 1

def day(n):
    if (n < 24):
        return 1
    # increase day by 1, decrease n by 24 in each recursion
    return 1 + day(n - 24)

def hour(n):
    if n == 0:
        return 1
    if (n < 24):
        return n + 1
    # we decrease by amount of hours in a day until we're left with the amount of hours
    return hour(n - 24)

def getrow_csv(filename):
    input_csvfile = csv.reader(open(filename, "r"))

    #ignore the header
    for i in range (4):
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

def getcol_csv(filename):
    input_csvfile = csv.reader(open(filename, "r"))
    #remove the first 5 columns (1), read the amount of max(db/dt), that's our amount of lists
    row1 = next(input_csvfile)
    row2 = next(input_csvfile)
    temp_data = [[] for _ in range(num_sites(len(row1) - 5))]
    
    #iterate through the list, removing elements that don't match the criteria and adding them to their
    #respective list
    row_count = 0
    element_count = 0
    for row in input_csvfile:
        for element in row: 
            if element == "" or row_count < 2 or "-" in element:
                continue
            else:
                temp_data[element_count].append(float(element))
                element_count += 1
        
        row_count += 1
        element_count = 0

    geo_class_list = getGeoList(temp_data, row2)

    return geo_class_list


def getGeoList(temp_data, row):
    # Create geo_list to hold regular statistics values
    geo_list = []
    geo_class_list = []
    first = True
    num_index = 0
    
    for data in row:
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
