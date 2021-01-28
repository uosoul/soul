import os
import time
import random
from concurrent.futures import ProcessPoolExecutor
from dj_update_agent.tool_code import *

# get_cpu,get_meminfo,get_space

# 设置主机列表
host_list = ({'ip': '47.93.1.155', 'port': 22, 'username': 'root', 'password': 'Dyanalysis@abc456'},
             {'ip': '47.111.182.11', 'port': 22, 'username': 'root', 'password': 'Dyanalysis@abc456'},
             {'ip': '192.168.2.9', 'port': 22, 'username': 'tangy', 'password': '111111'})

lst = [['ip', '当前CPU使用率', "MemTotal", 'MemAvailable', '内存使用率', 'Filesystem', 'Used', 'Avail', '磁盘占用率']]


def f1(host):
    lst1 = []
    tmp = []
    tmp.append(host['ip'])
    cpu_use = get_cpu(host)
    tmp.append(cpu_use)
    MemTotal, MemAvailable, nei_use = get_meminfo(host)
    nei_use = str(round(float(nei_use) * 100,3)) + '%'
    for i in MemTotal, MemAvailable, nei_use:
        tmp.append(i)
    # print(cpu_use, MemTotal, MemAvailable, nei_use)
    space = get_space(host)  # [['/dev/sda4', '938G', '874G', '2%'], ['/dev/sda5', '6.3T', '4.3T', '28%']]
    print(space)
    if len(space) == 1:
        [tmp.append(s) for s in space[0]]
        lst1.append(tmp)
    else:  # 第一个信息的都得显示
        [tmp.append(s) for s in space[0]]
        lst1.append(tmp)
        for g in space[1:]:  # 第一个之后前面的不用重复显示了
            two = [' ' for m in range(4)]
            two.insert(0, host['ip'])
            two.extend(g)
            lst1.append(two)
    return lst1

if __name__ == '__main__':
    executor = ProcessPoolExecutor(max_workers=3)

    futures = []
    for host in host_list:
        future = executor.submit(f1, host)
        futures.append(future)
    executor.shutdown(True)
    for future in futures:
        lst.append(future.result())
        print(future.result())
    print(lst)

