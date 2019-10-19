from fileopencsv import *
'''
This is our main file
'''

def main():
    input_file_list = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    input_file_list = file_interpret_csv("dataset1.csv")
    print(input_file_list)

main()