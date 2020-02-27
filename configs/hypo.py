class Hypo:
    def __init__(self):
        self.__account_number = ["iban", "IBAN", "account number"]
        self.__transaction_date = ["Transaction date", "Buchungstag", "Buchungsdatum"]
        self.__amount = ["Amount", "betrag", "Betrag"]
        self.__currency = ["WÃ¤hrung", "Waehrung"]
        self.__category = ["Kategorie", "Category", "buchungstext", "Booking text"]

    def getAccountNumberID(self, headings):
        for heading in headings:
            if heading in self.__account_number:
                return heading
        return None

    def getTransactionDateID(self, headings):
        for heading in headings:
            if heading in self.__transaction_date:
                return heading
        return None

    def getAmountID(self, headings):
        for heading in headings:
            if heading in self.__amount:
                return heading
        return None

    def getCurrencyID(self, headings):
        for heading in headings:
            if heading in self.__currency:
                return heading
        return None

    def getCategoryID(self, headings):
        for heading in headings:
            if heading in self.__category:
                return heading
        return None