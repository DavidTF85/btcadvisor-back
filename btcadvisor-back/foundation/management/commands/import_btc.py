"""""
read_csv.py

Description:
This is how you read the downloaded file.

How to Install:
pip install requests
pip install pandas

Source: https://romanorac.github.io/cryptocurrency/analysis/2017/12/17/cryptocurrency-analysis-with-python-part1.html
Special Thanks: https://towardsdatascience.com/cryptocurrency-analysis-with-python-macd-452ceb251d7c
"""
import pandas as pd
from django.db import migrations, models

filename = "BTC_USD_Bitstamp_day_2019-12-17.csv"
#funtions will read my csv and sorted to the lates 25 days
def read_dataset(filename):
    print('Reading data from %s' % filename)
    df = pd.read_csv(filename)
    df.datetime = pd.to_datetime(df.datetime) # change type from object to datetime
    df = df.set_index('datetime')
    df = df.sort_index(ascending=False) # sort by datetime
    print(df.shape)
    return df

df = read_dataset(filename)
#print(df.head(25))


class ImportBtc(models.Models):
    print (self)



#1. import my timesieresdata model here!
#2. load all the data not the last 25 in this models
#3. go trwo the csv file and imoport the data into the timesiresdata models
