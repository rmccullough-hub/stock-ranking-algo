import pandas as pd
import numpy as np
import requests
import lxml
from bs4 import BeautifulSoup
from .tickers import stocks
from .webscraping import *

# equations for calculating Return on capital employed, Leverage ratio

def update_stocks():
    top_stocks = []
    error_count = 0
    for ticker in stocks:
        try:
            name = summary(ticker)['name']
            eps = summary(ticker)['EPS (TTM)']
            pe = summary(ticker)['PE Ratio (TTM)']
            ebit = income_statement(ticker)[0]
            total_revenue = income_statement(ticker)[1]
            cost_of_revenue = income_statement(ticker)[2]
            capital_employed = balance_sheet(ticker)[1]
            leverage_ratio = balance_sheet(ticker)[0]

            if float(eps) <= 0 or int(ebit) <= 0 or int(capital_employed) <= 0 or float(leverage_ratio) <= 0:
                continue

            stock = {
                'eps': eps,
                'roce': int(ebit)/int(capital_employed),
                'leverage ratio': leverage_ratio,
                'ticker': ticker,
                'total_revenue': total_revenue,
                'cost_of_revenue': cost_of_revenue,
                'pe':pe,
                'name':name,
            }
            top_stocks.append(stock)
            top_stocks = ranking(top_stocks)
            
        except (AttributeError, IndexError, KeyError, TypeError):
            error_count += 1
            print(ticker)
    print(error_count)
    return top_stocks
