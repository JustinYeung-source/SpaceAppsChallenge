#This .py is purely for utility
import csv

def getData(fileName):
    #with open(fileName) as file:
    data = csv.reader(open(fileName, "r"), delimiter= ",")
    specificationRow = next(data)
    dictData = {}
    numRow = 0
    numCol = 0
    for row in data:
        numRow += 1    
        for info in row:
            numCol += 1
            if info.find('-') != -1:
                dictData[info] = []
    
getData('dataset2_full.csv')
