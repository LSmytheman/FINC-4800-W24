import yfinance as yf
import datetime as datetime
from datetime import timedelta
import pandas as pd

ticker = "XLC"

end_date = datetime.date.today() - timedelta(days=1)
last_year = end_date - timedelta(days=365)
if (last_year.year % 4 == 0 and last_year.year % 100 !=0) or (last_year.year % 400==0):
    time_subtract = timedelta(366)
else:
    time_subtract = timedelta(365)

yearly_start_date = end_date - time_subtract
YTD_start_date = datetime.date(2023, 12, 29)

ticker_info = yf.download(ticker, yearly_start_date, end_date)
yearly_start_price = ticker_info["Adj Close"].iloc[0]
yearly_end_price = ticker_info["Adj Close"].iloc[-1]
yearly_return = (yearly_end_price-yearly_start_price)/yearly_start_price

ticker_info = yf.download(ticker, YTD_start_date, end_date)
YTD_start_price = ticker_info["Adj Close"].iloc[0]
YTD_end_price = ticker_info["Adj Close"].iloc[-1]
YTD_return = (YTD_end_price-YTD_start_price)/YTD_start_price

print(f"end price:{yearly_end_price: .4f}")
print(f"yearly start price:{yearly_start_price: .4f}")
print(f"YTD start price:{YTD_start_price: .4f}")

print(end_date)
print(yearly_start_date)
print(f"The yearly return is:{yearly_return: .2%}")
print(f"The YTD return is:{YTD_return: .2%}")
