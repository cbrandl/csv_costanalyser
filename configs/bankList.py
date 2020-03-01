import configs.hypo as hypo
import configs.volksbank as volksbank

class BankList:
    def __init__(self, iban):
        self.__iban = iban

    def getBankConfig(self):
        bankClass = None

        if self.__iban[4:8] == '5700':
            bankClass = hypo.Hypo()
        elif self.__iban[4:8] == '4239':
            bankClass = volksbank.Volksbank()

        return bankClass
