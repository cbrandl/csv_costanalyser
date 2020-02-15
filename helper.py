import glob
import csv_mapping

def listDir(subfolder, ext):
    return glob.glob(subfolder + "/*." + ext)


def getDelimiter(filenamePath):
    # open file
    # file = open(filenamePath, 'r').read()
    file = open(filenamePath, 'r', encoding="ISO-8859-1").read()
    # search strings
    delimeterComma = ","
    delimeterSemicol = ";"
    # begin search
    countComma = file.count(delimeterComma)
    countSemicol = file.count(delimeterSemicol)
    print(countComma)
    print(countSemicol)

    if countComma > countSemicol:
        return delimeterComma
    else:
        return delimeterSemicol


def getAccountInfo(filenamePath):
    commerzbank_account_number = "666727300"
    commerzbank_creditcard_chris = "4018499001961263"
    commerzbank_creditcard_anett = "4018499001964689"
    volkdsbank_creditcard_anett = "MeineTransaktionen"
    vbk_savings_wohnbaufoerderung = "AT944239000055453333"
    vbk_giro = "AT154239000100094058"
    vbk_credit = "AT444239000052019560"
    vbk_lifebank = "AT584239000000524433"
    vbk_giro_old_chris = "AT024239000000123456"

    accountName = ""
    delimiter = ";"
    df_origin_mapping = ""
    decimal = "."
    if commerzbank_creditcard_anett in filenamePath:
        accountName = "Commerzbank-Kreditkarte-Anett"
        delimiter = ","
        df_origin_mapping = csv_mapping.mappingHeadersComrzCC_new
        if "-de-" in filenamePath:
            delimiter = ";"
            df_origin_mapping = csv_mapping.mappingHeadersComrzCC_new_de
        elif "old" in filenamePath:
            delimiter = ";"
            df_origin_mapping = csv_mapping.mappingHeadersComrzCC_old
    elif commerzbank_creditcard_chris in filenamePath:
        accountName = "Commerzbank-Kreditkarte-Chris"
        delimiter = ","
        df_origin_mapping = csv_mapping.mappingHeadersComrzCC_new
        if "-de-" in filenamePath:
            delimiter = ";"
            df_origin_mapping = csv_mapping.mappingHeadersComrzCC_new_de
        elif "old" in filenamePath:
            delimiter = ";"
            df_origin_mapping = csv_mapping.mappingHeadersComrzCC_old
    elif commerzbank_account_number in filenamePath:
        accountName = "Commerzbank-Giro"
        delimiter = ","
        df_origin_mapping = csv_mapping.mappingHeadersComrzGiro_new
        if "-de-" in filenamePath:
            delimiter = ";"
            df_origin_mapping = csv_mapping.mappingHeadersComrzGiro_old_de
        elif "old" in filenamePath:
            accountName = "Commerzbank-Giro-Old"
            delimiter = ";"
            df_origin_mapping = csv_mapping.mappingHeadersComrzGiro_old
    elif volkdsbank_creditcard_anett in filenamePath:
        accountName = "Volksbank-Kreditkarte-Anett"
        df_origin_mapping = csv_mapping.mappingHeadersvbkCC
        decimal = ","
    elif vbk_savings_wohnbaufoerderung in filenamePath:
        accountName = "Volksbank-Wohnbaufoerderung"
        df_origin_mapping = csv_mapping.mappingHeadersvbk
        decimal = ","
    elif vbk_giro in filenamePath:
        accountName = "Volksbank-Giro"
        df_origin_mapping = csv_mapping.mappingHeadersvbk
        decimal = ","
    elif vbk_credit in filenamePath:
        accountName = "Volksbank-Kredit"
        df_origin_mapping = csv_mapping.mappingHeadersvbk
        decimal = ","
    elif vbk_lifebank in filenamePath:
        accountName = "Volksbank-Lifebank"
        df_origin_mapping = csv_mapping.mappingHeadersvbk
        decimal = ","
    elif vbk_giro_old_chris in filenamePath:
        accountName = "Volksbank-Giro-Chris-archived"
        df_origin_mapping = csv_mapping.mappingHeadersvbk
        decimal = ","

    account_info = {}
    account_info["account_name"] = accountName
    account_info["delimiter"] = getDelimiter(filenamePath)
    account_info["decimal"] = decimal
    account_info["df_origin_mapping"] = df_origin_mapping

    return account_info