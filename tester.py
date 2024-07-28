import unittest
import pandas as pd
from analyze import AnalyzeOrders

class TestAnalyzeOrders(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Read the orders data from 'orders.csv' file
        cls.df = pd.read_csv('orders.csv')
        # Convert the 'order_date' column to datetime format
        cls.df['order_date'] = pd.to_datetime(cls.df['order_date'])
        # Create an instance of AnalyzeOrders class
        cls.analyzer = AnalyzeOrders(cls.df)

    def test_revenue_per_month(self):
        # Test the revenue_per_month method
        result = self.analyzer.revenue_per_month()
        expected = self.df.copy()
        expected['month'] = expected['order_date'].dt.to_period('M')
        expected = expected.groupby('month')['product_price'].sum()
        pd.testing.assert_series_equal(result, expected)

    def test_revenue_per_product(self):
        # Test the revenue_per_product method
        result = self.analyzer.revenue_per_product()
        expected = self.df.groupby('product_id')['product_price'].sum()
        pd.testing.assert_series_equal(result, expected)

    def test_revenue_per_customer(self):
        # Test the revenue_per_customer method
        result = self.analyzer.revenue_per_customer()
        expected = self.df.groupby('customer_id')['product_price'].sum()
        pd.testing.assert_series_equal(result, expected)

    def test_top_10_customers(self):
        # Test the top_10_customers method
        result = self.analyzer.top_10_customers()
        expected = self.df.groupby('customer_id')['product_price'].sum().nlargest(10)
        pd.testing.assert_series_equal(result, expected)

if __name__ == "__main__":
    # Run the unit tests
    unittest.main()

    # Create a status file
    with open('test_status.txt', 'w') as f:
        f.write('Testing done and verified')
