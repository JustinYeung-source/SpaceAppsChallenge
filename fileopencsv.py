import csv

class Extract:
    def __init__(self, longitude, latitude, maxMag, date):
        self.date = date
        self.longtitude = longitude
        self.latitude = latitude
        self.maxMag = maxMag

def main():
    input_file_list = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    input_file_list = fileopen_csv("dataset1.csv")
    print(input_file_list)

def fileopen_csv(filename):
    input_csvfile = csv.reader(open(filename, "r"))
    temp_data = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

    row_count = 0
    element_count = 0

    for row in input_csvfile:
        row_count += 1
        for element in row:
            
            if element == "" or row_count <= 4 or "-" in element:
                continue
            else:
                
                temp_data[element_count].append(element)
                element_count += 1
        element_count = 0

    return temp_data

if __name__ == "__main__":
    main()
