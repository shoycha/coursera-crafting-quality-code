import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    # Add your test methods for a1.stock_price_summary here.
    def test_stockprice_1(self):
        """ test with all 0's """
        actual = a1.stock_price_summary([0.0, 0.0, 0.0, 0.00, 0, 0, 0.0, 0])
        expected = (0, 0)
        self.assertEqual(actual, expected)

    def test_stockprice_2(self):
        """ test with all positive"""
        actual = a1.stock_price_summary([0.2, 0, 0.3, 0.05, 0, 0, 0.1, 0.01])
        expected = (0.66, 0)
        self.assertEqual(actual, expected)

    def test_stockprice_3(self):
        """ test with all negative """
        actual = a1.stock_price_summary([-0.2, 0, -0.3, -0.05, 0, 0, -0.1, -0.01])
        expected = (0, -0.66)
        self.assertEqual(actual, expected)

    def test_stockprice_4(self):
        """ test with both negative and positive """
        actual = a1.stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
        expected = (0.14, -0.17)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(exit=False)
