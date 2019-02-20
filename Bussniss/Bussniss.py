#coding:utf-8
__author__ = 'zcs'
from Commonlib.Commonlib import Commonlib
from selenium.webdriver.common.keys import Keys
class Bussniss():
    def __init__(self):
        self.p=Commonlib()
    def login(self,username,password):
        self.p.waite(3)
        self.p.activeEvent("xpath",".//*[@id='global_unlogin']/a[1]")
        self.p.waite(3)
        self.p.inputKeys("xpath",".//*[@id='un']",username)
        self.p.inputKeys("xpath",".//*[@id='pwd']",password)
        self.p.activeEvent("xpath",".//*[@id='login_button']")
        self.p.waite(3)
        try:
            gt=self.p.getText("xpath",".//*[@id='global_login']/div[1]/a[1]")
        except:
            gt=self.p.getText("xpath",".//*[@id='error_tips']")
        return gt
    def searchPrice(self,str):
        self.p.waite(3)
        self.p.inputKeys("xpath",".//*[@id='keyword']",str+Keys.ENTER)
        self.p.waite(3)
        str1=self.p.localElement("partail_link_text",str).get_attribute("id")
        return self.p.localElement("xpath",".//*[@id='price0_"+str1[8:]+"']").get_attribute("yhdprice")
