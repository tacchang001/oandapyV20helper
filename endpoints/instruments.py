from oandapyV20 import API
import oandapyV20.endpoints.instruments as instruments
import pandas as pd

from conf import PyOandaConfig

_TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:00.000000000Z"


def get_candles(instrument, params):
    _conf = PyOandaConfig()
    _api = API(access_token=_conf.access_token, environment="practice")
    _request = instruments.InstrumentsCandles(instrument=instrument, params=params)
    _api.request(_request)

    return _request.response


def make_from_to_params(granularity, from_time, to_time):
    _params = {
        "from": from_time.strftime(_TIMESTAMP_FORMAT),
        "to": to_time.strftime(_TIMESTAMP_FORMAT),
        "granularity": granularity
    }

    return _params


def make_to_params(granularity, to_time):
    _params = {
        "to": to_time.strftime(_TIMESTAMP_FORMAT),
        "granularity": granularity
    }

    return _params


def make_from_count_params(granularity, from_time, count):
    _params = {
        "from": from_time.strftime(_TIMESTAMP_FORMAT),
        "count": count,
        "granularity": granularity
    }

    return _params


def to_dataframe(candle_dict):
    candle = pd.DataFrame.from_dict([row['mid'] for row in candle_dict['candles']])
    candle['time'] = [row['time'] for row in candle_dict['candles']]
    candle['time'] = pd.to_datetime(candle['time'], format=_TIMESTAMP_FORMAT)
    candle['volume'] = [row['volume'] for row in candle_dict['candles']]
    for name in ['o', 'h', 'l', 'c']:
        candle[name] = candle[name].astype('float')

    return candle


def _time_str(date_time):
    return date_time.strftime(_TIMESTAMP_FORMAT)


def main():
    from datetime import datetime

    _to1 = datetime(2018, 4, 10, 12, 34, 56)
    _params1 = make_to_params("M15", to_time=_to1)
    _candle_dict1 = get_candles("USD_JPY", _params1)
    _candles1 = to_dataframe(_candle_dict1)
    print(_candles1)

    _from2 = datetime(2018, 4, 10, 0, 0, 0)
    _to2 = datetime(2018, 4, 10, 12, 34, 56)
    _params2 = make_from_to_params("M15", from_time=_from2, to_time=_to2)
    _candle_dict2 = get_candles("USD_JPY", _params2)
    _candles2 = to_dataframe(_candle_dict2)
    print(_candles2)

    _from3 = datetime(2018, 4, 10, 0, 0, 0)
    _count3 = 30
    _params3 = make_from_count_params("M15", from_time=_from3, count=_count3)
    _candle_dict3 = get_candles("USD_JPY", _params3)
    _candles3 = to_dataframe(_candle_dict3)
    print(_candles3)


if __name__ == "__main__":
    main()
