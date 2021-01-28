import csv
import os, sys
from collections import Counter
import matplotlib.pyplot as plt
import os
import numpy as np


# 从csv中得到线索。如：['76577997294', '99955505934']
def get_clue(csv_name):
    lst = []
    with open(csv_name, 'r')as af:
        datas = af.readlines()
        for i in datas:
            lst.append(i.strip())
    return lst


# 求出总人数，包括重复的
def f_sum(csv_dir_new):
    sum1 = 0
    for i in csv_dir_new:
        count = int(i.split('_')[0])
        sum1 += count
    return sum1


# 取到所有不重复的线索，存在clue_all
def get_no_repeat(csv_dir_new):
    # 集合删除指定元素的方法，clue_all.discard('xxx')
    clue_all = set()
    one_kind_csvs = os.listdir(os.path.join(csv_begin, kind))
    for onecsv in one_kind_csvs:
        path = os.path.join(os.path.join(csv_begin, kind), onecsv)  # csv的文件目录
        with open(path, 'r')as rf:
            datas = rf.readlines()  # ['76057340686\n', '3056167845\n']
            [clue_all.add(i.strip()) for i in datas]
    print(f'不重复的线索为：{len(clue_all)}')
    return clue_all


# dic_price ={'猴哥说车':500000}
def get_dic_price1(kind):
    # 小小岩哥, '20-60s视频': 25000/n
    with open(f'./all_price_txt/{kind}.txt', 'r', encoding='ISO-8859-1')as rf:
        dic_price = {}
        datas = rf.readlines()
        for i in datas:
            data = i.encode('ISO-8859-1').decode()
            name = data.split(',')[0]
            price = int(data.split(',')[-1].strip().split(':')[-1])
            dic_price[name] = price

    return dic_price

# {'93763913776': 400000, '104332721863': 350000,}
def get_dic_price(kind):
    with open(f'./all_price_txt/{kind}.txt', 'r', encoding='ISO-8859-1')as rf:
        dic_price = {}
        datas = rf.readlines()
        for data in datas:
            uid = data.split(',')[0]
            price = int(data.split(',')[-1].strip())
            dic_price[uid] = price

    return dic_price


# 算出第一轮占比，如：lst1 -> 107_猴哥说车  107,
def main(kind, clue_all):
    # 一个类别的路径，方便读取该类别下的CSV文件，D:\workspace\marketing\all_kinds\tesla_all
    one_kind_path = os.path.join(csv_begin, kind)
    # 一个类别下所有的CSV文件，['1.csv', '2.csv']
    one_kind_csvs = os.listdir(one_kind_path)

    result = {}
    people_lst = []
    price_lst = []
    people_all = len(clue_all)
    # 价格字典 uid:price
    dic_price = get_dic_price(kind)  # {'93763913776': 400000, '104332721863': 350000,}

    while len(one_kind_csvs) != 0:
        tmp2= []
        tmp = { }
        for cvname in one_kind_csvs:
            csv_name = os.path.join(one_kind_path, cvname)  # 完整的CSV路径
            lst = get_clue(csv_name)
            for j in lst:
                if j in clue_all:
                    # 如果出现，tmp记录一次
                    try:
                        tmp[cvname] += 1
                    except:
                        tmp[cvname] = 1
        # 循环结束一轮，找到这一轮最多次数的线索并记录。
        # res = sorted(tmp.items(), key=lambda x: x[1])  # ('107_猴哥说车.csv': 107, '106_虎哥说车.csv'})

        # 算出性价比
        for rs in tmp:
            name2 = rs.split('_')[-1].split('.')[0]     # 猴哥说车
            price2 = dic_price[name2]   # 价格
            cout2 = tmp[rs]     # 出现的次数
            price_count = round(price2/cout2, 3)
            tmp2.append((rs, price_count))
        # 对这一轮的性价比排序，取最小的
        tmp22 = sorted(tmp2, key=lambda x: x[1])  # [('b', 1), ('a', 2)] 得到从小到大排序的列表
        # tmp[tmp22[0][0]]次数    tmp22[0][0].split('_')[-1].split('.')[0] 价格
        cout3 = tmp[tmp22[0][0]]
        price3 = dic_price[tmp22[0][0].split('_')[-1].split('.')[0]]
        result[tmp22[0][0]] = (cout3, price3)   # 猴哥说车：6000
        pre_people = people_lst[-1] if people_lst else 0
        pre_price = price_lst[-1] if price_lst else 0
        price_lst.append(pre_price+price3)
        people_lst.append(pre_people+cout3)

        # 然后剔除，这一轮最大的csv中的线索
        name3 = tmp22[0][0]
        csv_n = os.path.join(one_kind_path, name3)
        num_one = set(get_clue(csv_n))
        [clue_all.discard(i) for i in num_one]
        # 也在循环的列表中将csv删除
        one_kind_csvs.remove(name3)
        if len(clue_all) == 0:
            break
    # people_lst = [round((i/people_all),3) for i in people_lst]
    with open(f'price_ratio_csv/{kind}_price_first.csv', 'w', newline='', encoding='utf-8')as f:
            writer = csv.writer(f)
            writer.writerow(('uuid', '覆盖目标用户比例', '预算'))
            for uuid, ratio, money in zip(result, people_lst, price_lst):
                writer.writerow((uuid, ratio, money))

    return result, price_lst, people_lst


if __name__ == '__main__':
    # csv_begin = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'all_kinds')
    # csv_begin = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'second_experiment')
    csv_begin = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'third_experiment')
    # 获取到所有的类别,tesla_all
    csv_all_kinds = os.listdir(csv_begin)  # ['tesla_all']
    print(csv_all_kinds)
    # sys.exit()
    for kind in csv_all_kinds:
        clue_all = get_no_repeat(kind)
        print(len(clue_all))
        result, price_lst, people_lst = main(kind, clue_all)
        print(result)
        print(price_lst)
        print(people_lst)
# 第二轮，
