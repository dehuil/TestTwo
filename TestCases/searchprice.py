#coding:utf-8
__author__ = 'zcs'
from Commonlib.Commonlib import Commonlib
from selenium.webdriver.common.keys import Keys
p=Commonlib()
p.openBrowser("http://www.yhd.com")
p.waite(3)
str=u"Apple 苹果 iPhone 7 (A1660) 32G 玫瑰金色 移动联通电信4G手机"
p.inputKeys("xpath",".//*[@id='keyword']",str+Keys.ENTER)
p.waite(3)
str1=p.localElement("partail_link_text",str).get_attribute("id")
print p.localElement("xpath",".//*[@id='price0_"+str1[8:]+"']").get_attribute("yhdprice")
p.closeBrowser()