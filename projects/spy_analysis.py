import yfinance as yf
import pandas as pd

spy = yf.download('SPY', start='2019-01-01', end='2024-01-01')

spy['Daily Return'] = spy['Close'].pct_change()

print("The worst day experienced a", spy['Daily Return'].loc[spy['Daily Return'].idxmin()]*100, "percent loss.")
print("The best day experienced a", spy['Daily Return'].loc[spy['Daily Return'].idxmax()]*100, "percent gain.")

monthly_returns = spy['Daily Return'].resample('ME').mean()
print("The worst month experienced an average", monthly_returns.loc[monthly_returns.idxmin()]*100, "percent loss.")
print("The best month experienced an average", monthly_returns.loc[monthly_returns.idxmax()]*100, "percent gain.")

endsum = (spy['Close'] > spy['Open']).sum().iloc[0]
print("The number of days where the closing price was higher than the opening price is", endsum)

print(spy['Volume'].rolling(30).mean())
print(spy['Volume'].mean())