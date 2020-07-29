#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Xiao Huang
from pprint import pprint

import pysnooper
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 时间序列平稳性检验
import scipy.stats as scs
import statsmodels.api as sm
import statsmodels.tsa.api as smt


# @pysnooper.snoop()
# 打印之后lags阶数的ACF,PACF
def tsplot(y, lags=None, figsize=(10, 8), style='bmh'):
    if not isinstance(y, pd.Series):
        y = pd.Series(y)
    with plt.style.context(style):  # 定义局部样式
        fig = plt.figure(figsize=figsize)  # 生成fig
        layout = (4, 2)  # 配置layout
        ts_ax = plt.subplot2grid(layout, (0, 0), colspan=2)
        hist_ax = plt.subplot2grid(layout, (3, 0))
        acf_ax = plt.subplot2grid(layout, (1, 0))
        pacf_ax = plt.subplot2grid(layout, (1, 1))
        qq_ax = plt.subplot2grid(layout, (2, 0))
        pp_ax = plt.subplot2grid(layout, (2, 1))

        y.plot(ax=ts_ax)
        ts_ax.set_title('Time Series Analysis Plots')
        y.plot(ax=hist_ax, kind='hist', bins=25)
        hist_ax.set_title('Histogram')
        smt.graphics.plot_acf(y, lags=lags, ax=acf_ax, alpha=0.5)  # 自相关系数ACF图
        smt.graphics.plot_pacf(y, lags=lags, ax=pacf_ax, alpha=0.5)  # 偏相关系数PACF图
        sm.qqplot(y, line='s', ax=qq_ax)  # QQ图检验是否是正太分布
        qq_ax.set_title('QQ Plot')
        scs.probplot(y, sparams=(y.mean(), y.std()), plot=pp_ax)

        plt.tight_layout()
        # plt.savefig('c:/apache/test.png')
        plt.show()


# 打印ACF,PACF 及lags阶数的Q值，P-value
def acf_and_pacf(y, lags=None):
    acf, q, p = sm.tsa.acf(y, nlags=lags, qstat=True, fft=True)  # 计算10个lag的自相关系数 及p-value
    pacf = sm.tsa.pacf(y, nlags=lags)
    out = np.c_[range(1, lags + 1), acf[1:], pacf[1:], q, p]
    output = pd.DataFrame(out, columns=['lag', "ACF", "PACF", "Q", "P-value"])
    output = output.set_index('lag')
    return output


def adf_test(ts):
    adftest = sm.tsa.adfuller(ts)
    adf_res = pd.Series(adftest[0:4], index=['Test Statistic', 'p-value', 'Lags Used', 'Number of Observations Used'])
    for key, value in adftest[4].items():
        adf_res['Critical Value (%s)' % key] = value
    return adf_res


if __name__ == "__main__":
    data = pd.read_csv("c:/apache/daily-minimum-temperatures-in-me.csv", index_col='Date')
    temp = data['temperatures']
    acf_and_pacf = acf_and_pacf(temp, lags=30)
    adf_res = adf_test(temp)
    print("ACF----PACF----------")
    print(acf_and_pacf)
    print("ADF-RESULT----------")
    print(adf_res)
    tsplot(temp, lags=30)
