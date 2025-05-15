#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas as pd
import requests
import re
from pandas import Series
#a=pd.read_csv('d:IDNumbers.txt',encoding='ANSI')#导入后a就是一个DataFrame，直接操作即可,一行一行读入
#a.head(5)#打印前5行数据
file = r"d:IDNumbers.txt"
def find_specific_id_numbers(file_path):
    pattern_sd_male = r'^37\d{15}[13579]$'  # 山东男性
    pattern_hn_male = r'^41\d{15}[13579]$'  # 河南男性
    pattern_gd_female = r'^44\d{15}[02468]$'  # 广东女性
    pattern_sc_female = r'^20\d{15}[02468]$'  # 四川女性

    sd_male_count = 0
    hn_male_count = 0
    gd_female_count = 0
    sc_female_count = 0

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if re.match(pattern_sd_male, line):
                sd_male_count += 1
            elif re.match(pattern_hn_male, line):
                hn_male_count += 1
            elif re.match(pattern_gd_female, line):
                gd_female_count += 1
            elif re.match(pattern_sc_female, line):
                sc_female_count += 1

    return sd_male_count, hn_male_count, gd_female_count, sc_female_count
a=r'[1-8][0-7]\d\d\d\d[1][9]\d\d[0][^0]\d\d\d\d\d[Xx0-9]'
sd=r'37\d\d\d\d[1][9]\d\d[0][^0]\d\d\d\d\d[13579]'
hn=r'41\d\d\d\d[1][9]\d\d[0][^0]\d\d\d\d\d[13579]'
gd=r'44\d\d\d\d[1][9]\d\d[0][^0]\d\d\d\d\d[02468]'
sc=r'20\d\d\d\d[1][9]\d\d[0][^0]\d\d\d\d\d[02468]'
i=0
#a=r'[1-4]\d\d'
with open(file) as f:
    for line in f:
        if(re.match(a, line, flags=0)):
            i=i+1
            #print(line)
print("匹配人数：",i)
with open(file) as f:
    for line in f:
        if(re.match(sd, line, flags=0)):
            print("山东男:",line)
        elif(re.match(hn,line,flags=0)):
            print("河南男：",line)
        elif(re.match(gd,line,flags=0)):
            print("广东女：",line)
        elif(re.match(sc,line,flags=0)):
            print("四川女：",line)
sd_male, hn_male, gd_female, sc_female = count_specific_id_numbers(file)

# 创建数据框
data = {
    '地区': ['山东', '河南', '广东', '四川'],
    '男性数量': [sd_male, hn_male, 0, 0],
    '女性数量': [0, 0, gd_female, sc_female]
}
df = pd.DataFrame(data)


# In[ ]:




