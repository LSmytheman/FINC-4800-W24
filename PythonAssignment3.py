import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display, clear_output
import time

# Mapping of sector ETF symbols to their full titles
sector_mapping = {
    'XLC': 'Comm. Serv.',
    'XLY': 'Cons. Disc.',
    'XLP': 'Cons. Staples',
    'XLE': 'Energy',
    'XLF': 'Financials',
    'XLV': 'Health Care',
    'XLI': 'Industrials',
    'XLB': 'Materials',
    'XLRE': 'Real Estate',
    'XLK': 'Technology',
    'XLU': 'Utilities',
    '^GSPC': 'S&P 500'
}

# List of sector ETF symbols
sector_symbols = list(sector_mapping.keys())

# Weekly and year-to-date updates
weekly_date_1 = '2024-01-19'
ytd_date_1 = '2024-01-19'
weekly_date_2 = '2024-01-12'
ytd_date_2 = '2024-01-12'

# Download historical data for each sector
data = yf.download(sector_symbols, start='2024-01-01', end=pd.to_datetime('today'))

# Rename tickers to full titles
data.rename(columns=sector_mapping, inplace=True)

# Function to plot returns
def plot_returns(returns, title):
    clear_output(wait=True)
    plt.figure(figsize=(15, 6))
    returns.plot(kind='bar', color='darkblue')
    plt.axhline(y=0, color='black', linestyle='-', linewidth=1)
    plt.title(title)
    plt.xlabel('Sector ETFs')
    plt.ylabel('Returns')
    plt.tight_layout()
    plt.show()

# Function to update and display weekly and year-to-date returns bar graphs
def plot_combined_returns(week_date, ytd_date):
    clear_output(wait=True)
    plt.figure(figsize=(15, 10))

    # Plotting weekly returns for the specified week
    plt.subplot(2, 2, 1)
    weekly_returns = data['Adj Close'].loc[:week_date].pct_change().dropna().iloc[-1] * 100
    if not weekly_returns.empty:
        weekly_returns_sorted = weekly_returns.sort_values(ascending=False)
        weekly_returns_sorted.plot(kind='bar', color='darkblue')
        plt.axhline(y=0, color='black', linestyle='-', linewidth=1)
        plt.title(f'Weekly Returns (Week of {weekly_date_1})')
        plt.xlabel('Sector ETFs')
        plt.ylabel('Returns')

    # Plotting year-to-date returns for the specified date
    plt.subplot(2, 2, 2)
    ytd_returns = data['Adj Close'].loc[:ytd_date].pct_change().dropna().cumsum().iloc[-1] * 100
    if not ytd_returns.empty:
        ytd_returns_sorted = ytd_returns.sort_values(ascending=False)
        ytd_returns_sorted.plot(kind='bar', color='darkgreen')
        plt.axhline(y=0, color='black', linestyle='-', linewidth=1)
        plt.title(f'Year-to-Date Returns (Week of {ytd_date_1})')
        plt.xlabel('Sector ETFs')
        plt.ylabel('Returns')

    # Plotting weekly returns for the week of January 12, 2024
    plt.subplot(2, 2, 3)
    weekly_returns_12 = data['Adj Close'].loc[:week_date].pct_change().dropna().iloc[-2] * 100
    if not weekly_returns_12.empty:
        weekly_returns_sorted_12 = weekly_returns_12.sort_values(ascending=False)
        weekly_returns_sorted_12.plot(kind='bar', color='darkblue')
        plt.axhline(y=0, color='black', linestyle='-', linewidth=1)
        plt.title(f'Weekly Returns (Week of {weekly_date_2})')
        plt.xlabel('Sector ETFs')
        plt.ylabel('Returns')

    # Plotting year-to-date returns for the week of January 12, 2024
    plt.subplot(2, 2, 4)
    ytd_returns_12 = data['Adj Close'].loc[:ytd_date].pct_change().dropna().cumsum().iloc[-2] * 100
    if not ytd_returns_12.empty:
        ytd_returns_sorted_12 = ytd_returns_12.sort_values(ascending=False)
        ytd_returns_sorted_12.plot(kind='bar', color='darkgreen')
        plt.axhline(y=0, color='black', linestyle='-', linewidth=1)
        plt.title(f'Year-to-Date Returns (Week of {ytd_date_2})')
        plt.xlabel('Sector ETFs')
        plt.ylabel('Returns')

    plt.tight_layout()
    plt.show()

plot_combined_returns(weekly_date_1, ytd_date_1)
time.sleep(2)
plot_combined_returns(weekly_date_2, ytd_date_2)