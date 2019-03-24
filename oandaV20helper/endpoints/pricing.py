from oandapyV20 import API
import oandapyV20.endpoints.instruments as instruments
import pandas as pd

# https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html#available-options
pd.options.display.width = 120
pd.options.display.max_rows = 30
pd.options.display.max_columns = 20
pd.options.display.max_colwidth = 20
pd.set_option('display.unicode.east_asian_width', True)
pd.options.display.colheader_justify = 'right'

_TIMESTAMP_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'


def to_dataframe(raw_dict):
    candle = None
    if raw_dict['type'] == 'PRICE':
        candle = pd.DataFrame()
        candle['tradeable'] = [raw_dict['tradeable']]
        candle['tradeable'] = candle['tradeable'].astype('bool')
        candle['instrument'] = raw_dict['instrument']
        candle['time'] = raw_dict['time']
        candle['time'] = pd.to_datetime(candle['time'], format=_TIMESTAMP_FORMAT)
        candle['asks'] = [row['price'] for row in raw_dict['asks']]
        candle['bids'] = [row['price'] for row in raw_dict['bids']]
        candle['closeoutBid'] = raw_dict['closeoutBid']
        candle['closeoutAsk'] = raw_dict['closeoutAsk']

    return candle
