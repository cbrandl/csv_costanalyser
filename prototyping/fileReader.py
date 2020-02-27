import csv

class FileReader:
    def __init__(self, filename):
        self.__sampleBytes = 32
        self.__filename = filename

    def readCsv(self):
        data = list(csv.reader(open(self.__filename), delimiter=';'))
        return data

    def hasHeader(self):
        sniffer = csv.Sniffer()
        return sniffer.has_header(open(self.__filename).read(self.__sampleBytes))
