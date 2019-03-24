from unittest import TestCase
import json

from oandaV20helper.endpoints.pricing import to_dataframe


class TestPricing(TestCase):

    def test_to_dataframe(self):
        data_dict = [
            'test_pricing.json',
            'test_pricing.json'
        ]
        for _file_name in data_dict:
            with open(_file_name, 'r') as f:
                json_data = json.load(f)
                result = to_dataframe(json_data)
                print(result)
