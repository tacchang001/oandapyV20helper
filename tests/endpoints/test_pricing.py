from unittest import TestCase
import json

from oandaV20helper.endpoints.pricing import to_dom


class TestPricing(TestCase):

    def test_to_dataframe(self):
        data_dict = [
            'test_pricing01.json',
            'test_pricing02.json',
            'test_pricing03.json'
        ]
        for _file_name in data_dict:
            with open(_file_name, 'r') as f:
                raw_dict = json.load(f)
                result = to_dom(raw_dict)
                print(result)
