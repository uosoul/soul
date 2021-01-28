from ronglian_sms_sdk import SmsSDK

accId = '8aaf0708762cb1cf0176f62c86c2494c'
accToken = 'c26e62fd491b4a2390b40fe9b0bbfaf7'
appId = '8aaf0708762cb1cf0176f62c88564953'


def send_message():
    sdk = SmsSDK(accId, accToken, appId)
    tid = '1'
    mobile = '13260886230'
    datas = ('666666', '5')
    resp = sdk.sendMessage(tid, mobile, datas)
    print(resp)

if __name__ == '__main__':
    send_message()
