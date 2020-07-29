#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@author: Xiao Huang

import baostock as bs
import pandas as pd
import numpy as np

#format of code is "sh.000001" ,return dataframe
def get_stock_data(code,start_date,end_date,frequency,saving):

    #### 登陆系统 ####
    lg = bs.login()
    # 显示登陆返回信息
    print('login respond error_code:'+lg.error_code)
    print('login respond  error_msg:'+lg.error_msg)

    #### 获取沪深A股历史K线数据 ####
    # 详细指标参数，参见“历史行情指标参数”章节；“分钟线”参数与“日线”参数不同。
    # 分钟线指标：date,time,code,open,high,low,close,volume,amount,adjustflag
    rs = bs.query_history_k_data_plus(code,
        "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,isST",
        start_date=start_date, end_date=end_date,
        frequency=frequency, adjustflag="3")
    print('query_history_k_data_plus respond error_code:'+rs.error_code)
    print('query_history_k_data_plus respond  error_msg:'+rs.error_msg)

    #### 打印结果集 ####
    data_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())
    result = pd.DataFrame(data_list, columns=rs.fields)

    #### 结果集输出到csv文件 ####
    if saving == 1:
        result.to_csv("c:/apache/"+code+".csv", index=False)

    #### 登出系统 ####
    bs.logout()
    return result

# input为输入dataframe，包含colum ‘close’,通过此函数为input 增加一列对数收益率‘ts_diff’
def add_ts_diff(input):
    ts = input['close'].astype(float)
    ts_log = np.log(ts)
    ts_diff = ts_log.diff(1)
    ts_diff.dropna(inplace=True)
    input['ts_diff'] = ts_diff
    return input

