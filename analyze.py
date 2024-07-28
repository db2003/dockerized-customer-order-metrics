import pandas as pd
from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

# Load DataFrame globally so it can be used across the application
df = pd.read_csv('orders.csv')
df['order_date'] = pd.to_datetime(df['order_date'])

class AnalyzeOrders:
    def __init__(self, dataframe):
        self.df = dataframe

    def revenue_per_month(self):
        # Calculate revenue per month by grouping orders by month and summing product prices
        self.df['month'] = self.df['order_date'].dt.to_period('M')
        return self.df.groupby('month')['product_price'].sum()

    def revenue_per_product(self):
        # Calculate revenue per product by grouping orders by product ID and summing product prices
        return self.df.groupby('product_id')['product_price'].sum()

    def revenue_per_customer(self):
        # Calculate revenue per customer by grouping orders by customer ID and summing product prices
        return self.df.groupby('customer_id')['product_price'].sum()

    def top_10_customers(self):
        # Get the top 10 customers based on revenue
        return self.revenue_per_customer().nlargest(10)

@app.route('/results')
def results():
    analyzer = AnalyzeOrders(df)
    monthly_revenue = analyzer.revenue_per_month()
    product_revenue = analyzer.revenue_per_product()
    customer_revenue = analyzer.revenue_per_customer()
    top_customers = analyzer.top_10_customers()

    # Convert PeriodIndex to string for serialization
    monthly_revenue.index = monthly_revenue.index.to_timestamp().strftime('%Y-%m')
    combined_results = {
        'revenue_per_month': monthly_revenue.to_dict(),
        'revenue_per_product': product_revenue.to_dict(),
        'revenue_per_customer': customer_revenue.to_dict(),
        'top_10_customers': top_customers.to_dict(),
    }

    return jsonify(combined_results)

@app.route('/test_status')
def test_status():
    try:
        # Run the tests using pytest
        result = subprocess.run(['pytest', 'tester.py'], capture_output=True, text=True)
        # Check if tests passed
        if result.returncode == 0:
            return "Testing done and verified", 200
        else:
            return "Testing failed", 500
    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)
