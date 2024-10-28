# -*- coding: utf8 -*-

import requests,time,re,json,random
import os

TG_BOT_TOKEN = ""           # telegram bot token 自行申请
TG_USER_ID = ""             # telegram 用户ID

def telegram_bot(title, content):
    print("\n")
    tg_bot_token = TG_BOT_TOKEN
    tg_user_id = TG_USER_ID
    if "TG_BOT_TOKEN" in os.environ and "TG_USER_ID" in os.environ:
        tg_bot_token = os.environ["TG_BOT_TOKEN"]
        tg_user_id = os.environ["TG_USER_ID"]
    if not tg_bot_token or not tg_user_id:
        print("Telegram推送的tg_bot_token或者tg_user_id未设置!!\n取消推送")
        return
    print("Telegram 推送开始")
    send_data = {"chat_id": tg_user_id, "text": title +
                 '\n\n'+content, "disable_web_page_preview": "true"}
    response = requests.post(
        url='https://api.telegram.org/bot%s/sendMessage' % (tg_bot_token), data=send_data)
    print(response.text)

now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
headers = {
        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 9; MI 6 MIUI/20.6.18)'
        }

#获取登录code
def get_code(location):
    code_pattern = re.compile("(?<=access=).*?(?=&)")
    code = code_pattern.findall(location)[0]
    return code

#登录
def login(user,password):
    url1 = "https://api-user.huami.com/registrations/" + user + "/tokens"
    headers = {
        "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
    "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2"
        }
    data1 = {
        "client_id":"HuaMi",
        "password":f"{password}",
        "redirect_uri":"https://s3-us-west-2.amazonaws.com/hm-registration/successsignin.html",
        "token":"access"
        }
    r1 = requests.post(url1,data=data1,headers=headers,allow_redirects=False)
    location = r1.headers["Location"]
    try:
        code = get_code(location)
    except:
        return 0,0
    #print("access_code获取成功！")ste
    #print(code)

    url2 = "https://account.huami.com/v2/client/login"
    data2 = {
            "allow_registration=": "false",
            "app_name": "com.xiaomi.hm.health",
            "app_version": "6.3.5",
            "code": f"{code}",
            "country_code": "CN",
            "device_id": "2C8B4939-0CCD-4E94-8CBA-CB8EA6E613A1",
            "device_model": "phone",
            "dn": "api-user.huami.com%2Capi-mifit.huami.com%2Capp-analytics.huami.com",
            "grant_type": "access_token",
            "lang": "zh_CN",
            "os_version": "1.5.0",
            "source": "com.xiaomi.hm.health",
            "third_name": "email",
        } 
    r2 = requests.post(url2,data=data2,headers=headers).json()
    login_token = r2["token_info"]["login_token"]
    #print("login_token获取成功！")
    #print(login_token)
    userid = r2["token_info"]["user_id"]
    #print("userid获取成功！")
    #print(userid)

    return login_token,userid

#主函数
def main(user, passwd, step):
    user = str(user)
    password = str(passwd)
    step = str(step)
    if user == '' or password == '':
        print ("用户名或密码填写有误！")
        return

    if step == '':
        print ("已设置为随机步数（20000-29999）")
        step = str(random.randint(20000,29999))
    login_token = 0
    login_token,userid = login(user,password)
    if login_token == 0:
        print("登陆失败！")
        return "login fail!"

    t = get_time()

    app_token = get_app_token(login_token)

    today = time.strftime("%F")

    data_json = '%5B%7B%22data_hr%22%3A%22%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F9L%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2FVv%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F0v%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F9e%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F0n%5C%2Fa%5C%2F%5C%2F%5C%2FS%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F0b%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F1FK%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2FR%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F9PTFFpaf9L%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2FR%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F0j%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F9K%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2FOv%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2Fzf%5C%2F%5C%2F%5C%2F86%5C%2Fzr%5C%2FOv88%5C%2Fzf%5C%2FPf%5C%2F%5C%2F%5C%2F0v%5C%2FS%5C%2F8%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2FSf%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2Fz3%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F0r%5C%2FOv%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2FS%5C%2F9L%5C%2Fzb%5C%2FSf9K%5C%2F0v%5C%2FRf9H%5C%2Fzj%5C%2FSf9K%5C%2F0%5C%2F%5C%2FN%5C%2F%5C%2F%5C%2F%5C%2F0D%5C%2FSf83%5C%2Fzr%5C%2FPf9M%5C%2F0v%5C%2FOv9e%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5

if __name__ == "__main__":
    user = os.environ['USER_PHONE']
    password = os.environ['USER_PWD']
    # step = str(randint(int(os.environ['STEP_MIN']), int(os.environ['STEP_MAX'])))
    step = os.environ['STEP']
    # step = str(randint(10123, 12302)) 
    main(user，password，step)
