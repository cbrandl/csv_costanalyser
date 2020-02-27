import configs.hypo as hypo
import configs.volksbank as volksbank

class Bank:
    def __init__(self, filename):
        self.__filename = filename

    def bankName(self, iban):
        if iban[4:8] == 5700:
            return hypo()
        elif iban[0:8] == 4239:
            return volksbank()
        else:
            return None
