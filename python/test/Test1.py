# coding=gbk
import pandas as pd
import re

import xlwt
from xlrd import *
from datetime import datetime
# ��ҵ�������
industry_max = 5
# 1.������
df = pd.read_excel('G:\Python����\Python����.xlsx')
# 2.1data clean
# 2.2ͳ������
dic_all = {}
# 3.��������
# �������õ�����
lines = df.iloc[3:]
len_lines = len(lines)
for i in range(len_lines):
    #����ÿһ��
    line = lines.iloc[i]
    # ����
    nation = line[1]
    # ��ҵ
    industry = str(line[2])
    # �������ݹ��� ��
    if industry != "nan":
        # ������ʽȥ������
        industry = re.sub(r"[0-9]+", "", industry)
#         print("����:%s,��ҵ:%s"%(nation,industry))
        if(dic_all.__contains__(nation)):
            dic_nation = dic_all[nation]
            # �����Ӧ�Ĵ�������
            count = dic_nation["count"]
            # ����count
            dic_nation["count"] = count + 1
            # �����Ӧ����ҵ
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
# DataFrame��Ҫ��list
list_df = []

dic_all_sort = sorted(dic_all.items(), key=lambda item:item[1]["count"])
# print(dic_all_sort)
# ת�ٷֱ�
for item in dic_all_sort:
    nation = item[0]
    dic_nation = item[1]
    # ��������
    count = dic_nation["count"]
    # ������ҵ����
    dic_industry = dic_nation["industry"]
    # ����
    dic_industry = sorted(dic_industry.items(), key=lambda item:item[1], reverse=True)
#     print(dic_industry)
    industry_top5 = ""
    number = 0
    for item in dic_industry:
        number += 1
        if(number > 5):
            break
        # ��ҵ��
        key = item[0]
        # ��ҵ������
        value = item[1]
        industry_top5 = industry_top5 + key + "(" + str("%.2f%%" % (value / count * 100)) + ")��"
    list_df.append([nation, industry_top5[:-1], count])
    
#     for key, value in dic_industry.items():
#         a = a + 1
#         
#         print(key)
#         print(value)
#         dic_industry[key] = "%.2f%%" % (value / count * 100)
    
# print(dic_all)

writer = pd.ExcelWriter(r'G:\Python����\1_python����_out.xlsx')
# columns������
df = pd.DataFrame(list_df, columns=['�������� ', '����222����', '��ҵ����'])
# df = pd.DataFrame(list_df)
# ExcelWriter����,sheet��,index�Ƿ���Ҫ����
# �ֶ������ȼ��� excel_header�ֶ��������ȼ���
excel_header = ['��������', '��ҵ����', '�������� ']
# header=excel_header
# df.to_excel(writer, sheet_name='��������ҵͳ��', header=excel_header, index=True)#index�Ƿ���Ҫ������true�����У�flase����ȥ��
df.to_excel(writer, sheet_name='��������ҵͳ��', index=True)  # ��̧ͷΪ����222����
writer.save()

# dic = {}
# print("%s:%s"%("dic",dic))
# zus = ["����", "����", "����", "����", "����"]
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
