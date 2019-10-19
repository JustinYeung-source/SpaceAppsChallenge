import csv

class Extract:
    def __init__(self, longitude, latitude, locname):
        self.longtitude = longitude
        self.latitude = latitude
        self.locname = locname

    def get_location(self, longitude, latitude, locname):
        return (longitude, latitude, locname)

def num_sites(n):
    if n <= 4:
        return 1
    return num_sites(n - 4) + 1

def day(n):
    if (n < 24):
        return 1
    return 1 + day(n - 24)

def hour(n):
    if (n < 24):
        return n
    return hour(n - 24)

def fileopen_csv(filename):
    input_csvfile = csv.reader(open(filename, "r"))

    #remove the first 5 columns (1), read the amount of max(db/dt), that's our amount of lists
    row1 = next(input_csvfile)
    temp_data = [[] for _ in range(num_sites(len(row1) - 5))]

    #iterate through the list, removing elements that don't match the criteria and adding them to their
    #respective list
    row_count = 0
    element_count = 0
    for row in input_csvfile:
        for element in row:            
            if element == "" or row_count < 3 or "-" in element:
                continue
            else:
                temp_data[element_count].append(float(element))
                element_count += 1
        row_count += 1
        element_count = 0
    return temp_data

if __name__ == "__main__":
    main()
