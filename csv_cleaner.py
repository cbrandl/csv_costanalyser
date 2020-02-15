#!/usr/bin/env python
import glob, time, os, csv, codecs, datetime, locale
import pandas as pd
import plotly.graph_objects as go
import helper
import csv_mapping
import csv_parser
import xlsxwriter


show_col = ["account_number", "account_name","transaction_date", "category", "amount", "revenue_text"]
filer = ["AT024239000000123456"]

transformCom_giro_df = csv_parser.start()

#Clear Duplicates
transformCom_giro_df = transformCom_giro_df.drop_duplicates()
transformCom_giro_df['account_name'].value_counts()

#groceries
transformCom_giro_df.loc[transformCom_giro_df['revenue_text'].str.contains('BILLA', na=False), "category"] = csv_mapping.categoryDict["groceries"][0]
transformCom_giro_df.loc[transformCom_giro_df['revenue_text'].str.contains('Spar', na=False), "category"] = csv_mapping.categoryDict["groceries"][0]
transformCom_giro_df.loc[transformCom_giro_df['revenue_text'].str.contains('MPREIS', na=False), "category"] = csv_mapping.categoryDict["groceries"][0]
transformCom_giro_df.loc[transformCom_giro_df['revenue_text'].str.contains('REWE', na=False), "category"] = csv_mapping.categoryDict["groceries"][0]
transformCom_giro_df.loc[transformCom_giro_df['revenue_text'].str.contains('BAGUETTE', na=False), "category"] = csv_mapping.categoryDict["groceries"][0]
transformCom_giro_df.loc[transformCom_giro_df['revenue_text'].str.contains('DM-DROGER', na=False), "category"] = csv_mapping.categoryDict["groceries"][0]
transformCom_giro_df.loc[transformCom_giro_df['revenue_text'].str.contains('ROSSMANN', na=False), "category"] = csv_mapping.categoryDict["groceries"][0]
transformCom_giro_df.loc[transformCom_giro_df['revenue_text'].str.contains('INTERSPAR', na=False), "category"] = csv_mapping.categoryDict["groceries"][0]
transformCom_giro_df.loc[transformCom_giro_df['revenue_text'].str.contains('JUFFINGER', na=False), "category"] = csv_mapping.categoryDict["groceries"][0]
transformCom_giro_df.loc[transformCom_giro_df['revenue_text'].str.contains('HOFER DANKT', na=False), "category"] = csv_mapping.categoryDict["groceries"][0]

#Geldtasche
transformCom_giro_df.loc[transformCom_giro_df['revenue_text'].str.contains('Bankomat', na=False), "category"] = csv_mapping.categoryDict["living"][1]
transformCom_giro_df.loc[transformCom_giro_df['revenue_text'].str.contains('BANKOMAT', na=False), "category"] = csv_mapping.categoryDict["living"][1]

#Company Name
#transformCom_giro_df.loc[transformCom_giro_df['company_name'].str.contains('Amazon web services', na=False), "category"] = csv_mapping.categoryDict["phone"][0]
#transformCom_giro_df.loc[transformCom_giro_df['company_name'].str.contains('HUTCHISON', na=False), "category"] = csv_mapping.categoryDict["phone"][0]
#transformCom_giro_df.loc[transformCom_giro_df['company_name'].str.contains('Hutchison', na=False), "category"] = csv_mapping.categoryDict["phone"][0]
#transformCom_giro_df.loc[transformCom_giro_df['company_name'].str.contains('Stadtwerke Kufstein', na=False), "category"] = csv_mapping.categoryDict["phone"][0]




#transformCom_giro_df.loc[("Billa" in transformCom_giro_df.revenue_text) & (transformCom_giro_df.category == "Uncategorized Expenses"), "category"] = csv_mapping.categoryDict["groceries"][0]
#df_test = transformCom_giro_df.loc[(transformCom_giro_df['revenue_text'].str.contains('Bankomat', na=False) & (transformCom_giro_df.category == "Uncategorized Expenses")), show_col]
#df_test.head(10)
transformCom_giro_df.loc[transformCom_giro_df.category.isin(csv_mapping.categoryDict["uncategorized"]), show_col].head(10)
#transformCom_giro_df.loc[transformCom_giro_df.category == ("Jewelry"), show_col].head(100)
#transformCom_giro_df.loc[transformCom_giro_df['revenue_text'].str.contains('JUFFINGER', na=False), show_col].value_counts()


##export cleaned CSV or Excel
#fexport_csv = df_amazon.to_csv (r'./csv_cleaned/cleaned_dataframe.csv', index = None, header=True)
export_csv = transformCom_giro_df.to_excel (r'./csv_cleaned/cleaned_dataframe.xlsx', index = None, header=True, engine='xlsxwriter')

