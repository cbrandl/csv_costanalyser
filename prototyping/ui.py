import fileReader
import cashbook as cb

reader = fileReader.FileReader()
data = reader.readCsv('bank_account.csv')
cashbook = cb.Cashbook(data)
inflow = cashbook.inflow_sum()
outflow = cashbook.outflow_sum()
balance = cashbook.getBalance(inflow, outflow)

print(cashbook.getCategories())
print(balance)

