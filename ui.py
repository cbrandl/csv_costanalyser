import fileReader as fileReader
import prototyping.cashbook as cb
import configLoader

filename = './csv_export/umsaetze-girokonto_AT024239000000123456.csv'

reader = fileReader.FileReader(filename)
data = reader.readCsv()
hasHeader = reader.hasHeader()
if hasHeader:
    configLoader = configLoader.ConfigLoader(data, 'AT024239000000123456')
    mappedData = configLoader.getStructuredData()
    cashbook = cb.Cashbook(mappedData)
    inflow = cashbook.inflow_sum()
    outflow = cashbook.outflow_sum()
    balance = cashbook.getBalance(inflow, outflow)

    #print(cashbook.getCategories())
    print(balance)

