import csv

class FileReader:
    def __init__(self):
        self.__data = []

    def readCsv(self, filename):
        data = list(csv.reader(open(filename), delimiter=';'))
        return data




