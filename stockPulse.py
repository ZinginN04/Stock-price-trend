from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import matplotlib.pyplot as plt

# Replace with your Alpha Vantage API key
API_KEY = 'QMD85U1IUFP9Z0YL'

# Initialize TimeSeries object
ts = TimeSeries(key=API_KEY, output_format='pandas')

# User input for stock symbol and date range
stock_symbol = input("Enter stock symbol (e.g., RELIANCE.BSE, M&M.BO, ITC.BSE): ").strip()
start_month = input("Enter start date (YYYY-MM): ").strip()
end_month = input("Enter end date (YYYY-MM): ").strip()

# Fetch monthly adjusted data
data, meta_data = ts.get_monthly_adjusted(symbol=stock_symbol)

# Convert index to datetime format
data.index = pd.to_datetime(data.index)

# Filter data based on user input
filtered_data = data.loc[(data.index.strftime('%Y-%m') >= start_month) & (data.index.strftime('%Y-%m') <= end_month)]

# Display filtered data
print(filtered_data)

# Plot the closing price trend
plt.figure(figsize=(10,5))
plt.plot(filtered_data.index, filtered_data['5. adjusted close'], marker='o', linestyle='-', color='b', label='Adjusted Close')
plt.xlabel("Date")
plt.ylabel("Stock Price")
plt.title(f"Stock Price Trend for {stock_symbol}")
plt.legend()
plt.grid()
plt.show()
