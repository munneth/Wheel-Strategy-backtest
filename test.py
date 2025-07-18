import unittest
from unittest.mock import patch
import getStockData
import getOptionsData
import main

class TestGetStockData(unittest.TestCase):
    @patch('getStockData.requests.get')
    def test_getStockData(self, mock_get):
        # Mock API response
        mock_get.return_value.json.return_value = {"Time Series (Daily)": {"2024-08-01": {"2. high": "150", "3. low": "140", "1. open": "145"}}}
        data = getStockData.getStockData('2024-08-01')
        self.assertIn("Time Series (Daily)", data)

    @patch('getStockData.getStockData')
    def test_getHigh(self, mock_getStockData):
        mock_getStockData.return_value = {"Time Series (Daily)": {"2024-08-01": {"2. high": "150"}}}
        self.assertEqual(getStockData.getHigh('2024-08-01'), "150")

    @patch('getStockData.getStockData')
    def test_getLow(self, mock_getStockData):
        mock_getStockData.return_value = {"Time Series (Daily)": {"2024-08-01": {"3. low": "140"}}}
        self.assertEqual(getStockData.getLow('2024-08-01'), "140")

    @patch('getStockData.getStockData')
    def test_getOpen(self, mock_getStockData):
        mock_getStockData.return_value = {"Time Series (Daily)": {"2024-08-01": {"1. open": "145"}}}
        self.assertEqual(getStockData.getOpen('2024-08-01'), "145")

    def test_calendarIncrement(self):
        self.assertEqual(getStockData.calendarIncrement('2024-08-01'), '2024-08-02')

class TestGetOptionsData(unittest.TestCase):
    @patch('getOptionsData.requests.get')
    def test_fetchOptions(self, mock_get):
        mock_get.return_value.json.return_value = {'data': [{'expiration': '2024-09-01', 'strike': '100', 'bid': '5'}]}
        data = getOptionsData.fetchOptions('2024-08-01')
        self.assertIsInstance(data, list)

    def test_getDay(self):
        self.assertEqual(getOptionsData.getDay('2024-08-01'), 1)

    def test_getMonth(self):
        self.assertEqual(getOptionsData.getMonth('2024-08-01'), 8)

    def test_getExpireDate(self):
        arr = [("2024-09-01", "100", "5")]
        self.assertEqual(getOptionsData.getExpireDate(arr, "5", "100"), "2024-09-01")

    def test_getViableOptions(self):
        options = [{'expiration': '2024-09-05'}, {'expiration': '2024-10-01'}]
        result = getOptionsData.getViableOptions(options, '2024-08-01')
        self.assertIsInstance(result, list)

    def test_getStrikeBidPairs(self):
        options = [{'expiration': '2024-09-01', 'strike': '100', 'bid': '5'}]
        pairs = getOptionsData.getStrikeBidPairs(options)
        self.assertIn(("2024-09-01", "100", "5"), pairs)

    def test_getStrikes(self):
        # This function prints, so just check it runs
        options = [{'strike': '100'}]
        getOptionsData.getStrikes(options)

    def test_getBids(self):
        # This function prints, so just check it runs
        options = [{'bid': '5'}]
        getOptionsData.getBids(options)

class TestMain(unittest.TestCase):
    @patch('builtins.input', side_effect=["1000", "2024-08-01", "10", "100", "5", "1"])
    @patch('main.fetchOptions', return_value=[{'expiration': '2024-09-01', 'strike': '100', 'bid': '5'}])
    @patch('main.getViableOptions', return_value=[{'expiration': '2024-09-01', 'strike': '100', 'bid': '5'}])
    @patch('main.getStrikeBidPairs', return_value=[("2024-09-01", "100", "5")])
    @patch('main.getExpireDate', return_value="2024-09-01")
    @patch('main.getDay', return_value=1)
    @patch('main.getMonth', return_value=8)
    @patch('main.getLow', return_value="90")
    @patch('main.getHigh', return_value="110")
    @patch('main.getOpen', return_value="95")
    @patch('main.calendarIncrement', return_value="2024-08-02")
    def test_main(self, *_):
        # Just check that main runs without error with mocks
        main.main()

if __name__ == "__main__":
    unittest.main()
