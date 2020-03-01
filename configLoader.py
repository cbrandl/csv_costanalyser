import configs.bankList as banklist
import dataMapper as dataMapper
#import vocabulary

class ConfigLoader:
    def __init__(self, data, iban):
        self.__data = data
        self.__iban = iban
        self.__headings = []
        #self.__defaultStruct = vocabulary.Vocabulary().getDictionary()

    def getStructuredData(self):
        self.setHeadings()
        mapper = dataMapper.dataMapper(self.__data)
        mappedData = mapper.map()

        bankList = banklist.BankList(self.__iban)
        bankConfig = bankList.getBankConfig()

        accountNumberIdentifier = bankConfig.getAccountNumberID(self.__headings).lower()
        transactioDateIdentifier = bankConfig.getTransactionDateID(self.__headings).lower()
        amountIdentifier = bankConfig.getAmountID(self.__headings).lower()
        currencyIdentifier = bankConfig.getCurrencyID(self.__headings).lower()

        finalDataSet = []
        for transaction in mappedData:
            item = {
                'account_number': transaction[accountNumberIdentifier],
                'transaction_date': transaction[transactioDateIdentifier],
                'amount': transaction[amountIdentifier],
                'category': transaction[currencyIdentifier]
            }
            finalDataSet.append(item)

        return finalDataSet

    def setHeadings(self):
        self.__headings = self.__data[0]