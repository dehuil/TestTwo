#coding=utf-8
from selenium import webdriver
from Commonlib.Commonlib import Commonlib
import requests
import json
import time
import random
from itertools import cycle
import re
url="http://ques.rishis.cn/#/login"
users={'lidehui':'111111','caoxianglan':'111111'}

def get_cookies(userkey):
    p=Commonlib()
    browser = webdriver.Chrome()
    browser.get(url)
    browser.find_element_by_name('loginText').send_keys(userkey)
    print('名字是',userkey)
    p.wait(1)
    browser.find_element_by_name('password').send_keys(users[userkey])
    print('密码是',users[userkey])
    p.wait(4)
    browser.find_element_by_css_selector("#app > div > div.login-container > form > button.el-button.el-button--primary > span").click()
    p.wait(3)
    for i in browser.get_cookies():
        if i["name"]=='vue_token':
            return i["value"].replace('%20',' ',1)
    # with open("cookies.txt","w") as f:
    #     f.write(json.dumps(cookie))
    browser.close()

if __name__ == "__main__":
    1