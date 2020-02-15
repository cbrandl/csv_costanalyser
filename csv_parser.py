#!/usr/bin/env python
import glob, time, os, csv, codecs, datetime, locale
import pandas as pd
import plotly.graph_objects as go
import helper
import csv_mapping

#from timestring import Date

def transformBankData(df, account_info):
    # rename columns of dataframe to mapping
    for column in df.columns:
        # print (column)
        for key, value in account_info["df_origin_mapping"].items():
            if value == column:
                # print(value)
                # rename columns
                df.rename(columns={column: csv_mapping.mappingHeaders[key]}, inplace=True)
                print(csv_mapping.mappingHeaders[key])
    diff = set(csv_mapping.mappingHeaders) - set(account_info["df_origin_mapping"])
    # print("Diff: ")
    # print(diff)
    for pos in diff:
        # print(mappingHeaders[pos])
        if (csv_mapping.mappingHeaders[pos] == "account_name"):
            df[csv_mapping.mappingHeaders[pos]] = account_info["account_name"]
        else:
            df[csv_mapping.mappingHeaders[pos]] = 0
    # print("Imported Dataframe Columns: ")
    # print(df.columns)
    # print("Mapping: ")
    # print(mappingHeaders.values())
    df = df[csv_mapping.mappingHeaders.values()]
    # transform specifc columns
    # clean amount column to english currency format 1000.00 instead of 1.000,00
    for i, row in df.iterrows():
        df.at[i, 'amount'] = str(df.at[i, 'amount']).replace(',', '.')
        if str(df.at[i, 'amount']).count('.') > 1:
            df.at[i, 'amount'] = str(df.at[i, 'amount']).replace(".", "", 1)
    df['amount'] = df['amount'].astype(float)

    # clean original_amount column to english currency format 1000.00 instead of 1.000,00
    for i, row in df.iterrows():
        df.at[i, 'original_amount'] = str(df.at[i, 'original_amount']).replace(',', '.')
        if str(df.at[i, 'original_amount']).count('.') > 1:
            df.at[i, 'original_amount'] = str(df.at[i, 'original_amount']).replace(".", "", 1)
    df['original_amount'] = df['original_amount'].astype(float)

    return df

def start():
    check_folders = [
        "./csv_export",
    ]
    extension = "csv"

    files = []
    for folder in check_folders:
        for file in helper.listDir(folder, extension.lower()):
            files.append(file)
        for file in helper.listDir(folder, extension.upper()):
            files.append(file)

    print("Number of files {}".format(len(files)))
    # for fileList in files:
    df_main = pd.DataFrame(columns=csv_mapping.mappingHeaders.values())

    for filenamePath in files:
        print(filenamePath)
        account_info = helper.getAccountInfo(filenamePath)
        df = pd.read_csv(filenamePath, encoding='ISO-8859-1', delimiter=account_info["delimiter"],
                         decimal=account_info["decimal"])
        df = transformBankData(df, account_info)
        # transformCom_giro_df.head(3)
        # print(df)
        df_main = df_main.append(df, ignore_index=True)

    return df_main


transformCom_giro_df = start()
transformCom_giro_df.head(3)
#transformCom_giro_df.info()
#transformCom_giro_df.groupby(['category'])['amount'].sum()
#transformCom_giro_df['account_name'].value_counts()







