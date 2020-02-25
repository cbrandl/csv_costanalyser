import prototyping.fileReader as fileReader
import prototyping.cashbook as cb

reader = fileReader.FileReader()
data = reader.readCsv('../csv_export/umsaetze-girokonto_AT024239000000123456.csv')
cashbook = cb.Cashbook(data)
inflow = cashbook.inflow_sum()
outflow = cashbook.outflow_sum()
balance = cashbook.getBalance(inflow, outflow)

print(cashbook.getCategories())
print(balance)

