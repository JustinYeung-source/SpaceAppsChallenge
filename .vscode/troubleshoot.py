import statistics
from fileopencsv import *
from GeoMagneticData import *

'''
'''

#finds the anomalies by column
def anomalies_col(in_list):
    #init the lower bound (mean - stdev) and upper bound (mean + stdev)
    lower_bound = statistics.mean(in_list) - statistics.stdev(in_list)
    upper_bound = statistics.mean(in_list) + statistics.stdev(in_list)
    anomaly_list = []
    #iterate through the data and if it does not fit in our IQR, we append the day, and hour it occurred.
    for i in range(len(in_list)):
        temp = []
        if in_list[i] < lower_bound or in_list[i] > upper_bound:
            temp.append(day(i))
            temp.append(hour(i))
            anomaly_list.append(temp)
    return anomaly_list

#finds the anomalies by row
def anomalies_row(in_list, n):
    #init the lower bound (mean - stdev) and upper bound (mean + stdev)
    lower_bound = statistics.mean(in_list) - n * statistics.stdev(in_list)
    upper_bound = statistics.mean(in_list) + n * statistics.stdev(in_list)
    anomaly_list = []
    #iterate through the data and if it does not fit in our IQR, append it to the anomaly list, else we append 0
    for i in range(len(in_list)):
        if in_list[i] < lower_bound or in_list[i] > upper_bound:
            anomaly_list.append(in_list[i])
        else:
            anomaly_list.append(0)
    return anomaly_list

def anomalies_row_prob(in_list, n):
    #init the lower bound (mean - stdev) and upper bound (mean + stdev)
    lower_bound = statistics.mean(in_list) - n * statistics.stdev(in_list)
    upper_bound = statistics.mean(in_list) + n * statistics.stdev(in_list)
    anomaly_list = []
    #iterate through the data and if it does not fit in our IQR, append it to the anomaly list, else we append 0
    for i in range(len(in_list)):
        if in_list[i] < lower_bound or in_list[i] > upper_bound:
            anomaly_list.append( float('%.2f' % (((in_list[i] - upper_bound)/in_list[i]) * 100))) 
        else:
            anomaly_list.append(0)
    return anomaly_list

#used to find the geographical data corresponding to the index provided
def findGeoDataIndex(theList, theIndex):
    for item in theList:
        if item.getDataIndex() == theIndex:
            return item

#appends the day and hour to the anomalies by row, returning the anomalies as a list by row.
def make_row_anomalies(filename, n):
    input_file_list = get_row_csv(filename)
    temp_list = []
    for i in range (len(input_file_list)):
        anom = anomalies_row(input_file_list[i], n)
        anom.insert(0, str(day(i)) + "-" + str(hour(i)) )
        temp_list.append(anom)
    return temp_list

def make_row_anom_prob(filename, n):
    input_file_list = get_row_csv(filename)
    temp_list = []
    for i in range (len(input_file_list)):
        anom = anomalies_row_prob(input_file_list[i], n)
        anom.insert(0, str(day(i)) + "-" + str(hour(i)) )
        temp_list.append(anom)
    return temp_list
