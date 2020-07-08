#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Xiao Huang

import matplotlib.pyplot as plt
import numpy as np


# 生成一个时间序列，n 为长度，start 为起始项， factor 为参数阿尔法
def generate_sequence(n,start,factor):
    rd = np.random.normal(loc=0.0, scale=1.0, size=n)  # 生成一个标准正态分布序列,长度为N
    sequence = np.zeros(n, dtype=float)  # 生成一个全为0，长度为N的array
    sequence[0] = start
    i = 1
    while i < n:
        sequence[i] = factor * sequence[i - 1] + rd[i]
        i = i + 1
    # print(rd)
    # print(sequence)
    return sequence

if __name__=='__main__':
    s1 = generate_sequence(100,0,-0.2)
    print(s1)
    plt.plot(s1)
    plt.show()


