#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@author: Xiao Huang

import numpy as np
import pandas as pd

df = pd.read_csv('C:/apache/SDW_CABLES.csv')
print(df.head())
#print(df.values)
print(type(df['VALIDFROM']))

print(df.VALIDFROM.index)
