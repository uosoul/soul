import csv
import os, sys
import pandas as pd

# 为了从该类别的KOL中，找到对应的价格生成tesla——price.txt文件，方便处理。
IO = './KOL.xlsx'
df = pd.read_excel(io=IO,)
# print(df['账号名称'].values, len(df['账号名称'].values))    # 汽车类别的一共110个
# sys.exit()
car_lst = df['账号名称'].values

# 从1500个csv中筛选出目标csv
def select_csv():
    with open('./all_price_txt/tesla_all.txt', 'r')as rf:

        all_uid = [ i.split(',')[0]+'.csv' for i in rf.readlines() ]
        print(all_uid)
    all_csv = os.listdir('./all_kinds/all_csv')
    for csv_file in all_csv:
        # csv_file --> 100_1516963116881684.csv
        filename = csv_file.split('_')[-1]      # 1516963116881684.csv
        if filename in all_uid:
            print(csv_file)
            print(filename)
            with open(f'./all_kinds/all_csv/{csv_file}', 'r')as rf:
                reader = csv.reader(rf)  # reader是生成器，可迭代的
                with open(f'./all_kinds/tesla_all/{filename}', 'w', newline='')as f:
                    writer = csv.writer(f)
                    for i in reader:
                        writer.writerow(i)



def get_price_txt(car_lst):
    lst = []
    with open("./all_price_txt/tesla_all.txt", 'a+')as af:
        with open('tesla_top1500.csv', 'r', encoding='utf-8')as rf:
            kinds = rf.readlines()
            for kind in kinds[1:]:
                kind_name = kind.split(',')[1]
                if kind_name in car_lst:
                    lst.append(kind_name)
                    af.write(kind)
    # 判断生成
    lst2 = [i for i in car_lst]
    print(len(lst), lst.index('鲁哥说车'), lst)
    print(len(lst2), lst2.index('鲁哥说车'), lst2)  # 我Y大王
    for i in lst:
        if i not in lst2:
            print(False,i)


def get_price_txt():
    lst = []
    n = 0
    with open('price2.txt','a+')as wf:
        with open("./all_price_txt/tesla_all.txt", 'r')as rf:
            datas = rf.readlines()
            for i in datas:
                if i.strip().endswith(','):
                    n += 1
                    uid = i.split(',')[0]
                    price = '90000'     # 平均价格为9W
                    wf.write(uid+','+price+'\n')
                else:
                    uid = i.split(',')[0]
                    price = i.split(',')[-2].split(':')[-1].strip()[:-1]
                    try:
                        lst.append(int(price))
                    except:
                        print(price)
                    wf.write(uid+','+price+'\n')
    print(f'平均价格为：{sum(lst)/len(lst)}')
    print(f'平均价格为：{len(lst)}',n)

def get_dic_price(kind):
    with open(f'./all_price_txt/{kind}.txt', 'r', encoding='ISO-8859-1')as rf:
        dic_price = {}
        datas = rf.readlines()
        for data in datas:
            uid = data.split(',')[0]
            price = int(data.split(',')[-1].strip())
            dic_price[uid] = price

    return dic_price

# 1-->30     2--->24    3--->26
def select_res_csv():
    df1 = pd.read_csv('./price_ratio_csv/tesla_all_price_first.csv')
    df2 = pd.read_csv('./price_ratio_csv/secondtesla_all_price_first.csv')
    df3 = pd.read_csv('./price_ratio_csv/thirdtesla_all_price_first.csv')
    no_need1 = [i for i in df1['uuid'][:34]]
    no_need2 = [i for i in df2['uuid'][:20]] + no_need1
    no_need3 = [i for i in df3['uuid'][:18]] + no_need2
    print(len(set(no_need3)))
    sys.exit()

    all_one_kind = os.listdir('./all_kinds/tesla_all')
    lst = [i for i in all_one_kind if i not in no_need2]

    for csv_file in lst:
        with open(f'./all_kinds/tesla_all/{csv_file}', 'r')as rf:
            reader = csv.reader(rf)  # reader是生成器，可迭代的
            # with open(f'./second_experiment/secondtesla_all/{csv_file}', 'w', newline='')as f:
            with open(f'./third_experiment/thirdtesla_all/{csv_file}', 'w', newline='')as f:
                writer = csv.writer(f)
                for i in reader:
                    writer.writerow(i)


if __name__ == '__main__':

    # a = get_dic_price('tesla_all')
    # print(len(a), a)
    # select_csv()
    select_res_csv()



