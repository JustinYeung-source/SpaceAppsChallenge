from GeoMagneticData import *
import DataHandler, Compute_data, fileopencsv, troubleshoot

def main():
    data_BY_COLUMN = fileopencsv.get_column_csv("dataset1.csv")
    data_BY_ROW = fileopencsv.get_row_csv("dataset1.csv")

    MEAN_data_C = Compute_data.compute_mean(data_BY_COLUMN) #MEAN data organized by Columns
    MEAN_data_R = Compute_data.compute_mean(data_BY_ROW) #MEAN data organized by Rows

    STDEV_data_R = Compute_data.compute_standard_deviation(data_BY_ROW) #Standard Deviation data organized by Rows
    STDEV_data_C = Compute_data.compute_standard_deviation(data_BY_COLUMN) #Standard Deviation data organized by Columns

    ''' 
    OUTLIERS/ANOMALIES CALCULATED USING:
    IF YOUR VALUE >= MEAN
    '''
    data_wout_outliers_R = Compute_data.remove_outliers(data_BY_ROW, MEAN_data_R) #ORGANIZED BY ROWS DENOTED BY (R)
    data_just_outliers_R = Compute_data.just_outliers(data_BY_ROW, MEAN_data_R)   #ORGANIZED BY ROWS DENOTED BY (R)

    data_wout_outliers_C = Compute_data.remove_outliers(data_BY_COLUMN, MEAN_data_C) #ORGANIZED BY COLUMNS DENOTED BY (C)
    data_just_outliers_C = Compute_data.just_outliers(data_BY_COLUMN, MEAN_data_C)   #ORGANIZED BY COLUMNS DENOTED BY (C)

    header_tags = fileopencsv.headers("dataset1.csv") #THIS IS JUST LOCATION NAME: + (LONGITUDE LATITUDE)
    '''
    MAIN_ANOMALIES IS CALCUATED USING IQR: 
    UPPERBOUND = (MEAN + STDEV) 
    LOWERBOUND = (MEAN - STDEV)
    '''
    main_anomalies = troubleshoot.make_row_anomalies("dataset1.csv", 2.5)
    fileopencsv.export_csv_file(header_tags,main_anomalies,"test.csv") #THIS JUST EXPORTS TO A CSV FILE USING "," AS DELIMITERS
main()