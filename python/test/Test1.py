# coding=gbk
import pandas as pd
import re

import xlwt
from xlrd import *
from datetime import datetime
# 行业最大数量
industry_max = 5
# 1.读数据
df = pd.read_excel('G:\Python试题\Python试题.xlsx')
# 2.1data clean
# 2.2统计数据
dic_all = {}
# 3.保存数据
# 保留有用的数据
lines = df.iloc[3:]
len_lines = len(lines)
for i in range(len_lines):
    #遍历每一行
    line = lines.iloc[i]
    # 民族
    nation = line[1]
    # 行业
    industry = str(line[2])
    # 垃圾数据过滤 空
    if industry != "nan":
        # 正则表达式去掉数字
        industry = re.sub(r"[0-9]+", "", industry)
#         print("民族:%s,行业:%s"%(nation,industry))
        if(dic_all.__contains__(nation)):
            dic_nation = dic_all[nation]
            # 民族对应的答题人数
            count = dic_nation["count"]
            # 更新count
            dic_nation["count"] = count + 1
            # 民族对应的行业
            dic_industry = dic_nation["industry"]
            if dic_industry.__contains__(industry):
                dic_industry[industry] = dic_industry[industry] + 1
            else:
                dic_industry[industry] = 1
        else:
            dic_industry = {industry:1}
            dic = {"count":1, "industry":dic_industry}
            dic_all[nation] = dic

# print(dic_all)
# DataFrame需要的list
list_df = []

dic_all_sort = sorted(dic_all.items(), key=lambda item:item[1]["count"])
# print(dic_all_sort)
# 转百分比
for item in dic_all_sort:
    nation = item[0]
    dic_nation = item[1]
    # 答题人数
    count = dic_nation["count"]
    # 各个行业人数
    dic_industry = dic_nation["industry"]
    # 排序
    dic_industry = sorted(dic_industry.items(), key=lambda item:item[1], reverse=True)
#     print(dic_industry)
    industry_top5 = ""
    number = 0
    for item in dic_industry:
        number += 1
        if(number > 5):
            break
        # 行业名
        key = item[0]
        # 行业的数量
        value = item[1]
        industry_top5 = industry_top5 + key + "(" + str("%.2f%%" % (value / count * 100)) + ")、"
    list_df.append([nation, industry_top5[:-1], count])
    
#     for key, value in dic_industry.items():
#         a = a + 1
#         
#         print(key)
#         print(value)
#         dic_industry[key] = "%.2f%%" % (value / count * 100)
    
# print(dic_all)

writer = pd.ExcelWriter(r'G:\Python试题\1_python试题_out.xlsx')
# columns是列名
df = pd.DataFrame(list_df, columns=['答题人数 ', '民族222名称', '行业门类'])
# df = pd.DataFrame(list_df)
# ExcelWriter对象,sheet名,index是否需要索引
# 字段名优先级高 excel_header字段名字优先级高
excel_header = ['民族名称', '行业门类', '答题人数 ']
# header=excel_header
# df.to_excel(writer, sheet_name='民族内行业统计', header=excel_header, index=True)#index是否需要索引，true代表有，flase代表去掉
df.to_excel(writer, sheet_name='民族内行业统计', index=True)  # 表抬头为民族222名称
writer.save()

# dic = {}
# print("%s:%s"%("dic",dic))
# zus = ["汉族", "苗族", "回族", "苗族", "苗族"]
# # print(len(zus))
# for i in range(len(zus)):
#     print("%s%d%s"%("-",i,"--------------------------"))
#     zu = zus[i]
#     print("%d:%s" % (i, zu))
#     if(dic.__contains__(zu)):
#         count = dic[zu]
#         print("%s%s:%d" % ("dic",zu, count))
#         dic[zu] = count + 1
#         print("%s%s:%d" % ("dic",zu,  dic[zu]))
#     else:
#         dic[zu] = 1
#         print("%s:%s"%("dic",dic))
# print(dic)
