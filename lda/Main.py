# -*- coding: utf-8 -*- 
import numpy as np
import pandas as pd
import re

df = pd.read_csv("./input/HillaryEmails.csv")
print (df)
# print (df.iloc[1:10].pop)
# 原邮件数据中有很多Nan的值，直接扔了。
# df = df[['Id','ExtractedBodyText']]
# .dropna()
# print (df)
# print (df.dropna())