import prototyping.fileReader as fileReader
import prototyping.cashbook as cb
import prototyping.dataMapper as dataMapper

filename = '../csv_export/umsaetze-girokonto_AT024239000000123456.csv'

reader = fileReader.FileReader(filename)
data = reader.readCsv()
hasHeader = reader.hasHeader()
dataMapper = dataMapper.dataMapper(data)
if hasHeader:
    mappedData = dataMapper.map()
    cashbook = cb.Cashbook(mappedData)
    inflow = cashbook.inflow_sum()
    outflow = cashbook.outflow_sum()
    balance = cashbook.getBalance(inflow, outflow)

    print(cashbook.getCategories())
    print(balance)

