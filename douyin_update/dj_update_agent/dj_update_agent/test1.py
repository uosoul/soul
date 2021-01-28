import sys
import pymysql
from dj_update_agent.utils1 import getUserMsg
from dj_update_agent.utils1 import getUserMsg3


# Uid 4296519660339635

def update_agent(Uid, brand):
    state = True
    conn = pymysql.connect(
        host='47.93.1.155',
        port=3306,
        user='root',
        password='Dyanalysis@1a2b3c',
        db='dy_live',
        charset='utf8'
    )
    conn_local = pymysql.connect(
        # host='localhost',
        host='192.168.2.9',
        port=3306,
        user='root',
        password='Dyanalysis@1a2b3c',
        db='dy_live',
        charset='utf8'
    )
    conn3 = pymysql.connect(
        host='47.93.1.155',
        port=3306,
        user='root',
        password='Dyanalysis@1a2b3c',
        db='dy_live_new',
        charset='utf8'
    )

    car_brand = {'奥迪': 1, '宝马': 2, '奔驰': 3, '沃尔沃': 4, '大众': 5, '保时捷': 6, '雷克萨斯': 7, '东风本田': 8}
    province_region = {'江苏': ('东部区', 4), '山东': ('东北区', 1), '辽宁': ('东北区', 1), '上海': ('东部区', 4), '安徽': ('东部区', 4),
                       '江苏省': ('东部区', 4), '山东省': ('东北区', 1), '辽宁省': ('东北区', 1), '上海市': ('东部区', 4), '安徽省': ('东部区', 4),
                       '北京': ('北部区', 7), '河南': ('东部区', 4), '浙江': ('东南区', 2), '甘肃': ('西部区', 6), '福建': ('东南区', 2),
                       '黑龙江': ('东北区', 1),
                       '北京市': ('北部区', 7), '河南省': ('东部区', 4), '浙江省': ('东南区', 2), '甘肃省': ('西部区', 6), '福建省': ('东南区', 2),
                       '黑龙江省': ('东北区', 1),
                       '湖北': ('南部区', 5), '四川': ('西部区', 6), '吉林': ('东北区', 1), '广东': ('南部区', 5), '广西': ('南部区', 5),
                       '海南': ('南部区', 5),
                       '湖北省': ('南部区', 5), '四川省': ('西部区', 6), '吉林省': ('东北区', 1), '广东省': ('南部区', 5),
                       '广西壮族自治区': ('南部区', 5), '海南省': ('南部区', 5),
                       '河北': ('北部区', 7), '云南': ('西部区', 6), '天津': ('北部区', 7), '内蒙古': ('北部区', 7), '重庆': ('西部区', 6),
                       '湖南': ('南部区', 5),
                       '河北省': ('北部区', 7), '云南省': ('西部区', 6), '天津市': ('北部区', 7), '内蒙古自治区': ('北部区', 7), '重庆市': ('西部区', 6),
                       '湖南省': ('南部区', 5),
                       '江西': ('南部区', 5), '江西省': ('南部区', 5), '山西': ('北部区', 7), '山西省': ('北部区', 7)}
    # 调用接口获取各个信息，
    dic_all = getUserMsg3(Uid)
    print(dic_all)
    keys = ['uid', 'nickname', 'fans_count', 'avatar_url',
            'city', 'province', 'totl_video_digg_count', 'total_post_count']

    is_live = 1     # 一般为1
    bid = car_brand[brand]  # 品牌ID

    uid = dic_all['uid']    # uid  live_new表需要
    nick_name = dic_all['nickname']  # 昵称
    fans_count = dic_all['fans_count']  # 粉丝数
    avatar_url = dic_all['avatar_url']  # 头像URL
    city = dic_all['city']  # 城市
    province = dic_all['province']  # 省
    region = province_region[province][0]     # 地区
    rid = province_region[province][1]    # 地区ID   ('南部区', 4),
    total_video_digg_count = dic_all['total_video_digg_count']   # 点赞数
    total_post_count = dic_all['total_post_count']      # 作品数
    sql_insert = """insert into agent (brand,is_live,bid,nick_name,fans_count,avatar_url,city,
    province,region,rid,total_video_digg_count,total_post_count)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    print((brand, is_live, bid, nick_name, fans_count, avatar_url, city,
           province, region, rid, total_video_digg_count, total_post_count))
    cur = conn.cursor()
    cur_local = conn_local.cursor()     # 本地
    cur3 = conn3.cursor()       # live_new
    try:
        # 执行创建表sql
        cur.execute(sql_insert, (brand,is_live,bid,nick_name,fans_count,avatar_url,city,
    province,region,rid,total_video_digg_count,total_post_count))
        last_id = int(cur.lastrowid)


        # 本地

        sql_insert2 = """insert into agent (id,brand,is_live,bid,nick_name,fans_count,avatar_url,city,
        province,region,rid,total_video_digg_count,total_post_count)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        cur_local.execute(sql_insert2, (last_id, brand, is_live, bid, nick_name, fans_count, avatar_url, city,
                             province, region, rid, total_video_digg_count, total_post_count))

        # live_new

        sql_insert3 = """insert into agent (id,uid,brand,bid,nick_name,fans_count,avatar_url,city,
                province,region,rid)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
        cur3.execute(sql_insert3, (last_id, uid, brand, bid, nick_name, fans_count, avatar_url, city,
                                        province, region, rid))
        
    except Exception as e:
        print(e)
        print("创建失败")
        state = False
    finally:
        if state == False:
            conn.rollback()
            conn_local.rollback()
            conn3.rollback()
        else:
            conn.commit() # insert,update需要commit，查询不需要
            print("执行成功！", cur.lastrowid)
            conn_local.commit()
            print("执行成功！", int(cur_local.lastrowid))
            conn3.commit()
            print("执行成功！", int(cur3.lastrowid))
        conn.close()
        return state





# if __name__ == '__main__':
#     brand = '宝马'
#     update_agent(72934616299, brand)