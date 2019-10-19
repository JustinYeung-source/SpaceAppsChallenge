import statistics
from fileopencsv import *
'''
iterate through the list.
if the element is within the range, then it's accepted and we 
    increment the accepted num
else the element is out of range
    increment the rejected num
'''

def anomalies_col(in_list):
    lower_bound = statistics.fmean(in_list) - statistics.stdev(in_list)
    upper_bound = statistics.fmean(in_list) + statistics.stdev(in_list)
    anomaly_list = []
    for i in range(len(in_list)):
        temp = []
        if in_list[i] < lower_bound or in_list[i] > upper_bound:
            temp.append(day(i))
            temp.append(hour(i))
            anomaly_list.append(temp)
    return anomaly_list

def anomalies_row(in_list):
    lower_bound = statistics.fmean(in_list) - statistics.stdev(in_list)
    upper_bound = statistics.fmean(in_list) + statistics.stdev(in_list)
    anomaly_list = []
    for i in range(len(in_list)):
        temp = []
        if in_list[i] < lower_bound or in_list[i] > upper_bound:
            temp.append(i)
            temp.append(in_list[i])
            anomaly_list.append(temp)
    return anomaly_list

def main():
    input_file_list = getrow_csv("dataset1.csv")
    anom = anomalies_row(input_file_list[0])
    #print(input_file_list[0])
    print(anom)
main()