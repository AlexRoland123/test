import re
import pandas

'''
从文件中读取内容
'''
def read_numbers(path_file):
    with open(path_file, "r", encoding="utf-8") as fin:
        return " ".join(fin.readlines())

'''
从指定的文件中找到符合条件的号码
a.第一位数字是在【1-8】之间
b.第二位数字是在【0-7】之间
c.出生年在1900-1999之间
d.月份在01-09之间
e.假设每个月都可以有31天
f.最后一位是一个数字或者X/x
g.ID号码总共有18位
'''
def get_id_numbers(fin):
    str_nums = read_numbers(fin)
    # print(str_nums)
    pattn_id = re.compile(r"([1-8][0-7]\d{4}19\d{2}0[1-9](([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx])")
    IDs = [ele if type(ele) == str else ele[0] for ele in re.findall(pattn_id, str_nums)]
    return IDs    

'''
找到山东男性、河南男性、广东女性和四川女性的ID号码
前两位中：37表示山东，41表示河南，44表示广东，20表示四川
第17位数字表示性别：奇数表示男性，偶数表示女性

'''
def province_nums(str_nums):
    pattn_sd_male = re.compile(r"37\d{7}[13579].")
    pattn_hn_male = re.compile(r"41\d{7}[13579].")
    pattn_gd_female = re.compile(r"44\d{7}[02468].")
    pattn_sc_female = re.compile(r"20\d{7}[02468].")
    ids_sd = re.findall(pattn_sd_male, str_nums)
    ids_hn = re.findall(pattn_hn_male, str_nums)
    ids_gd = re.findall(pattn_gd_female, str_nums)
    ids_sc = re.findall(pattn_sc_female, str_nums)
    
    return [ids_sd, ids_hn, ids_gd, ids_sc]

def draw_pie(ids_sd, ids_hn, ids_gd, ids_sc):
    counts_ids = [len(ids_sd), len(ids_hn), len(ids_gd), len(ids_sc)]
    print(counts_ids)
    counts_pd  =pandas.Series(counts_ids)
    import matplotlib.pyplot as plt
    names = ["shandong-m", "henan-m", "guangdong-f", "sichuan-f"]
    counts_pd.plot.pie(labels=names, autopct="%.0f%%", figsize=(10,10))
    plt.ylabel("phone number counts")
    plt.title("distribution of IDs from different provinces with different genders")
    plt.legend(names)
    plt.show()

def main():
    # create_phone_numbers("id_numbers.txt", 2000, 100)
    # step-1
    IDs = get_id_numbers("id_numbers.txt")
    print(len(IDs))
    # step-2
    # 将第一步中获取的ID号内容拼接后传递给第二步作为输入
    str_nums = "\n".join(IDs)
    IDs_province = province_nums(str_nums)
    # step-3 
    # 统计第二步中获得的数据，并以饼状图进行展示
    draw_pie(*IDs_province)  

if __name__ == '__main__':
    main()
