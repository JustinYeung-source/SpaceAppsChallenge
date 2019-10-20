import statistics
from fileopencsv import *
from GeoMagneticData import *
'''
iterate through the list.
if the element is within the range, then it's accepted and we 
    increment the accepted num
else the element is out of range
    increment the rejected num
'''

def anomalies_col(in_list):
    lower_bound = statistics.mean(in_list) - statistics.stdev(in_list)
    upper_bound = statistics.mean(in_list) + statistics.stdev(in_list)
    anomaly_list = []
    for i in range(len(in_list)):
        temp = []
        if in_list[i] < lower_bound or in_list[i] > upper_bound:
            temp.append(day(i))
            temp.append(hour(i))
            anomaly_list.append(temp)
    return anomaly_list

def anomalies_row(in_list):
    lower_bound = statistics.mean(in_list) - statistics.stdev(in_list)
    upper_bound = statistics.mean(in_list) + statistics.stdev(in_list)
    anomaly_list = []
    for i in range(len(in_list)):
        if in_list[i] < lower_bound or in_list[i] > upper_bound:
            anomaly_list.append(in_list[i])
        else:
            anomaly_list.append(0)
    return anomaly_list

def findGeoDataIndex(theList, theIndex):
    for item in theList:
        if item.getDataIndex() == theIndex:
            return item
    

def make_row_anomalies(filename):
    input_file_list = get_row_csv(filename)
    temp_list = []
    for i in range (len(input_file_list)):
        anom = anomalies_row(input_file_list[i])
        anom.insert(0, str(day(i)) + " - " + str(hour(i)) )
        temp_list.append(anom)

    return temp_list
