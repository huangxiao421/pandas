#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@author: Xiao Huang

# 时间序列分析

import matplotlib.pyplot as plt
from pylab import mpl

from timeSeries import get_stock_data
from timeSeries import pre_check

#导入数据
input = get_stock_data.get_stock_data("sh.000001", '2010-01-01', '2020-07-27', frequency='D', saving=0)
output = get_stock_data.add_ts_diff(input)
ts = output.ts_diff


#作图观察
pre_check.tsplot(ts,lags=30)












