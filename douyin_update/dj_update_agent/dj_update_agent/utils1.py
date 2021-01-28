# _*_ coding:utf-8 _*_
import hashlib

import requests
import time
import re
import pymysql
import threading
from dj_update_agent.apidemo import douApi
import json
import pandas as pd

user_id = '98182548230'
# sec_uid = 'MS4wLjABAAAAS6-PQESP85l3TCuMRoxfzI9uV55Vlb_2HVl9kvYlouc'
sec_uid = 'MS4wLjABAAAAyOfrn2y_K-MNXhKp1Vv2KWlSDfiwek0oNP37igd9cpQ'
# 开始位置
max_cursor = '0'
max_time = '0'
# global_cookie = 'tt_webid=51d0b5467ab939ba8067ea1ff61c10f6; d_ticket=fe89d1c059d16ab34512ca7434c8f5c97568f; odin_tt=6880023c291630d22789433ccc3017381ccfaba0f781ecf5561b57fb7889401a0328ae777d70cecafc99e70b309cf457869bc2e5586ff38c17306b5d6075a544; sid_guard=e0d381191bf688bd3142ca43202a4143%7C1604124484%7C5184000%7CWed%2C+30-Dec-2020+06%3A08%3A04+GMT; uid_tt=703babe2ff55e8b36341c19a0e905b30; sid_tt=e0d381191bf688bd3142ca43202a4143; sessionid=e0d381191bf688bd3142ca43202a4143'
global_cookie = 'MONITOR_WEB_ID=e35d5257-79ec-4dc2-ac3f-9816f5bbf21d; gftoken=MzU0NDQyNTk2YnwxNjA3OTQ4OTEwOTN8fDAGBgYGBgY; csrftoken=TQF4qb2q5OgMwQe9yTkqBZ3v9uk4LEiO; tt_webid=6906087601452828173; passport_csrf_token=4d2c2a7a47eb65642934afde3c25320b; n_mh=9-mIeuD4wZnlYrrOvfzG3MuT6aQmCUtmr8FxV8Kl8xY; sid_guard=354442596b0e190daf50aebed80e35e9%7C1607948888%7C5184000%7CFri%2C+12-Feb-2021+12%3A28%3A08+GMT; uid_tt=c9f80d0b046511116b411fb7117213ca; uid_tt_ss=c9f80d0b046511116b411fb7117213ca; sid_tt=354442596b0e190daf50aebed80e35e9; sessionid=354442596b0e190daf50aebed80e35e9; sessionid_ss=354442596b0e190daf50aebed80e35e9; star_sessionid=bb2e9174a591245701766013d7b98173'

