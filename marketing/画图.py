import os,sys
import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np


def f1():
    text = "'20-60s视频': 10000\n"
    length = len("霸王花侃车,'1-20s视频': 1000,")
    with open('price1.txt', 'r', encoding='ISO-8859-1')as f:
        datas = f.readlines()
        with open('all_price_txt/tesla_all.txt', 'a+', encoding='utf-8')as af:
            for i in datas:
                data = i.encode('ISO-8859-1').decode()
                if len(data) > length:
                    lst = data.split(',')
                    new_data = ','.join([lst[0], lst[-1]])
                    af.write(new_data)
                else:
                    af.write(data.strip()+text)

def f2():
    # 小小岩哥, '20-60s视频': 25000/n
    with open('all_price_txt/tesla_all.txt', 'r', encoding='ISO-8859-1')as rf:
        dic_price = {}
        datas = rf.readlines()
        for i in datas:
            data = i.encode('ISO-8859-1').decode()
            name = data.split(',')[0]
            price = int(data.split(',')[-1].strip().split(':')[-1])
            dic_price[name] = price

    return dic_price


def f3():
    # 小小岩哥, '20-60s视频': 25000/n
    with open('all_price_txt/tesla_all.txt', 'r', encoding='ISO-8859-1')as rf:
        dic_price = {}
        datas = rf.readlines()
        for i in datas:
            data = i.encode('ISO-8859-1').decode()
            name = data.split(',')[0]
            price = int(data.split(',')[-1].strip().split(':')[-1])
            dic_price[name] = price

    return dic_price



def plot_price_first(people, prices, kind):
    name1 = f'./性价比优先图/{kind}覆盖用户比例'
    name2 = f'./性价比优先图/{kind}预算'
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    print(len(people), len(prices))

    fig, ax = plt.subplots(1, 1)
    ax.plot(np.arange(len(people)), people, label='111')
    ax.set_title('KOL数量与覆盖目标用户比例关系')
    ax.set_xlabel('选择的KOL数量')
    ax.set_ylabel('覆盖目标用户比例')
    fig.savefig(name1, dpi=300)

    fig, ax = plt.subplots(1, 1)
    ax.plot(np.arange(len(prices)), prices, label='111')
    ax.set_title('KOL数量和预算的关系')
    ax.set_xlabel('选择的KOL数量')
    ax.set_ylabel('所花费总金额 ')
    fig.savefig(name2, dpi=300)

def plot_cover_num_first(people, prices, kind):
    name1 = f'./覆盖用户优先图/{kind}覆盖用户比例.png'
    name2 = f'./覆盖用户优先图/{kind}预算.png'

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    print(len(prices), len(people))

    fig, ax = plt.subplots(1, 1)
    ax.plot(np.arange(len(people)), people, label='111')
    ax.set_title('KOL数量与覆盖目标用户比例关系')
    ax.set_xlabel('选择的KOL数量')
    ax.set_ylabel('覆盖目标用户比例 ')
    fig.savefig(name1, dpi=300)

    fig, ax = plt.subplots(1, 1)
    ax.plot(np.arange(len(prices)), prices, label='111')
    ax.set_title('KOL数量和预算的关系')
    ax.set_xlabel('选择的KOL数量')
    ax.set_ylabel('所花费总金额 ')
    fig.savefig(name2, dpi=300)
def num_first():
    dir_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cover_user_csv')
    csv_all = os.listdir(dir_name)

    for cv in csv_all:
        path = os.path.join(dir_name, cv)
        # print(path,cv)
        kind = cv.split('_')[0]

        df = pd.read_csv(path)
        # print(df['覆盖目标用户比例'], df['预算'])
        plot_cover_num_first(df['覆盖目标用户比例'], df['预算'], kind=kind)
def price_first():
    dir_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'price_ratio_csv')
    csv_all = os.listdir(dir_name)

    for cv in csv_all:
        path = os.path.join(dir_name, cv)
        # print(path,cv)
        kind = cv.split('_')[0]

        df = pd.read_csv(path)
        # print(df['覆盖目标用户比例'], df['预算'])
        plot_price_first(df['覆盖目标用户比例'], df['预算'], kind=kind)

if __name__ == '__main__':
    num_first()
    price_first()


