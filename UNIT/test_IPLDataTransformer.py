import unittest
from IPLDataTransformer import IPLDataTransformer

class TestIPLDataTransformer(unittest.TestCase):
    def setUp(self):
        self.data_transformer = IPLDataTransformer("mock_matches.csv")

    def test_matches_per_year(self):
        expected_result = {'2017': 8, '2008': 11}
        result = self.data_transformer.matches_per_year()
        self.assertEqual(result, expected_result)





if __name__ == '__main__':
    unittest.main()
