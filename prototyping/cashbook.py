import fileReader
import numpy

class Cashbook:
    def __init__(self, data):
        self.__data = data
        self.__categories = self.extract_categories()

    def extract_categories(self):
        allCategories = []
        for transaction in self.__data:
            allCategories.append(transaction[3])

        return numpy.unique(allCategories)

    def getCategories(self):
        return self.__categories

    def outflow_sum(self):
        outflow = 0
        for transaction in self.__data:
            if float(transaction[1]) < 0:
                outflow += float(transaction[1])
        return outflow

    def inflow_sum(self):
        inflow = 0
        for transaction in self.__data:
            if float(transaction[1]) >= 0:
                inflow += float(transaction[1])
        return inflow

    def getBalance(self, inflow, outflow):
        sum = inflow + outflow
        return "Balance: {:> 8.2f}".format(sum)