def getXKandXG(max_time='0', type='user', stype=2):
    # url = 'http://47.103.221.69:8080/api/xg0408'
    url = 'http://localhost:8080/api/xg0408'
    # 用户
    if type == 'user':
        datas = '''{
            "cookie":"''' + global_cookie + '''",
            "param":"sec_user_id=''' + sec_uid + '''&address_book_access=2&from=0&publish_video_strategy_type=2&user_avatar_shrink=188_188&user_cover_shrink=750_422&os_api=23&device_type=MI+5s&ssmix=a&manifest_version_code=120501&dpi=270&uuid=540000000306958&app_name=aweme&version_name=12.5.0&ts=1605052546&cpu_support64=false&storage_type=0&app_type=normal&appTheme=dark&ac=wifi&host_abi=armeabi-v7a&update_version_code=12509900&channel=xinyou_dy_and10&_rticket=1605052547049&device_platform=android&iid=3746764381502061&version_code=120500&mac_address=08%3A00%3A27%3A6F%3A1B%3A86&cdid=a18cf4e7-1d04-48b3-8312-534ec33ba8c7&openudid=ae30fe852c1140d1&device_id=3394919896190647&resolution=810*1440&os_version=6.0.1&language=zh&device_brand=Xiaomi&aid=1128&mcc_mnc=46007",
            "stub":"",
            "sessionId":""
            }'''
    # 关注
    elif type == 'following':
        datas = '''{
                "cookie":"''' + global_cookie + '''",
                "param":"user_id=''' + user_id + '''&sec_user_id=''' + sec_uid + '''&max_time=''' + max_time + '''&count=20&offset=0&source_type=''' + stype + '''&address_book_access=1&gps_access=1&vcd_count=0&vcd_auth_first_time=0&os_api=23&device_type=MI+5s&ssmix=a&manifest_version_code=120501&dpi=270&uuid=350000000189098&app_name=aweme&version_name=12.5.0&ts=1603700025&cpu_support64=false&storage_type=0&app_type=normal&appTheme=dark&ac=wifi&host_abi=armeabi-v7a&update_version_code=12509900&channel=xinyou_dy_and10&_rticket=1603700024836&device_platform=android&iid=773684176105005&version_code=120500&mac_address=08%3A00%3A27%3A6F%3A1B%3A86&cdid=933eb827-2322-4958-b8c3-2897d49b4aad&openudid=ae30fe852c1140d1&device_id=3394919896190647&resolution=810*1440&os_version=6.0.1&language=zh&device_brand=Xiaomi&aid=1128",
                "sessionId":""
                }'''
    else:
        # 作品
        datas = '''{
                "cookie":"''' + global_cookie + '''",
                "param":"source=0&user_avatar_shrink=96_96&video_cover_shrink=248_330&publish_video_strategy_type=2&max_cursor=''' + max_cursor + '''&sec_user_id=''' + sec_uid + '''&count=20&is_order_flow=0&os_api=23&device_type=MI+5s&ssmix=a&manifest_version_code=120501&dpi=270&uuid=350000000189098&app_name=aweme&version_name=12.5.0&ts=1603690207&cpu_support64=false&storage_type=0&app_type=normal&appTheme=dark&ac=wifi&host_abi=armeabi-v7a&update_version_code=12509900&channel=xinyou_dy_and10&_rticket=1603690205951&device_platform=android&iid=773684176105005&version_code=120500&mac_address=08%3A00%3A27%3A6F%3A1B%3A86&cdid=933eb827-2322-4958-b8c3-2897d49b4aad&openudid=ae30fe852c1140d1&device_id=3394919896190647&resolution=810*1440&os_version=6.0.1&language=zh&device_brand=Xiaomi&aid=1128",
                "stub":"",
                "sessionId":""
                }'''

    headers = {
        'User-Agent': 'okhttp/3.10.0.1',
        'Content-Type': 'application/json'
    }
    r = requests.post(url=url, headers=headers, data=datas)
    j = r.json()
    return {'XG': j['X-Gorgon'], 'XK': j['X-Khronos']}


def remove_emoji(text):
    try:
        highpoints = re.compile(u'[\U00010000-\U0010ffff]')
    except re.error:
        highpoints = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    return highpoints.sub(u'', text)


