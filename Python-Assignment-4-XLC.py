import yfinance as yf

def calculate_annual_return(symbol, start_date, end_date):
    # Download historical data for the specified symbol and date range
    data = yf.download(symbol, start=start_date, end=end_date)

    # Extract adjusted close prices and round to 6 decimal places
    adjusted_close_start = round(data['Adj Close'].iloc[0], 6)
    adjusted_close_end = round(data['Adj Close'].iloc[-1], 6)  # Use the last row for the last trading day

    # Print out the adjusted close prices used in the calculation
    print(f"Adjusted Close at Start of Year: {adjusted_close_start}")
    print(f"Adjusted Close at End of Year: {adjusted_close_end}")

    # Calculate the annual return
    annual_return = ((adjusted_close_end - adjusted_close_start) / adjusted_close_start) * 100

    return annual_return

# Symbol for XLC sector
symbol = "XLC"
# Start date and end date for 2023
start_date = "2023-01-03"
end_date = "2023-12-31"  # Adjusted to fetch data until December 31, 2023

# Calculate the annual return for the specified symbol and date range
annual_return = calculate_annual_return(symbol, start_date, end_date)
print(f"The annual return of {symbol} sector in 2023 is: {annual_return:.2f}%")
