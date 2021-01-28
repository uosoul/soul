import paramiko
import re,sys
import time
# 设置主机列表
host_list = ({'ip': '47.93.1.155', 'port': 22, 'username': 'root', 'password': 'Dyanalysis@abc456'},
             {'ip': '47.111.182.11', 'port': 22, 'username': 'root', 'password': 'Dyanalysis@abc456'},
             {'ip': '192.168.2.9', 'port': 22, 'username': 'tangy', 'password': '111111'})


def get_cpu(host):
    ssh = paramiko.SSHClient()
    # 设置为接受不在known_hosts 列表的主机可以进行ssh连接
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


    ssh.connect(hostname=host['ip'], port=host['port'], username=host['username'], password=host['password'])
    # print(host['ip'])
    stdin, stdout, stderr = ssh.exec_command('cat /proc/stat | grep "cpu "')
    str_out = stdout.read().decode()
    str_err = stderr.read().decode()

    if str_err != "":
        print(str_err)

    else:
        cpu_time_list = re.findall('\d+', str_out)
        cpu_idle1 = cpu_time_list[3]
        total_cpu_time1 = 0
        for t in cpu_time_list:
            total_cpu_time1 = total_cpu_time1 + int(t)

    time.sleep(2)

    stdin, stdout, stderr = ssh.exec_command('cat /proc/stat | grep "cpu "')
    str_out = stdout.read().decode()
    str_err = stderr.read().decode()
    if str_err != "":
        print(str_err)

    else:
        cpu_time_list = re.findall('\d+', str_out)
        cpu_idle2 = cpu_time_list[3]
        total_cpu_time2 = 0
        for t in cpu_time_list:
            total_cpu_time2 = total_cpu_time2 + int(t)

    cpu_usage = round(1 - (float(cpu_idle2) - float(cpu_idle1)) / (total_cpu_time2 - total_cpu_time1), 2)

    print('当前CPU使用率为：' + str(cpu_usage))
    time.sleep(1)
    ssh.close()
    return str(cpu_usage)+'%'


def get_meminfo(host):
    ssh = paramiko.SSHClient()
    # 设置为接受不在known_hosts 列表的主机可以进行ssh连接
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


    ssh.connect(hostname=host['ip'], port=host['port'], username=host['username'], password=host['password'])
    #print(host['ip'])
    stdin, stdout, stderr = ssh.exec_command('cat /proc/meminfo')
    str_out = stdout.read().decode()
    str_err = stderr.read().decode()

    if str_err != "":
        print(str_err)

    else:
        str_total = re.search('MemTotal:.*?\n', str_out).group()
        # print(str_total.strip())
        totalmem = re.search('\d+', str_total).group()
        # print(totalmem,type(totalmem))
        str_free = re.search('MemAvailable:.*?\n', str_out).group()
        # print(str_free.strip())
        freemem = re.search('\d+', str_free).group()
        use = round(float(freemem) / float(totalmem), 3)
        # print('当前内存使用率为：' + str(round((1 - use), 3)))

        time.sleep(1)
        ssh.close()
        totalmem = float(round(int(totalmem)/1048576, 3))
        freemem = float(round(int(freemem)/1048576, 3))
        nei_use = str(round((1 - use), 3))
        return totalmem, freemem, nei_use
def get_space(host):
    ssh = paramiko.SSHClient()
    # 设置为接受不在known_hosts 列表的主机可以进行ssh连接
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


    ssh.connect(hostname=host['ip'], port=host['port'], username=host['username'], password=host['password'])
    # print(host['ip'])
    stdin, stdout, stderr = ssh.exec_command('df -lh')
    str_out = stdout.read().decode()
    str_err = stderr.read().decode()

    if str_err != "":
        print(str_err)

    lst = str_out.split('\n')
    res = []
    out = []
    for i in lst[1:]:
        lst_out = i.split(' ')
        tmp = [lt for lt in lst_out if lt]
        res.append(tmp)
    res = [i for i in res if i]

    # 筛选出合适的磁盘
    for rs in res:
        if rs[1][-1] == 'T':
            out.append(rs)
        if float(rs[1][:-1]) >= 40 and rs[1][-1] == 'G':
            out.append(rs)
    result = []

    for o in out:
        result.append([o[0], o[1], o[3], o[-2]])
    # print(result)
    time.sleep(1)
    ssh.close()
    return result



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


