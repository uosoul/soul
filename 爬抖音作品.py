import requests
import csv,sys,json,time
index = 0

with open('xinwen.txt','r',encoding='utf-8')as rf:

    all_kinds = rf.readlines()
    for kind in all_kinds:
        info = kind.split(',')
        # 判断has_more如果为一则继续爬取   下一页的URL需要重新拼接max_cursor
        uid = info[0]   # 命名CSV
        if index < 10:
            index += 1
            continue
        index += 1
        name = f'./files/{uid}.csv'
        secid = info[-1].strip()
        max_cursor = 0
        has_more = 1
        n = 0
        url = f"http://122.114.11.174:3389/douyin/usertimeline?secid={secid}&max_cursor={max_cursor}"
        headers = ('aweme_id', 'desc','create_time', 'comment_count', 'digg_count', 'duration', 'download_count', 'play_count', 'share_count')
        lst = []
        with open(name, 'w', newline='',encoding='gb18030')as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            while has_more:
                n += 1
                for i in range(10):
                    try:
                        datas = requests.get(url, timeout=10).content.decode()
                        time.sleep(1)
                        if len(json.loads(datas).get("aweme_list")) > 0:
                            break
                    except:
                        if i == 9:
                            print(datas)
                            print("尝试超过10次，结束了")
                            print(f'执行到第{index}个')
                            sys.exit()
                # time.sleep(1)
                datas_dic = json.loads(datas)
                ten_works = datas_dic.get("aweme_list")
                for work in ten_works:
                    aweme_id = repr(work.get('aweme_id'))     # 有
                    desc = work.get('desc')     # 有
                    create_time = work.get('create_time')   # 有
                    duration = work.get('duration')     # 有
                    comment_count = work.get('statistics').get('comment_count')     # 有
                    digg_count = work.get('statistics').get('digg_count')   # 有
                    download_count = work.get('statistics').get('download_count')   # 有
                    play_count = work.get('statistics').get('play_count')
                    share_count = work.get('statistics').get('share_count')     # 有

                    # 'aweme_id', 'desc','create_time', 'comment_count', digg_count', 'duration','download_count', 'play_count', 'share_count'
                    line = (aweme_id, desc, create_time,comment_count,digg_count,duration,download_count,play_count,share_count)
                    writer.writerow(line)

                has_more = datas_dic.get("has_more")

                max_cursor = datas_dic.get("max_cursor")      # max_cursor=0
                # if max_cursor == 0 and has_more !=0 :
                lst.append(max_cursor)
                url = f"http://122.114.11.174:3389/douyin/usertimeline?secid={secid}&max_cursor={max_cursor}"
                print(n, '次', url)
        print(max_cursor, has_more, datas_dic, datas)
        print(f'总共爬取了：{n}次,不重复的网址有：{len(set(lst))}个')
        with open('log.txt', 'a+')as f:
            f.write(str(uid)+'\t'+str(len(set(lst)))+'\n')


