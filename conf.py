import os
import sys
from configparser import ConfigParser

from singleton import Singleton


class PyOandaConfig(metaclass=Singleton):
    """
    OANDA V20サイトを利用するのに必要な情報を保持する。
    情報源は、以下の順で優先して読み出す。
    * インスタンス生成時の引数で指定されたファイル
    * PYOANDAINIPATHで指定されたディレクトリ/OANDA.ini
    * 実行されたスクリプトと同じディレクトリ/OANDA.ini

    Attributes
    ----------
    account_id : str
        アカウントID
    access_token : str
        アクセストークン
    """

    def __init__(self, filepath=None):
        _filepath = filepath
        try:
            if _filepath is None or len(filepath) == 0:
                _filepath = PyOandaConfig._get_config_filepath()
            _config = ConfigParser()
            _config.read(_filepath)

            self._account_id = _config['oanda']['accountID']
            self._access_token = _config['oanda']['access_token']

        except KeyError as err:
            sys.stderr.write(err)

    @property
    def account_id(self):
        return self._account_id

    @property
    def access_token(self):
        return self._access_token

    @staticmethod
    def _get_config_filepath():
        try:
            _dirname = os.environ.get('PYOANDAINIPATH', os.path.dirname(__file__))
            _config_filepath = os.path.join(_dirname, 'OANDA.ini')
        except KeyError:
            pass

        return _config_filepath


if __name__ == "__main__":
    __conf = PyOandaConfig()
    print(__conf.account_id)
    print(__conf.access_token)
