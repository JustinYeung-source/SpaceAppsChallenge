import csv

class GeoMagneticData():

    def __init__(self, location, longitude, latitude, dataIndex):
        self._location = location
        self._longtitude = longitude
        self._latitude = latitude
        # Each index is a row I.E it is the DD/HH in the file
        self._data = []
        # IMPORTANT: this index relates to which column this classes data is
        self._dataIndex = dataIndex

    def __repr__(self):
        return self._location + " (" + self._longtitude + " " + self._latitude + "), "

    def add(self, data):
        self._data.append(data)

    def getLocation(self):
        return self._location

    def getData(self):
        return self._data

    def getLongitude(self):
        return self._longtitude

    def getLatitude(self):
        return self._latitude

    def getDataIndex(self):
        return self._dataIndex

    def __str__(self):
        return self._location + " (" + self._longtitude + " " + self._latitude + "), "