def getUserMsg(uid):
    '''
    global sec_uid
    sec_uid = secuid1
    pdic = getXKandXG()

    timestr = str(int(time.time() * 1000))
    headers = {
        'Accept-Encoding': 'gzip',
        'passport-sdk-version': '17',
        'X-Tt-Token': '00799b7678c710df16aa80e7ff484e53e1c73fecafc21cd34f5d8a885cc1c39b5ae4effe5ab9ee371530c738aad965b02d2',
        'sdk-version': '2',
        'X-SS-REQ-TICKET': timestr,
        'Cookie': global_cookie,
        'X-Gorgon': pdic.get('XG'),
        'X-Khronos': str(pdic.get('XK')),
        'Host': 'aweme.snssdk.com',
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.10.0.1'
    }

    url = 'https://aweme.snssdk.com/aweme/v1/user/profile/other/?sec_user_id=' + sec_uid + '&address_book_access=2&from=0&publish_video_strategy_type=2&user_avatar_shrink=188_188&user_cover_shrink=750_422&os_api=23&device_type=MI+5s&ssmix=a&manifest_version_code=120501&dpi=270&uuid=540000000306958&app_name=aweme&version_name=12.5.0&ts=1605052546&cpu_support64=false&storage_type=0&app_type=normal&appTheme=dark&ac=wifi&host_abi=armeabi-v7a&update_version_code=12509900&channel=xinyou_dy_and10&_rticket=1605052547049&device_platform=android&iid=3746764381502061&version_code=120500&mac_address=08%3A00%3A27%3A6F%3A1B%3A86&cdid=a18cf4e7-1d04-48b3-8312-534ec33ba8c7&openudid=ae30fe852c1140d1&device_id=3394919896190647&resolution=810*1440&os_version=6.0.1&language=zh&device_brand=Xiaomi&aid=1128&mcc_mnc=46007'
    # print(url)
    r = requests.get(url, headers=headers)
    '''
    # url = 'http://protocol.newringtech.com/davp/douyin/query/user_info?user_id={}&group_id=3&auth=4c2488af72'.format(
    #     uid)
    # r = requests.get(url)
    # data_j = r.json()

    data_j = douApi.get_user_info(uid)
    data_j = json.loads(data_j)
    dic_all = {}
    # uid
    uid = data_j.get('user').get('uid')
    dic_all['uid'] = uid
    # 昵称 nickname
    nickname = remove_emoji(data_j.get('user').get('nickname'))
    dic_all['nickname'] = nickname
    # 粉丝数  fans_count
    fans_count = data_j.get('user').get('follower_count')
    dic_all['fans_count'] = fans_count
    # 头像
    avatar_url = data_j.get('user').get('avatar_168x168').get('url_list')[0]
    dic_all['avatar_url'] = avatar_url
    # 城市 city
    city = data_j.get('user').get('city')
    dic_all['city'] = city
    # 省 province
    province = data_j.get('user').get('province')
    dic_all['province'] = province
    # 作品点赞数 totl_video_digg_count
    total_video_digg_count = data_j.get('user').get('total_favorited')
    dic_all['total_video_digg_count'] = total_video_digg_count
    # 作品数 total_post_count
    total_post_count = data_j.get('user').get('aweme_count')
    dic_all['total_post_count'] = total_post_count
    keys=['uid','nickname','fans_count','avatar_url',
          'city','province','totl_video_digg_count','total_post_count']


    return dic_all
def getUserMsg2(uid):

    url = 'http://protocol.newringtech.com/davp/douyin/query/user_info?user_id={}&group_id=3&auth=4c2488af72'.format(uid)
    r = requests.get(url)
    data_j = r.json()

    uid = data_j.get('user').get('uid')
    # 昵称
    nickname = remove_emoji(data_j.get('user').get('nickname'))
    # unique_id
    unique_id = data_j.get('user').get('unique_id')
    # 粉丝数
    follower_count = data_j.get('user').get('follower_count')
    # 关注数
    following_count = data_j.get('user').get('following_count')
    # 点赞数
    digg_count = data_j.get('user').get('total_favorited')
    # 作品数
    aweme_count = data_j.get('user').get('aweme_count')
    # 动态个数
    dongtai_count = data_j.get('user').get('dongtai_count')
    # 地区
    province = data_j.get('user').get('province')
    city = data_j.get('user').get('city')
    district = data_j.get('user').get('district')
    pc = city if province == city else province + city
    district = '' if city == district else district
    address = pc + district
    if address != None and len(address) > 16:
        address = address[:16]

    # 喜欢
    favoriting_count = data_j.get('user').get('favoriting_count')
    # 头像
    avatar_url = data_j.get('user').get('avatar_168x168').get('url_list')[0]

    return uid, nickname, unique_id, follower_count, following_count, digg_count, aweme_count, favoriting_count, dongtai_count, address, avatar_url

def getUserMsg3(uid):

    url = 'http://protocol.newringtech.com/davp/douyin/query/user_info?user_id={}&group_id=3&auth=4c2488af72'.format(uid)
    r = requests.get(url)
    data_j = r.json()

    print(data_j)
    dic_all = {}
    # uid
    uid = data_j.get('user').get('uid')
    dic_all['uid'] = uid
    # 昵称 nickname
    nickname = remove_emoji(data_j.get('user').get('nickname'))
    dic_all['nickname'] = nickname
    # 粉丝数  fans_count
    fans_count = data_j.get('user').get('follower_count')
    dic_all['fans_count'] = fans_count
    # 头像
    avatar_url = data_j.get('user').get('avatar_168x168').get('url_list')[0]
    dic_all['avatar_url'] = avatar_url
    # 城市 city
    city = data_j.get('user').get('city')
    dic_all['city'] = city
    # 省 province
    province = data_j.get('user').get('province')
    dic_all['province'] = province
    # 作品点赞数 totl_video_digg_count
    total_video_digg_count = data_j.get('user').get('total_favorited')
    dic_all['total_video_digg_count'] = total_video_digg_count
    # 作品数 total_post_count
    total_post_count = data_j.get('user').get('aweme_count')
    dic_all['total_post_count'] = total_post_count
    keys = ['uid', 'nickname', 'fans_count', 'avatar_url',
            'city', 'province', 'totl_video_digg_count', 'total_post_count']

    return dic_all

