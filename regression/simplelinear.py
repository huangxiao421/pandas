#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@author: Xiao Huang

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pylab import mpl
import statsmodels.api as sm
import statsmodels.formula.api as smf


cyb = pd.read_csv('C:/apache/StockMarket/cyb.csv',usecols=["date", "close",'pctChg'])
szzs = pd.read_csv('C:/apache/StockMarket/szzs.csv',usecols=["date", "close",'pctChg'])
df = pd.merge(left=cyb,right=szzs,how='inner',on='date', suffixes=['_cyb','_szzs'])
print(df.describe())

# 防止图形中文文字乱码
mpl.rcParams['font.sans-serif'] = ['SimHei']   # 以黑体的字体显示中文
mpl.rcParams['axes.unicode_minus'] = False   # 解决保存图像是负号'-'显示为方块的问题

# #走势图
# plt.figure(figsize=(9,6))   # 设置图形大小
# plt.title('两指数走势图', fontsize=14)   # 标题，fontsize 为字体大小
# # 常见线的属性有：color, label, linewidth, linestyle, marker 等
# #plt.plot(df['date'], df['pctChg_cyb'], color='blue', label='创业板指数')
# plt.plot(df['date'], df['pctChg_szzs'], color='red', label='上证指数')
# plt.legend(fontsize=14)  # 显示上面的 label
# plt.xticks(fontsize=14)  # x轴文字设置
# plt.yticks(fontsize=14)
# plt.xlabel('日期', fontsize=14)
# plt.ylabel('指数值', fontsize=14)
# # plt.axis([0, 2*np.pi, -1, 1])   #设置坐标范围 axis([xmin,xmax,ymin,ymax])
# # plt.ylim(-1,1)   #仅设置 y 轴坐标范围
# plt.show()

# #散点图
# plt.figure(figsize=(9,6))
# plt.scatter(x=df['pctChg_cyb'], y=df['pctChg_szzs'], c='b', marker='o')
# plt.xticks(fontsize=14)
# plt.yticks(fontsize=14)
# plt.title('两指数散点图', fontsize=14)
# plt.xlabel('创业板收益率', fontsize=14)
# plt.ylabel('上证指数收益率', fontsize=14)
# plt.show()

# #随机变量分布 密度图
# plt.figure(figsize=(9,6), dpi=80)
# sns.kdeplot(df['pctChg_cyb'], shade=True, color="r", label="CYB", alpha=.7)
# # Decoration
# plt.title('Density Plot of daily return of cyb', fontsize=22)
# plt.legend()
# plt.show()

#应用smf.ols进行最小二乘法回归，formula为模型公式，data为准备好的数据
result = smf.ols(formula = 'pctChg_cyb~pctChg_szzs',data = df[['date','pctChg_cyb','pctChg_szzs']]).fit()
print(result.summary())