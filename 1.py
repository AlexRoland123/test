#!/usr/bin/env python
# coding: utf-8

# In[4]:


import re
import pandas as pd
import matplotlib.pyplot as plt

def count_valid_id_numbers(file_path):
    pattern = r'^[1-8][0-7](19\d{2}|20\d{2})(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])\d{11}[0-9Xx]$'
    count = 0

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if re.match(pattern, line):
                count += 1

    return count



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


def count_specific_id_numbers(file_path):
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

file_path = r'D:\IDNumbers.txt'
sd_male, hn_male, gd_female, sc_female = count_specific_id_numbers(file_path)

# 创建数据框
data = {
    '地区': ['山东', '河南', '广东', '四川'],
    '男性数量': [sd_male, hn_male, 0, 0],
    '女性数量': [0, 0, gd_female, sc_female]
}
df = pd.DataFrame(data)

# 计算百分比
df['男性百分比'] = df['男性数量'] / df['男性数量'].sum() * 100
df['女性百分比'] = df['女性数量'] / df['女性数量'].sum() * 100

# 绘制饼状图
fig, ax = plt.subplots()
ax.axis('equal')
ax.pie(df['男性百分比'], labels=df['地区'], autopct='%1.1f%%', startangle=90)
ax.set_title('不同地区男性ID号码比例')
plt.show()

fig, ax = plt.subplots()
ax.axis('equal')
ax.pie(df['女性百分比'], labels=df['地区'], autopct='%1.1f%%', startangle=90)
ax.set_title('不同地区女性ID号码比例')
plt.show()

file_path = r'D:\IDNumbers.txt'
sd_male, hn_male, gd_female, sc_female = find_specific_id_numbers(file_path)


file_path = r'D:\IDNumbers.txt'
total_count = count_valid_id_numbers(file_path)
print("符合条件的号码总数：", total_count)

print("山东男性的ID号码数量：", sd_male)
print("河南男性的ID号码数量：", hn_male)
print("广东女性的ID号码数量：", gd_female)
print("四川女性的ID号码数量：", sc_female)


# In[ ]:




