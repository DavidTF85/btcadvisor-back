"""
download_csv.py
Description:
This file is used for saving bitcoin price history from start until today.

How to Install:
pip install requests
pip install pandas

Source:
https://romanorac.github.io/cryptocurrency/analysis/2017/12/17/cryptocurrency-analysis-with-python-part1.html

Special Thanks:
- https://towardsdatascience.com/cryptocurrency-analysis-with-python-macd-452ceb251d7c
"""
import requests
import pandas as pd
from datetime import datetime
from django.core.management.base import BaseCommand, CommandError

from_symbol = 'BTC'
to_symbol = 'USD'
exchange = 'Bitstamp'
datetime_interval = 'day'

class Command(BaseCommand):
    help = 'Here you will dowload the BTC price history as CSV file :)'


    def handle(self, *args, **options):
        self.process()

        self.stdout.write(self.style.SUCCESS('Successfully got the historical intra-day BTC prices :p'))

    def process(self):
        data = download_data(from_symbol, to_symbol, exchange, datetime_interval)
        df = convert_to_dataframe(data)
        df = filter_empty_datapoints(df)
        current_datetime = datetime.now().date().isoformat()
        filename = get_filename(from_symbol, to_symbol, exchange, datetime_interval, current_datetime)
        print('Saving data to %s' % filename)
        df.to_csv(filename, index=False)

def get_filename(from_symbol, to_symbol, exchange, datetime_interval, download_date):
    return '%s_%s_%s_%s_%s.csv' % (from_symbol, to_symbol, exchange, datetime_interval, download_date)
def download_data(from_symbol, to_symbol, exchange, datetime_interval):
    supported_intervals = {'minute', 'hour', 'day'}
    assert datetime_interval in supported_intervals,\
        'datetime_interval should be one of %s' % supported_intervals
    print('Downloading %s trading data for %s %s from %s' %
          (datetime_interval, from_symbol, to_symbol, exchange))
    base_url = 'https://min-api.cryptocompare.com/data/histo'
    url = '%s%s' % (base_url, datetime_interval)
    params = {'fsym': from_symbol, 'tsym': to_symbol,
              'limit': 2000, 'aggregate': 1,
              'e': exchange}
    request = requests.get(url, params=params)
    data = request.json()
    return data
def convert_to_dataframe(data):
    df = pd.io.json.json_normalize(data, ['Data'])
    df['datetime'] = pd.to_datetime(df.time, unit='s')
    df = df[['datetime', 'low', 'high', 'open',
             'close', 'volumefrom', 'volumeto']]
    return df
def filter_empty_datapoints(df):
    indices = df[df.sum(axis=1) == 0].index
    print('Filtering %d empty datapoints' % indices.shape[0])
    df = df.drop(indices)
    return df



"""""
read_csv.py
Description:
This is how you read the downloaded file.
How to Install:
pip install requests
pip install pandas
Source: https://romanorac.github.io/cryptocurrency/analysis/2017/12/17/cryptocurrency-analysis-withpython-part1.html
Special Thanks: https://towardsdatascience.com/cryptocurrency-analysis-with-python-macd452ceb251d7c
"""
import xmltodict
import pandas as pd
import datetime
from django.db import transaction
class Command(BaseCommand):
 help = '-'
 #funtions will read my csv and sorted to the lates 25 days
 def read_dataset(self):
 filename = "BTC_USD_Bitstamp_day_2019-12-20.csv"
 print('Reading data from %s' % filename)
 df = pd.read_csv(filename)
 df = df.sort_index(ascending=False) # sort by datetime
 df = df.head(25)
 format = '%Y-%m-%d'
 df['datetime'] = pd.to_datetime(df['datetime'],
 format=format)
 date_extraction = [datetime.datetime.date(d) for d in df['datetime']]
 low_data = pd.to_numeric(df['low'])
 high_data = pd.to_numeric(df['high'])
 open_data = pd.to_numeric(df['open'])
 close_data = pd.to_numeric(df['close'])
 volume_from_data = pd.to_numeric(df['volumefrom'])
 volume_to_data = pd.to_numeric(df['volumeto'])
 low_list = list(low_data)
 high_list = list(high_data)
 open_list = list(open_data)
 close_list = list(close_data)
 volume_from_list = list(volume_from_data)
 volume_to_list = list(volume_to_data)

 for date,low,high,open,close,volumefrom,volumeto in
zip(date_extraction,low_list,high_list,open_list,close_list,volume_from_list,volume_to_list):
 TimeSeriesData.objects.create(
 datetime = date,
 low = low,
 high = high,
 open = open,
 close = close,
 volume_from = volumefrom,
 volume_to = volumeto,
 )

 @transaction.atomic
 def process(self):
 self.read_dataset()

 def handle(self, *args, **options):
 self.process()
 self.stdout.write(self.style.SUCCESS('Successfully processed BTC_USD_Bitstamp_day_2019 Data
File'))
 #1. import my timesieresdata model here!
 #2. load all the data not the last 25 in this models
 #3. go trwo the csv file and imoport the data into the timesiresdata models
