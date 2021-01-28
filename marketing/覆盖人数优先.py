import csv
import os, sys
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 从csv中得到线索。如：['76577997294', '99955505934']
def get_clue(csv_name):
    lst = []
    with open(csv_name, 'r')as af:
        datas = af.readlines()
        for i in datas:
            lst.append(i.strip())
    return lst


# 求出总人数，包括重复的
def f0(csv_dir_new):
    sum1 = 0
    for i in csv_dir_new:
        count = int(i.split('_')[0])
        sum1 += count
    return sum1


# 取到所有不重复的线索，存在clue_all
def get_no_repeat(kind):
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


# dic_price ={'猴哥说车':500000}，获取一个类别中，每个达人对应的价格信息。
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

    people_all = len(clue_all)
    result = {}
    people_lst = []     #
    price_lst = []
    dic_price = get_dic_price(kind)    # {林哥撩车:30000,··· }

    while len(one_kind_csvs) != 0:
        tmp = {}
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
        res = sorted(tmp.items(), key=lambda x: x[1], reverse=True)   # [('22_学好姐姐😍', 5), ('11_学好姐姐😍', 6)]
        name, cout = res[0]
        result[name] = cout  # 通过字典记录，当前轮最多的的线索的CSV名字和次数
        name1 = name.split('_')[-1].split('.')[0]
        price1 = dic_price[name1]
        pre_price = price_lst[-1] if price_lst else 0

        price_lst.append(pre_price + price1)

        pre_people = people_lst[-1] if people_lst else 0
        # print(pre_people, cout, type(pre_people), type(cout))
        people_lst.append(pre_people+cout)
        # print(people_lst)

        # 然后剔除，这一轮最大的csv中的线索
        csv_n = os.path.join(one_kind_path, name)
        num_one = set(get_clue(csv_n))
        [clue_all.discard(i) for i in num_one]

        # 也在循环的列表中将csv删除
        one_kind_csvs.remove(name)
        if len(clue_all) == 0:
            break

    # people_lst = [round((i/people_all), 3) for i in people_lst]
    with open(f'cover_user_csv/{kind}_cover_num_first.csv', 'w', newline='', encoding='utf-8')as f:
            writer = csv.writer(f)
            writer.writerow(('uuid', '覆盖目标用户比例', '预算'))
            for uuid, ratio, money in zip(result, people_lst, price_lst):
                writer.writerow((uuid, ratio, money))

    return result, price_lst, people_lst


def select_res_csv(num):
    df = pd.read_csv('./price_ratio_csv/tesla_all_price_first.csv')
    no_need = [i for i in df['uuid'][:36]]
    all_one_kind = os.listdir('./all_kinds/tesla_all')
    lst = [i for i in all_one_kind if i not in no_need]

    for csv_file in lst:
        with open(f'./all_kinds/tesla_all/{csv_file}', 'r')as rf:
            reader = csv.reader(rf)  # reader是生成器，可迭代的
            with open(f'./second_experiment/tesla_all/{csv_file}', 'w', newline='')as f:
                writer = csv.writer(f)
                for i in reader:
                    writer.writerow(i)


if __name__ == '__main__':
    csv_begin = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'all_kinds')
    # 获取到所有的类别,tesla_all
    csv_all_kinds = os.listdir(csv_begin)  # ['101_君卡好车.csv','10_DH大海说进口车.csv']

    print(csv_all_kinds)
    # sys.exit()
    for kind in csv_all_kinds:
        # 获取该类别下所有不重复的用户
        clue_all = get_no_repeat(kind)
        result, price_lst, people_lst = main(kind, clue_all)
        print(len(result), len(price_lst))
        print(price_lst)
        print(people_lst)
# 第二轮，
