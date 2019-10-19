import Fileopencsv, Compute_data, statistics
'''
This is our main file
'''

def main():
    data_BY_COLUMN = Fileopencsv.get_column_csv("dataset1.csv")

    MEAN_data_C = Compute_data.compute_mean(data_BY_COLUMN)
    STDEV_data_C = Compute_data.compute_standard_deviation(data_BY_COLUMN)

    data_wout_outliers_C = Compute_data.remove_outliers(data_BY_COLUMN, MEAN_data_C)
    data_just_outliers_C = Compute_data.just_outliers(data_BY_COLUMN, MEAN_data_C)




    data_BY_ROW = Fileopencsv.get_row_csv("dataset1.csv")

    MEAN_data_R = Compute_data.compute_mean(data_BY_ROW)
    STDEV_data_R = Compute_data.compute_standard_deviation(data_BY_ROW)

    data_wout_outliers_R = Compute_data.remove_outliers(data_BY_ROW, MEAN_data_R)
    data_just_outliers_R = Compute_data.just_outliers(data_BY_ROW, MEAN_data_R)
    print(data_just_outliers_R)





    
main()