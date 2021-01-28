import requests
from datetime import datetime
from mail_util import SendEMail

wid = 'A3359E1B43376F77E0538101600A8722'
userId = '201307050011'
today = str(datetime.now())[:10].replace('-','/')

def check(wid,uid):
    url = 'http://form.hhu.edu.cn/pdc/formDesignApi/dataFormSave?wid={}&userId={}'.format(wid,uid)
    # print(url)
    headers = {
        'Host':'form.hhu.edu.cn',
        'Content-Length': '660',
        'Accept': 'application/json,text/javascript,*/*;q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0(Macintosh;IntelMacOSX10_15_6)AppleWebKit/537.36(KHTML,likeGecko)Chrome/87.0.4280.88Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Origin': 'http://form.hhu.edu.cn',
        'Referer': 'http://form.hhu.edu.cn/pdc/formDesignApi/S/xznuPIjG',
        'Accept-Encoding': 'gzip,deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cookie': 'JSESSIONID=E08CAA2BCBC5DFBB85208B87D5017E75;amlbcookie=01;iPlanetDirectoryPro=AQIC5wM2LY4SfcyutWDzVC6mBpob2z0mkwbmYxQMlePRIIc%3D%40AAJTSQACMDE%3D%23',
        'Connection': 'keep-alive'
    }

    data = {
        # 填报时间
        "DATETIME_CYCLE":today,
        # 学号
        "XGH_566872":"201307050011",
        # 姓名
        "XM_140773":"张宏宇",
        # 身份证号
        "SFZJH_402404":"320684199711166417",
        # 学院
        "SZDW_439708":"计算机与信息学院",
        # 专业
        "ZY_878153":"软件工程",
        # 攻读学位
        "GDXW_926421":"硕士生",
        # 导师
        "DSNAME_606453":"唐彦",
        # 培养类别
        "PYLB_253720":"非定向",
        # 宿舍楼
        "SELECT_172548":"江宁校区2舍",
        # 宿舍号
        "TEXT_91454":"330",
        # 手机号码
        "TEXT_24613":"18361489212",
        # 紧急联系人电话
        "TEXT_826040":"15162790648",
        # 您今日上午8点体温是否超过37.3℃
        "RADIO_479243":"否",
        # 您今日下午18点体温是否超过37.3℃
        "RADIO_813412":"否",
        # 您的健康情况
        "RADIO_49955":"健康",
        # 健康码是否正常
        "RADIO_17769":"是",
        # 目前是否在校
        "RADIO_165012":"是",
        # 是否是新冠肺炎病例或疑似病例、无症状感染者
        "RADIO_221941":"",
        # 今日是否与确诊/疑似病例或无症状感染者密接
        "RADIO_460881":"",
        # 今日是否在疫情严重地区停留或与从疫情严重地区返乡未满14天人员密接
        "RADIO_769987":"",
        # 今日是否与发热或呼吸道感染症状人员密接
        "RADIO_165581":"",
        # 今日是否有海外旅居史
        "RADIO_232736":"",
        # 今日是否接触过境外归国未满14天人员
        "RADIO_413114":"",
        # 今日是否被要求隔离
        "RADIO_685292":"",
        # 是否在国内
        "RADIO_875565":"",
        # 返乡目的地
        "PICKER_928530":"",
        # 当日所在地
        "PICKER_449470":"江苏省,南京市,鼓楼区",
        # 国家
        "TEXT_248903":"",
        # 城市
        "TEXT_301305":"",
        # 学校
        "TEXT_195684":""

    }
    r = requests.post(url=url,data=data,headers=headers)
    s = SendEMail('smtp.qq.com', 465, '2593548686@qq.com', 'jihrlicmenwcdihe')
    if r.json().get('result') is True:
        msg = '打卡成功'
    else:
        msg = '打卡失败'
    s.send_text('2593548686@qq.com',msg,'打卡提醒')

if __name__ == '__main__':
    check(wid,userId)
