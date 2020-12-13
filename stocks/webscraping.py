import pandas as pd
import numpy as np
import requests
import lxml
from bs4 import BeautifulSoup
from decouple import config


def stock_data(ticker):
    API_URL = "https://www.alphavantage.co/query"
    api_key = '**********'

    data = {
        "function": "BALANCE_SHEET",
        "symbol": ticker,
        "outputsize" : "compact",
        "datatype": "json",
        "apikey": api_key,
    }

    response = requests.get(API_URL, data)
    response_json = response.json()

    balance_sheet = pd.DataFrame(response_json['annualReports'])
    balance_sheet.set_index('fiscalDateEnding', inplace=True)

    total_assets = balance_sheet.get('totalAssets')[0]
    total_debt = balance_sheet.get('longTermDebt')[0]
    total_current_liabilities = balance_sheet.get('totalCurrentLiabilities')[0]


    data = {
        "function": "INCOME_STATEMENT",
        "symbol": ticker,
        "outputsize" : "compact",
        "datatype": "json",
        "apikey": api_key,
    }

    response = requests.get(API_URL, data)
    response_json = response.json()

    income_statement = pd.DataFrame(response_json['annualReports'])
    income_statement.set_index('fiscalDateEnding', inplace=True)

    ebit = income_statement.get('ebit')[0]

    data = {
        "function": "OVERVIEW",
        "symbol": ticker,
        "outputsize" : "compact",
        "datatype": "json",
        "apikey": api_key,
    }

    response = requests.get(API_URL, data)
    response_json = response.json()

    eps = response_json['EPS']
    pe = response_json['PERatio']
    name = response_json['Name']

    leverage_ratio = int(total_debt) / int(total_assets)

    roce = int(ebit) / (int(total_assets) - int(total_current_liabilities))

    score = float(eps) * ( 1 + float(roce) - float(leverage_ratio))

    return {'ticker':ticker, 'leverage_ratio':leverage_ratio, 'roce':roce, 'eps':float(eps), 'pe':float(pe), 'score':score, 'name':name, 'image_url': f'https://g.foolcdn.com/art/companylogos/mark/{ticker}.png'}


def ranking(stock):
    return stock['score']


