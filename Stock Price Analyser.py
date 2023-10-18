#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install yfinance


# In[3]:


import yfinance as yf
import matplotlib.pyplot as plt


# In[4]:


def analyze_stock(symbol, start_date, end_date):
    # Fetch the stock data from Yahoo Finance
    stock_data = yf.download(symbol, start=start_date, end=end_date)

    # Calculate the daily returns
    stock_data['Daily Return'] = stock_data['Close'].pct_change()

    # Plot the closing price and daily returns
    plt.figure(figsize=(10, 5))
    plt.subplot(2, 1, 1)
    plt.plot(stock_data['Close'])
    plt.title('Stock Price')
    plt.ylabel('Price')

    plt.subplot(2, 1, 2)
    plt.plot(stock_data['Daily Return'])
    plt.title('Daily Returns')
    plt.ylabel('Return')

    plt.tight_layout()
    plt.show()


# In[5]:


# Example usage
symbol = 'AAPL'  # Stock symbol (e.g., Apple Inc.)
start_date = '2023-09-01'  # Start date of the analysis
end_date = '2023-09-30'  # End date of the analysis

analyze_stock(symbol, start_date, end_date)


# In[ ]:




