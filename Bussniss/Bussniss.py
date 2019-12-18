#coding:utf-8
__author__ = 'zcs'
from Commonlib.Commonlib import Commonlib
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait as ww
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
from selenium.webdriver.common.by import By
class Bussniss():
    def __init__(self):
        self.p=Commonlib()

    def login(self,username,password):
        self.p.seeWait('LINK_TEXT',u'登录',20,0.5)
        self.p.activeEvent("link_text","登录")
        self.p.wait(4)
        self.p.inputKeys("id","j_username",username)
        self.p.inputKeys("id","j_password",password)
        self.p.wait(1)
        self.p.activeEvent("id","btn_Login")
        self.p.wait(3)
        try:
            gt=self.p.getText("link_text","mwlt")
        finally:
            gt='错误'

    def searchPrice(self,str):
        self.p.waite(3)
        self.p.inputKeys("xpath",".//*[@id='keyword']",str+Keys.ENTER)
        self.p.waite(3)
        str1=self.p.localElement("partail_link_text",str).get_attribute("id")
        return self.p.localElement("xpath",".//*[@id='price0_"+str1[8:]+"']").get_attribute("yhdprice")
