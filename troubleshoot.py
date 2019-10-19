import statistics, fileopencsv
#attach the dataset, make it numeric
#find the mean of the list
#find median of the list
#find the fivenum summary
#confidence interval of the list
#standard deviation of the list

#create a rejected list with the range of the number
#of sites within it
'''
iterate through the list.
if the element is within the range, then it's accepted and we 
    increment the accepted num
else the element is out of range
    increment the rejected num
'''

def anomalies(site_list):
    lower_bound = statistics.fmean(site_list) - statistics.stdev(site_list)
    upper_bound = statistics.fmean(site_list) + statistics.stdev(site_list)
    anomaly_list = []
    for i in range(len(site_list)):
        temp = []
        print(site_list[i], lower_bound, upper_bound, statistics.fmean(site_list), statistics.stdev(site_list))
        if site_list[i] < lower_bound or site_list[i] > upper_bound:
            temp.append(fileopencsv.day(i))
            temp.append(fileopencsv.hour(i))
            anomaly_list.append(temp)
    return anomaly_list

def main():
    input_file_list = fileopencsv.fileopen_csv("dataset1.csv")
    anom = anomalies(input_file_list[0])
    #print(input_file_list[0])
    print(anom)
main()