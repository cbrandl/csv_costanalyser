import numpy

class Cashbook:
    def __init__(self, data):
        self.__data = data
        self.__categories = self.extract_categories()

    def extract_categories(self):
        allCategories = []
        for transaction in self.__data:
            allCategories.append(transaction['buchungstext'])

        return numpy.unique(allCategories)

    def getCategories(self):
        return self.__categories

    def outflow_sum(self):
        outflow = 0
        for transaction in self.__data:
            # fix german float separation
            amount = transaction['betrag'].replace(',', '.')
            if float(amount) < 0:
                outflow += float(amount)
        return outflow

    def inflow_sum(self):
        inflow = 0
        for transaction in self.__data:
            #fix german float separation
            amount = transaction['betrag'].replace(',', '.')
            if float(amount) >= 0:
                inflow += float(amount)
        return inflow

    def getBalance(self, inflow, outflow):
        sum = inflow + outflow
        return "Balance: {:> 8.2f}".format(sum)
