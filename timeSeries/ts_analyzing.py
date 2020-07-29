#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@author: Xiao Huang

# 时间序列分析

import matplotlib.pyplot as plt
from pylab import mpl

from timeSeries import get_stock_data
from timeSeries import pre_check
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

#导入数据
input = get_stock_data.get_stock_data("sh.000001", '2010-01-01', '2020-07-27', frequency='D', saving=0)
output = get_stock_data.add_ts_diff(input)
ts = output['ts_diff']
ts=ts.dropna()

if __name__ == "__main__":
    # 作图观察
    pre_check.tsplot(ts, lags=30)

    # adf 单位根检验
    print('-----------------------ADF--TEST-------------------------------\n')
    adf_res = pre_check.adf_test(ts)

    # ACF PACF输出
    print('-----------------------ACF--PACF--------------------------------\n')
    acf_and_pacf = pre_check.acf_and_pacf(ts, 30)

    # AIC 信息准则定阶
    print('-----------------------ADF--AIC---------------------------------\n')
    adf_aic = pre_check.adf_aic(ts)









