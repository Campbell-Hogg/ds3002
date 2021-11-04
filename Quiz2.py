#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 20:44:07 2021

@author: campbellhogg
"""

import csv 
from csv import DictWriter
import time
import json
import requests

#1 Grab a list of quotes to get from Yahoo
def get_ticker_info():
    apikey='l4gryeh0g19ETMNloNjZJ6MEVa0MP1qz8vVN5wJ3'
    ticker = input("Insert Ticker ")
    url = "https://yfapi.net/v6/finance/quote"
    querystring = {"symbols":ticker}
    headers = {
        'x-api-key': apikey
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    try:
        stock_json = response.json()
        mkt_time = stock_json['quoteResponse']['result'][0]["regularMarketTime"]
        info = (stock_json['quoteResponse']['result'][0]["shortName"] + ", " + time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime(mkt_time))+ ", " + str(stock_json['quoteResponse']['result'][0]["regularMarketPrice"]))
        print(info)
        field_names = ["symbol","RegularMarketTime","regularMarketPrice"]
        dict={'symbol': str(stock_json['quoteResponse']['result'][0]["symbol"]), "RegularMarketTime": time.strftime("%Y-%m-%d %H:%M:%S",time.gmtime(mkt_time)), "regularMarketPrice": str(stock_json['quoteResponse']['result'][0]["regularMarketPrice"])}
        with open('tickers.csv', 'a') as f_object:
            dictwriter_object = DictWriter(f_object, fieldnames = field_names)
            dictwriter_object.writerow(dict)
            f_object.close()
    except:
        print("Erroneous Ticker")
      
get_ticker_info()

