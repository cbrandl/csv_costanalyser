mappingHeaders = {}
mappingHeaders["1"] = "account_number"
mappingHeaders["2"] = "account_name"
mappingHeaders["3"] = "transaction_date"
mappingHeaders["4"] = "value_date"
mappingHeaders["5"] = "transaction_type"
mappingHeaders["6"] = "booking_text"
mappingHeaders["7"] = "amount"
mappingHeaders["8"] = "currency"
mappingHeaders["9"] = "original_amount"
mappingHeaders["10"] = "original_currency"
mappingHeaders["11"] = "company_name"
mappingHeaders["12"] = "account_of_initiator"
mappingHeaders["13"] = "bank_code_of_account_of_initiator"
mappingHeaders["14"] = "IBAN_of_account_of_initiator"
mappingHeaders["15"] = "category"
mappingHeaders["16"] = "account_id"
mappingHeaders["17"] = "created_at"
mappingHeaders["18"] = "updated_at"
mappingHeaders["19"] = "validated"
mappingHeaders["20"] = "payee_id"
mappingHeaders["21"] = "payee_name"
mappingHeaders["22"] = "inbound"
mappingHeaders["23"] = "outbound"
mappingHeaders["24"] = "billing_date"
mappingHeaders["25"] = "manipulationfee_in_eur"
mappingHeaders["26"] = "used_exchange_rate"
mappingHeaders["27"] = "statement_number"
mappingHeaders["28"] = "transaction_timestamp"
mappingHeaders["29"] = "revenue_text"


# Mapping Commerzabank Creditcard with Main Mapping dictionary "mappingHeaders"
mappingHeadersComrzCC_new = {}
mappingHeadersComrzCC_new["3"] = "Transaction date"
mappingHeadersComrzCC_new["4"] = 'Receipt'
mappingHeadersComrzCC_new["11"] = 'Company'
mappingHeadersComrzCC_new["7"] = 'Amount'
mappingHeadersComrzCC_new["8"] = 'Currency'
mappingHeadersComrzCC_new["9"] = 'Original Amount'
mappingHeadersComrzCC_new["10"] = 'Original Currency'
mappingHeadersComrzCC_new["1"] = 'Debited Credit Card'
mappingHeadersComrzCC_new["15"] = 'Category'

# Mapping Commerzabank Creditcard with Main Mapping dictionary "mappingHeaders"
mappingHeadersComrzCC_new_de = {}
mappingHeadersComrzCC_new_de["3"] = "Buchungstag"
mappingHeadersComrzCC_new_de["4"] = 'Beleg'
mappingHeadersComrzCC_new_de["11"] = 'Unternehmen'
mappingHeadersComrzCC_new_de["7"] = 'Betrag'
mappingHeadersComrzCC_new_de["8"] = 'WÃ¤hrung'
mappingHeadersComrzCC_new_de["9"] = 'Betrag Ursprung'
mappingHeadersComrzCC_new_de["10"] = 'WÃ¤hrung Ursprung'
mappingHeadersComrzCC_new_de["1"] = 'Belastete Kreditkarte'
mappingHeadersComrzCC_new_de["15"] = 'Kategorie'

# Mapping Commerzabank Creditcard with Main Mapping dictionary "mappingHeaders"
mappingHeadersComrzCC_old = {}
mappingHeadersComrzCC_old["3"] = "Buchungstag"
mappingHeadersComrzCC_old["4"] = 'Beleg'
mappingHeadersComrzCC_old["11"] = 'Unternehmen'
mappingHeadersComrzCC_old["7"] = 'Betrag'
mappingHeadersComrzCC_old["8"] = 'WÃ¤hrung'
mappingHeadersComrzCC_old["9"] = 'Betrag Ursprung'
mappingHeadersComrzCC_old["10"] = 'WÃ¤hrung Ursprung'
mappingHeadersComrzCC_old["1"] = 'Belastete Kreditkarte'

# Mapping Commerzabank Giro OLD with Main Mapping dictionary "mappingHeaders"
mappingHeadersComrzGiro_old = {}
mappingHeadersComrzGiro_old["3"] = "Buchungstag"
mappingHeadersComrzGiro_old["4"] = 'Wertstellung'
mappingHeadersComrzGiro_old["5"] = 'Umsatzart'
mappingHeadersComrzGiro_old["6"] = 'Buchungstext'
mappingHeadersComrzGiro_old["7"] = 'Betrag'
mappingHeadersComrzGiro_old["8"] = 'WÃ¤hrung'
mappingHeadersComrzGiro_old["12"] = 'Auftraggeberkonto'
mappingHeadersComrzGiro_old["13"] = 'Bankleitzahl Auftraggeberkonto'
mappingHeadersComrzGiro_old["14"] = 'IBAN Auftraggeberkonto'
mappingHeadersComrzGiro_old["15"] = 'Kategorie'

# Mapping Commerzabank Giro OLD with Main Mapping dictionary "mappingHeaders"
mappingHeadersComrzGiro_old_de = {}
mappingHeadersComrzGiro_old_de["3"] = "Buchungstag"
mappingHeadersComrzGiro_old_de["4"] = 'Wertstellung'
mappingHeadersComrzGiro_old_de["5"] = 'Umsatzart'
mappingHeadersComrzGiro_old_de["6"] = 'Buchungstext'
mappingHeadersComrzGiro_old_de["7"] = 'Betrag'
mappingHeadersComrzGiro_old_de["8"] = 'WÃ¤hrung'
mappingHeadersComrzGiro_old_de["12"] = 'Auftraggeberkonto'
mappingHeadersComrzGiro_old_de["13"] = 'Bankleitzahl Auftraggeberkonto'
mappingHeadersComrzGiro_old_de["14"] = 'IBAN Auftraggeberkonto'

