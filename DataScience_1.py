# coding: utf-8
import pandas as pd
# import os
# import codecs
# import locale

# ----中文乱码问题-------
import sys

# reload(sys)
# sys.setdefaultencoding('utf8')
# ---------------------

# from sqlalchemy import create_engine
#
# engine = create_engine('sqlite:///:memory:')
#
# sql_dataframe = pd.read_sql_table('my_table', engine, columns=['ColA', 'ColB'])
# xls_dataframe = pd.read_excel('my_dataset.xlsx', 'Sheet1', na_values=['NA', '?'])
# json_dataframe = pd.read_json('my_dataset.json', orient='columns')
# csv_dataframe = pd.read_csv('my_dataset.csv', sep=',')
table_dataframe = pd.read_html('http://jwc.jxnu.edu.cn/', encoding='gb2312' )[0]

excel_dataframe = pd.read_excel("/Users/Yel/Desktop/mining_folder/tele_20180315.xlsx",
                                na_values=['N/A'],
                                usecols="A:D",
                                header=0)  # names=["phone_num", "uname", "sex", "ID_card"] usecols=["A:C"],index_col=0,

# print(excel_dataframe.tail(5))
# print(excel_dataframe.index)
# print(excel_dataframe.columns)
# print(excel_dataframe.dtypes)
# print(excel_dataframe.describe())

df = pd.DataFrame({'AAA': [4, 5, 6, 7], 'BBB': [10, 20, 30, 40], 'CCC': [100, 50, -30, -50]})
print(df);

str1 = table_dataframe.to_string()
ss = str1.encode("gb2312", errors='ignore')
print(ss)

# print("中国".encode())

# print(help(pd.read_excel))
