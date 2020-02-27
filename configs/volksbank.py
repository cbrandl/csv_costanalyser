class Volksbank:
    def __init__(self):
        self.__iban = ["iban", "account number"]
        self.__date = ["transaction_date", "Transaction date", "Buchungstag", "Buchungsdatum"]
        self.__amount = ["Amount", "amount", "betrag", "Betrag"]
        self.__text = ["category", "Kategorie", "Category", "buchungstext", "Booking text"]

    def getIbanIdentifier(self, headings):
        for heading in headings:
            if heading in self.__iban:
                return heading
        return None




