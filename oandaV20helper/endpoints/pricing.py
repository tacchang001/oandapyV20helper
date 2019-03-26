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


def _average_of_price(prices):
    if len(prices) == 1:
        price = float(prices[0]['price'])
        volume = int(prices[0]['liquidity'])
    else:
        _sum = 0.0
        volume = 0.0
        for i in prices:
            d = int(i['liquidity'])
            _sum = _sum + (float(i['price']) * d)
            volume = volume + d
        price = _sum / volume

    return price, volume


def to_bidask(raw_dict):
    bidask = None
    if raw_dict['type'] == 'PRICE':
        bidask = pd.DataFrame()
        bidask['tradeable'] = [raw_dict['tradeable']]
        bidask['tradeable'] = bidask['tradeable'].astype('bool')
        bidask['instrument'] = raw_dict['instrument']
        bidask['time'] = raw_dict['time']
        bidask['time'] = pd.to_datetime(bidask['time'], format=_TIMESTAMP_FORMAT)
        bidask['asks'], bidask['volumeAsk'] = _average_of_price(raw_dict['asks'])
        bidask['bids'], bidask['volumeBid'] = _average_of_price(raw_dict['bids'])
        bidask['closeoutBid'] = raw_dict['closeoutBid']
        bidask['closeoutAsk'] = raw_dict['closeoutAsk']

    return bidask


