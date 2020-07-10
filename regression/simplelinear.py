#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@author: Xiao Huang


import pandas as pd

cyb = pd.read_csv('C:/apache/StockMarket/cyb.csv',usecols=["date", "close"])
szzs = pd.read_csv('C:/apache/StockMarket/szzs.csv',usecols=["date", "close"])
df = pd.merge(left=cyb,right=szzs,how='inner',on='date', suffixes=['_cyb','_szzs'])
print(df.head(5))

