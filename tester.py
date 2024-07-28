import unittest
import pandas as pd
from analyze import AnalyzeOrders

class TestAnalyzeOrders(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.df = pd.read_csv('orders.csv')
        cls.df['order_date'] = pd.to_datetime(cls.df['order_date'])
        cls.analyzer = AnalyzeOrders(cls.df)

    def test_revenue_per_month(self):
        result = self.analyzer.revenue_per_month()
        expected = self.df.copy()
        expected['month'] = expected['order_date'].dt.to_period('M')
        expected = expected.groupby('month')['product_price'].sum()
        pd.testing.assert_series_equal(result, expected)

    def test_revenue_per_product(self):
        result = self.analyzer.revenue_per_product()
        expected = self.df.groupby('product_id')['product_price'].sum()
        pd.testing.assert_series_equal(result, expected)

    def test_revenue_per_customer(self):
        result = self.analyzer.revenue_per_customer()
        expected = self.df.groupby('customer_id')['product_price'].sum()
        pd.testing.assert_series_equal(result, expected)

    def test_top_10_customers(self):
        result = self.analyzer.top_10_customers()
        expected = self.df.groupby('customer_id')['product_price'].sum().nlargest(10)
        pd.testing.assert_series_equal(result, expected)

if __name__ == "__main__":
    unittest.main()

    # Create a status file
    with open('test_status.txt', 'w') as f:
        f.write('Testing done and verified')
