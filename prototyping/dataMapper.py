class dataMapper:
    def __init__(self, data):
        self.__data = data
        self.__structure = self.getDataStructure()

    def getDataStructure(self):
        headings = self.__data[0]
        structure = {}
        for key in headings:
            structure[key.lower()] = ''
        return structure

    def map(self):
        dataSet = []
        for dataRecord in self.__data[1:]:
            item = {}
            for index, key in enumerate(self.__structure):
                item[key] = dataRecord[index]
            dataSet.append(item)
        return dataSet
