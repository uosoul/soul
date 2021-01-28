import csv, time
import os,sys

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker



# 使用scatter()绘制一系列点
# 使用scatter()绘制散点图并设置样式


def create_time_and_comment_count(create_time, comment_count, uid):
    # 显示中文标签
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 解决负号“-”显示为方块的问题
    plt.rcParams['axes.unicode_minus'] = False
    name1 = f'./comment_count/{uid}_时间-评论量的关系'
    x_values = create_time
    y_values = comment_count
    # fig, ax = plt.subplots(1, 1)
    fig = plt.figure(figsize=(30, 20))
    ax = fig.add_subplot(111)
    ax.scatter(x_values, y_values, s=50)
    # 设置图表标题并给坐标轴加上标签
    ax.set_title("时间-评论量的关系", fontsize=40)
    ax.set_xlabel("时间", fontsize=30)
    ax.set_ylabel("评论量", fontsize=30)
    # 设置刻度标记的大小
    ax.tick_params(axis='both', which='major', labelsize=20)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(4))
    fig.savefig(name1, dpi=300)



def create_time_and_digg_count(create_time, digg_count, uid):
    # 显示中文标签
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 解决负号“-”显示为方块的问题
    plt.rcParams['axes.unicode_minus'] = False
    name1 = f'./digg_count/{uid}_时间-点赞量的关系'
    x_values = create_time
    y_values = digg_count
    # fig, ax = plt.subplots(1, 1)
    fig = plt.figure(figsize=(30, 20))
    ax = fig.add_subplot(111)
    ax.scatter(x_values, y_values, s=50)
    # 设置图表标题并给坐标轴加上标签
    ax.set_title("时间-点赞量的关系", fontsize=40)
    ax.set_xlabel("时间", fontsize=30)
    ax.set_ylabel("点赞量", fontsize=30)
    # 设置刻度标记的大小
    ax.tick_params(axis='both', which='major', labelsize=20)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(4))
    fig.savefig(name1, dpi=300)



def create_time_and_share_count(create_time, share_count, uid):
    # 显示中文标签
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 解决负号“-”显示为方块的问题
    plt.rcParams['axes.unicode_minus'] = False
    name1 = f'./share_count/{uid}_时间-分享量的关系'
    x_values = create_time
    y_values = share_count
    # fig, ax = plt.subplots(1, 1)
    fig = plt.figure(figsize=(30, 20))
    ax = fig.add_subplot(111)
    ax.scatter(x_values, y_values, s=50)
    # 设置图表标题并给坐标轴加上标签
    ax.set_title("时间-分享量的关系", fontsize=40)
    ax.set_xlabel("时间", fontsize=30)
    ax.set_ylabel("分享量", fontsize=30)
    # 设置刻度标记的大小
    ax.tick_params(axis='both', which='major', labelsize=20)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(4))
    fig.savefig(name1, dpi=300)


def main():

    uids = os.listdir('./files')
    for uid in uids:
        try:
            # print(uid)
            # sys.exit()
            uid = uid.split('.')[0]
            df = pd.read_csv(f'./files/{uid}.csv', encoding='gb18030', engine='python')
            create_time = df['create_time'].values
            create_time = [time.localtime(i).tm_hour+(round(int(time.localtime(i).tm_min)/60, 2)) for i in create_time]
            comment_count = df['comment_count'].values
            digg_count = df['digg_count'].values
            share_count = df['share_count'].values

            create_time_and_comment_count(create_time, comment_count, uid)
            create_time_and_digg_count(create_time, digg_count, uid)
            create_time_and_share_count(create_time, share_count, uid)
        except:
            continue

if __name__ == '__main__':
    main()