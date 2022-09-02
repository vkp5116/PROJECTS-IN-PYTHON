#!/usr/bin/env python
# coding: utf-8

# # For this project, I will assume the role of a Data Scientist / Data Analyst working for a new startup investment firm that helps customers invest their money in stocks. My job is to extract financial data like historical share price and quarterly revenue reportings from various sources using Python libraries and webscraping on popular stocks. After collecting this data I will visualize it in a dashboard to identify patterns or trends. The stocks I will work with are Tesla, Amazon, AMD, and GameStop.

# pip install yfinance==0.1.67

import yfinance as yf
import pandas as pd

apple_stock = yf.Ticker("AAPL")


apple_info = apple_stock.info
apple_info


# I will use the history() method to get the share price of the stock
apple_share_price = apple_stock.history(period = "max")
# This will return a data frame 
apple_share_price.head()


apple_share_price.reset_index(inplace=True)
# Now, I will plot date vs open price 
apple_share_price.plot(x="Date",y="Open")


# Dividends are the distribution of a companys profits to shareholders. In this case they are defined as an amount of money returned per share an investor owns.


apple_stock.dividends

apple_stock.dividends.plot()


# # I will analyse the AMD stock


amd_stock = yf.Ticker("AMD")

amd_info = amd_stock.info
amd_info["country"]
amd_info["sector"]


amd_share_price = amd_stock.history(period = "max")
amd_share_price.reset_index(inplace=True)




