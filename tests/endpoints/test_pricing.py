import json

import pytest

from oandaV20helper.endpoints.pricing import to_dom


class TestPricing:
    @pytest.mark.parametrize("num, filename", [
        (1, 'test_pricing01.json'),
        (3, 'test_pricing02.json'),
        (15, 'test_pricing03.json')
    ])
    def test_to_dataframe(self, num, filename):
        with open(filename, 'r') as f:
            raw_dict = json.load(f)
            result = to_dom(raw_dict)
            print(result)


# if __name__ == '__main__':
#     pytest.main(['-v', __file__])