# 更新header
def updateHeaders(g, k):
    headers = {
        'Accept-Encoding': 'gzip',
        'passport-sdk-version': '17',
        'X-Tt-Token': '00d8671acf6ec0710ba3430b7b02ebcda4967d7ee4e8597d55ec25115af37bcf31ee8c159ea55390478b3feb9ed66211403d',
        'sdk-version': '2',
        'X-SS-REQ-TICKET': '1603680063499',
        'Cookie': global_cookie,
        'X-Gorgon': g,
        'X-Khronos': k,
        'Host': 'aweme.snssdk.com',
        'Connection': 'Keep-Alive',
        'User-Agent': 'okhttp/3.10.0.1'
    }
    return headers


def getFollowings(u_id, s_id = 0):
    global max_time, user_id, sec_uid
    user_id = u_id
    sec_uid = s_id
    max_time = '0'

    # 存放所有关注者
    following_all = []
    # 页数
    page = 0

    while True:
        '''
        stype = '2' if max_time == '0' else '1'

        pdic = getXKandXG(max_time, type='following', stype=stype)
        XG = pdic.get('XG')
        XK = str(pdic.get('XK'))
        
        headers = updateHeaders(XG, XK)
        '''
        try:
            #url = 'https://aweme.snssdk.com/aweme/v1/user/following/list/?user_id=' + user_id + '&sec_user_id=' + sec_uid + '&max_time=' + max_time + '&count=20&offset=0&source_type=' + stype + '&address_book_access=1&gps_access=1&vcd_count=0&vcd_auth_first_time=0&os_api=23&device_type=MI+5s&ssmix=a&manifest_version_code=120501&dpi=270&uuid=350000000189098&app_name=aweme&version_name=12.5.0&ts=1603700025&cpu_support64=false&storage_type=0&app_type=normal&appTheme=dark&ac=wifi&host_abi=armeabi-v7a&update_version_code=12509900&channel=xinyou_dy_and10&_rticket=1603700024836&device_platform=android&iid=773684176105005&version_code=120500&mac_address=08%3A00%3A27%3A6F%3A1B%3A86&cdid=933eb827-2322-4958-b8c3-2897d49b4aad&openudid=ae30fe852c1140d1&device_id=3394919896190647&resolution=810*1440&os_version=6.0.1&language=zh&device_brand=Xiaomi&aid=1128'
            url = 'http://api.it1002.top/open?appkey=ds5t8g6sdd&api=video.douyin.following&uid={}&page={}'.format(user_id,max_time)
            r = requests.get(url)
            text = r.content.decode('utf-8')
            data_j = json.loads(text,strict = False)
            print(data_j)
            f = data_j.get('data').get('followings')
            if max_time != '0':
                if f == None or len(f) == 0:
                    break
            elif f == None:
                break
            max_time = str(data_j.get('data').get('min_time'))
            following_all.extend(f)
            page += 1
        except:
            continue
    print('page=' + str(page))
    return following_all

def getFollowings2(uid):
    global max_time, user_id, sec_uid
    user_id = uid
    max_time = '0'

    # 存放所有关注者
    following_all = []
    # 页数
    page = 0
    # 失败次数
    fail_count = 0
    while True:
        if fail_count >= 10:
            break
        try:
            url = 'http://xx.dy.jvshuju.cn/api/user/following'
            data = {
                "uid": uid,
                "cursor": max_time,
                "token": "BSyEDwzEWDtl1Ep2JHXJwFsGZXD"
            }
            header = {
                'Content-Type': 'application/json'
            }

            r = requests.post(url,json=data,headers = header,timeout=60)
            data_j = r.json()
            f = data_j.get('followings')

            if f is None:
                fail_count+=1
                continue
            elif len(f) == 0:
                break

            max_time = str(data_j.get('min_time'))
            fail_count = 0
            following_all.extend(f)
            page += 1
            print(threading.current_thread().name,'已爬取'+str(page)+'页')
        except :
            fail_count+=1
            print(threading.current_thread().name,'失败次数:' + str(fail_count))
            continue
    print(threading.current_thread().name,'page=' + str(page))
    return following_all

