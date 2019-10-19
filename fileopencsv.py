import csv
'''
This file just reads the csv file contents and organizes it into nested lists
'''
class Extract:
    def __init__(self, location_name, location, longitude, latitude):
        self.longtitude = longitude
        self.latitude = latitude
        self.longtitude = longitude
        self.location_name = location_name
        self.location = ()
    
    def get_location(self, longitude, latitude):
        self.location = (location_name,longitude,latitude)

def num_sites(n):
    if n <= 4:
        return 1
    return num_sites(n - 4) + 1

def file_interpret_csv(filename):  
    input_csvfile = csv.reader(open(filename, "r"))
    row1 = next(input_csvfile)

    temp_data = [[] for _ in range(num_sites(len(row1) - 5))]

    row_count = 0
    element_count = 0

    for row in input_csvfile:
        row_count += 1
        for element in row:
            
            if element == "" or row_count <= 4 or "-" in element:
                continue
            else:
                
                temp_data[element_count].append(float(element))
                element_count += 1
        element_count = 0

    return temp_data


print(file_interpret_csv('dataset2_full.csv'))