# Mapping Commerzabank Giro NEW with Main Mapping dictionary "mappingHeaders"
mappingHeadersComrzGiro_new = {}
mappingHeadersComrzGiro_new["3"] = "Transaction date"
mappingHeadersComrzGiro_new["4"] = 'Value date'
mappingHeadersComrzGiro_new["5"] = 'Transaction type'
mappingHeadersComrzGiro_new["6"] = 'Booking text'
mappingHeadersComrzGiro_new["7"] = 'Amount'
mappingHeadersComrzGiro_new["8"] = 'Currency'
mappingHeadersComrzGiro_new["12"] = 'Account of initiator'
mappingHeadersComrzGiro_new["13"] = 'Bank code of account of initiator'
mappingHeadersComrzGiro_new["14"] = 'IBAN of account of initiator'
mappingHeadersComrzGiro_new["15"] = 'Category'

# Mapping Volksbank CC with Main Mapping dictionary "mappingHeaders"
mappingHeadersvbkCC = {}
mappingHeadersvbkCC["3"] = "Buchungsdatum"
mappingHeadersvbkCC["4"] = 'Transaktionsdatum'
mappingHeadersvbkCC["24"] = 'Abrechnungsdatum'
mappingHeadersvbkCC["6"] = 'Rechnungstext'
mappingHeadersvbkCC["1"] = 'Kartennummer'
mappingHeadersvbkCC["8"] = 'WÃ¤hrung'
mappingHeadersvbkCC["9"] = 'Betrag in FremdwÃ¤hrung'
mappingHeadersvbkCC["9"] = 'WÃ¤hrung.1'
mappingHeadersvbkCC["25"] = 'Manipulationsentgelt in EUR'
mappingHeadersvbkCC["7"] = 'WÃ¤hrung.2'
mappingHeadersvbkCC["8"] = 'Betrag'
mappingHeadersvbkCC["26"] = 'Verwendeter Umrechnungskurs'

# Mapping Volksbank Wohnbauförderung with Main Mapping dictionary "mappingHeaders"
mappingHeadersvbk = {}
mappingHeadersvbk["1"] = "IBAN"
mappingHeadersvbk["27"] = 'Auszugsnummer'
mappingHeadersvbk["3"] = 'Buchungsdatum'
mappingHeadersvbk["4"] = 'Valutadatum'
mappingHeadersvbk["28"] = 'Umsatzzeit'
mappingHeadersvbk["20"] = 'Zahlungsreferenz'
mappingHeadersvbk["8"] = 'Waehrung'
mappingHeadersvbk["7"] = 'Betrag'
mappingHeadersvbk["6"] = 'Buchungstext'
mappingHeadersvbk["29"] = 'Umsatztext'



#New Categories
categoryDict = {}
categoryDict["banking"] = ["Bank Fees & Service Fees", "Loan repayment", "BankgebÃ¼hren", "Bank Fees", "Zinsen / Dividenden"]
categoryDict["booksMusicGames"] = ["Books, Music, Games, etc.", "BÃ¼cher / Musik / DVDs"]
categoryDict["officeSupplies"] = ["Office supplies", "BÃ¼romaterial"]
categoryDict["creditcard"] = ["Credit Card Payment", "Kreditkartenabrechnung"]
categoryDict["hobbys"] = ["Hobbies","Hobbys"]
categoryDict["income"] = ["Income", "Einnahmen", "Lohn / Gehalt", "Paycheck", "Einnahmen aus VerkÃ¤ufen", "Interest income", "Proceeds from sale"]
categoryDict["cinema"] = ["Kino / Kunst / Kultur","Movies, Theatres, Concerts etc."]
categoryDict["electronics"] = ["Electronics & Computers","Elektronik / Computer"]
categoryDict["groceries"] = ["Groceries","Lebensmittel / GetrÃ¤nke"]
categoryDict["restaurants"] = ["Restaurants, Cafes, Bars", "Restaurants & Cafes","Restaurants / Cafes / Bars"]
categoryDict["sports"] = ["Sport / Fitness", "Cycling", "Gym & Sports"]
categoryDict["travel"] = ["Public Transportation","Reisekosten (Flug/Bahn/Schiff)", "Ãffentliche Verkehrsmittel"]
categoryDict["subscriptions"] = ["Subscriptions","Abonnements","Subscriptions & Media"]
categoryDict["taxRefunds"] = ["Tax refund", "SteuerrÃ¼ckerstattungen"]
categoryDict["employeeExpenses"] = ["Employment related expenses", "Dienstreise / Spesen"]
categoryDict["phone"] = ["Home Phone and Internet","Telefon / Internet / Fernsehen"]
categoryDict["jewelry"] = ["Jewelry","Uhren / Schmuck"]
categoryDict["vacation"] = ["Vacation", "Planes, Cars & Transport on Vacation","Urlaubskasse","Holiday fund"]
categoryDict["hotels"] = ["Hotels & Accomodation"]
categoryDict["presents"] = ["Flowers, Candles & Minor Items"]
categoryDict["services"] = ["Shopping & Services"]
categoryDict["living"] = ["Living", "Geldtasche", "Lebenshaltung"]
categoryDict["clothing"] = ["Clothing & Accessories"]
categoryDict["uncategorized"] = ["Uncategorized Expenses","Unkategorisierte Ausgaben", 0]