# 解析关注
def parseFollowings(u_id, s_id = 0):
    f_list = getFollowings2(u_id)
    result_list = []
    if f_list != None and len(f_list) != 0:
        print(threading.current_thread().name,'%d位关注' % (len(f_list)))
        for item in f_list:
            follower_count = item.get('follower_count')
            if follower_count < 100000:
                continue
            secuid = item.get('sec_uid')
            usrid = item.get('uid')
            nickname = item.get('nickname')

            result_list.append([usrid, nickname, follower_count, secuid])
        return result_list
    else:
        return -1

def search(name,cookie):
    url = "https://star.toutiao.com/v/api/demand/author_list/?limit=20&need_detail=true&page=1&platform_source=1&key=" + str(
        name) + "&task_category=1&order_by=score&disable_replace_keyword=false&only_nick_name=false"

    header = {
        'authority': 'star.toutiao.com',
        'method': 'GET',
        'path': '/v/api/demand/author_list/?limit=20&need_detail=true&page=1&platform_source=1&key=%E6%9C%B1%E4%B8%80%E6%97%A6&task_category=1&order_by=score&disable_replace_keyword=false&only_nick_name=false',
        'scheme': 'https',
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': cookie,
        'referer': 'https://star.toutiao.com/ad',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
        'x-csrftoken': 'Qd9y6Y6niAqE5hENmcxaNn7JYwDR9T3D'
    }

    # 换成json就不会有Unicode编码了
    response = requests.get(url, headers=header).text.replace(r'\\u', r'\u')
    # print(response)
    res = json.loads(response).get('data').get('authors')[0]
    return res

def get_sign(params):
    s = ""
    #params按key排序
    keys = sorted(params.keys())
    for key in keys:
        if key=="recommend":
            value = "recommend"
        else:
            value = params[key]
        s += key + value
    salt = "e39539b8836fb99e1538974d3ac1fe98"
    s += salt

    sign = hashlib.md5(s.encode()).hexdigest()
    return sign

def get_fans_feature(o_id,cookie):
    """
    获得星图上的粉丝特征
    :param o_id:
    :return:
    """
    url = "https://star.toutiao.com/h/api/gateway/handler_get/"
    params = {
        "o_author_id":str(o_id),
        "platform_source":"1",
        "platform_channel":"1",
        "service_name":"data.AdStarDataService",
        "service_method":"GetAuthorFansDistributionV2",
    }
    sign = get_sign(params)
    params.update({
        'sign': sign
    })
    # print(params)

    header = {
    'authority': 'star.toutiao.com',
    'method': 'GET',
    'path': '/h/api/gateway/handler_get/?o_author_id='+str(o_id)+'&platform_source=1&platform_channel=1&service_name=data.AdStarDataService&service_method=GetAuthorFansDistributionV2&sign='+str(sign),
    'scheme': 'https',
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip,deflate,br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': cookie,
    'referer': 'https://star.toutiao.com/ad',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'x-csrftoken': 'Qd9y6Y6niAqE5hENmcxaNn7JYwDR9T3D',
    'x-star-service-method': 'GetAuthorMarketingInfo',
    'x-star-service-name': 'author.AdStarAuthorService'
    }
    response = requests.get(url, headers=header, params=params).text
    return json.loads(response)

def getConnector(host,db_name):
    conn = pymysql.connect(
        host=host,
        port=3306,
        user='root',
        password='Dyanalysis@1a2b3c',
        # 很重要 不能搞错
        db=db_name,
        charset='utf8'
    )
    return conn

if __name__ == '__main__':
    print(parseFollowings('109581230516'))
    # r = search('papi酱',global_cookie)
    # print(r)

    # print(getUserMsg('3619224279334190'))
    # getFollowings2('77212801186')

