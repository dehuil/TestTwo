#coding:utf-8
__author__ = 'lee'
from Commonlib.Commonlib import Commonlib
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait as ww
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import chardet
class Bussniss():
    def __init__(self):
        self.p=Commonlib()

    def kcb_login(self,username,password):
        self.p.wait(4)
        self.p.inputKeys("name","loginText",username)
        self.p.inputKeys("name","password",password)
        self.p.wait(2)
        self.p.activeEvent("xpath","//button[@class='el-button el-button--primary']")
        self.p.wait(3)
        try:
            gt=self.p.getText("xpath","//span[contains(text(),'1111')]")
            gt.encode('raw_unicode_escape')
            return gt
        except NoSuchElementException as e:
            print('登录失败')
        self.p.wait(5)

    def searchPrice(self,str):
        self.p.waite(3)
        self.p.inputKeys("xpath",".//*[@id='keyword']",str+Keys.ENTER)
        self.p.waite(3)
        str1=self.p.localElement("partail_link_text",str).get_attribute("id")
        return self.p.localElement("xpath",".//*[@id='price0_"+str1[8:]+"']").get_attribute("yhdprice")

if __name__ == '__main__':
    1