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
