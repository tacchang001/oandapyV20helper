from oandapyV20 import API
import oandapyV20.endpoints.instruments as instruments
import pandas as pd

from conf import PyOandaConfig

_TIMESTAMP_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'


def to_dataframe(raw_dict):
    candle = pd.DataFrame.from_dict(raw_dict)
    # candle['time'] = [row['time'] for row in candle_dict['candles']]
    # candle['time'] = pd.to_datetime(candle['time'], format=_TIMESTAMP_FORMAT)
    # candle['volume'] = [row['volume'] for row in candle_dict['candles']]
    # for name in ['o', 'h', 'l', 'c']:
    #     candle[name] = candle[name].astype('float')

    return candle
