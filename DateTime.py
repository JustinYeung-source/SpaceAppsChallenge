
class DateTime:
    def __init__(self, day, hour, index):
        self._day = day
        self._hour = hour
        self._index = index

    def __repr__(self):
        return "DD/HH: " + self._day + "/" + self._hour

    def getDay(self):
        return self._day

    def getHour(self):
        return self._hour

    def getIndex(self):
        return self._index