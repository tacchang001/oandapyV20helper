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


def to_dom(raw_dict):
    """
    OANDA Streamから得られる板情報（Depth of Market）をオリジナルの板情報に変換する。

    :param raw_dict: OANDA Streamから受信した板情報
    :return: オリジナルの板情報
    """
    dom = None
    if raw_dict['type'] == 'PRICE':
        dom = pd.DataFrame()
        dom['tradeable'] = [raw_dict['tradeable']]
        dom['tradeable'] = dom['tradeable'].astype('bool')
        dom['instrument'] = raw_dict['instrument']
        dom['time'] = raw_dict['time']
        dom['time'] = pd.to_datetime(dom['time'], format=_TIMESTAMP_FORMAT)
        dom['asks'], dom['volumeAsk'] = _average_of_price(raw_dict['asks'])
        dom['bids'], dom['volumeBid'] = _average_of_price(raw_dict['bids'])
        dom['closeoutBid'] = raw_dict['closeoutBid']
        dom['closeoutAsk'] = raw_dict['closeoutAsk']

    return dom


