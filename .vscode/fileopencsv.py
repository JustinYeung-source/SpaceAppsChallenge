import csv
from GeoMagneticData import *


class Data:
    def __init__(self, longitude, latitude, maxMag, date):
        self.date = date
        self.longtitude = longitude
        self.latitude = latitude
        self.maxMag = maxMag

def main():
    input_file_list = fileopen_csv("dataset1.csv")
    print(input_file_list)

def num_sites(n):
    if n <= 4:
        return 1
    return num_sites(n - 4) + 1

def fileopen_csv(filename):
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

    #print("first =", temp_data[0][1])
    
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
    for data in geo_class_list:
        print(data.getData())
    return geo_class_list

if __name__ == "__main__":
    main()
