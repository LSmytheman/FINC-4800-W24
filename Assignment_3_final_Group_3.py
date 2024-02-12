# database and plugins used in this program
import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd
from matplotlib import pyplot as plt

# list and dictionaries to be used in the program
tickers = [
    "^GSPC",
    "XLE",
    "^SP500-50",
    "^SP500-25",
    "^SP500-30",
    "^SP500-60",
    "^SP500-20",
    "^SP500-35",
    "^SP500-40",
    "^SP500-1010",
    "^SP500-15",
    "^SP500-55",
]
fin_info = {ticker: [] for ticker in tickers}

for ticker in tickers:
  stock_data = yf.Ticker(ticker)
  ticker_name = stock_data.info['longName']
  fin_info[ticker].append(ticker_name)
  
# function to get the date
end_date = datetime.strptime(input("Please enter Monday's date (YYYY-MM-DD): "), "%Y-%m-%d")
start_date_week = end_date - timedelta(days=7)
start_date_ytd = datetime(2023, 1, 2).date()

# Calculates the return for each sector during the given period.
# If it's over a single day, it will use the closing price
for ticker in tickers:
  # Weekly return with dividends reinvested
  stock_data_week = 

  # YTD return with dividends reinvested
  stock_data_ytd = 

# calculates the relative change of each sector during the given period to the S&P500
# Create subplots
fig, axes = plt.subplots(nrows=2, figsize=(12, 10))
fig.suptitle('Sector Returns', fontsize=8)

# Plot Weekly Returns
weekly_returns = [fin_info[ticker][1] * 100 for ticker in fin_info]
sorted_tickers = sorted(tickers, key=lambda ticker: weekly_returns[tickers.index(ticker)], reverse=True)
axes[0].bar(tickers, [fin_info[ticker][1] * 100 for ticker in fin_info], color='blue')
axes[0].set_ylabel('Weekly Return (%)')
axes[0].set_title('Weekly Returns')

for i, value in enumerate(weekly_returns):
  va = 'top' if value < 0 else 'bottom'
  axes[0].text(i, value, f'{value:.2f}%', ha='center', va=va, color='black')
axes[0].set_xticks(tickers)
axes[0].set_xticklabels([fin_info[ticker][0] for ticker in fin_info], rotation=45, ha='right')
  
# Plot YTD Returns
ytd_returns = [fin_info[ticker][-1] * 100 for ticker in fin_info]
axes[1].bar(tickers, [fin_info[ticker][-1] * 100 for ticker in fin_info], color='blue')
axes[1].set_ylabel('YTD Return (%)')
axes[1].set_title('YTD Returns')

for i, value in enumerate(ytd_returns):
  va = 'top' if value < 0 else 'bottom'
  axes[1].text(i, value, f'{value:.2f}%', ha='center', va=va, color='black')

axes[1].set_xticks(tickers)
axes[1].set_xticklabels([fin_info[ticker][0] for ticker in fin_info], rotation=45, ha='right', fontsize=4)

# Rotate x-axis labels for better readability
for ax in axes:
  ax.axhline(y=0, color='black', linestyle='-', linewidth=2, label='y = 0')
for ax in axes:
  ax.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()
