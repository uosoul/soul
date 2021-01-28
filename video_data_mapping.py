import os
import time
import sys

def get_time(ts_name):
    t = os.path.getctime(ts_name)   # 时间戳
    timeArray = time.localtime(t)
    video_time = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return video_time

video_data_mapping = '/var/services/homes/admin/video_data_mapping'
base_url = '/var/services/homes/admin/video_data'
roomid_all = os.listdir(base_url)

for roomid in roomid_all:

    # 获取roomid目录下的时间目录的名字
    roomid_time_dirname = os.path.join(base_url, roomid)
    date_time = os.listdir(roomid_time_dirname)[0]

    # 获取该roomid 对应的视频路径
    roomid_time_dir = os.path.join(roomid_time_dirname, date_time)

    # 获取所有后缀为 ts的视频。
    video_all = [video for video in os.listdir(roomid_time_dir) if os.path.splitext(video)[1] == '.ts']

    # 生成 roomid_time.txt文件
    filename = os.path.join(video_data_mapping, roomid + '_' + date_time + '.txt')
    with open(filename, 'w')as f:
        for video in video_all:
            # 完整的视频路径
            video_url = os.path.join(roomid_time_dir, video)
            video_create_time = get_time(video_url)
            f.write(video+'\t'+video_create_time+'\n')





