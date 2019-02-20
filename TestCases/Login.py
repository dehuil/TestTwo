#coding:utf-8
__author__ = 'zcs'
from Commonlib.Commonlib import Commonlib
p=Commonlib()
p.openBrowser("http://www.yhd.com")
p.waite(3)
p.activeEvent("xpath",".//*[@id='global_unlogin']/a[1]")
p.waite(3)
p.inputKeys("xpath",".//*[@id='un']","zcsfcy1225")
p.inputKeys("xpath",".//*[@id='pwd']","kcrx8888")
p.activeEvent("xpath",".//*[@id='login_button']")
p.waite(3)
p.moveElement("xpath",".//*[@id='global_login']/div[1]/a[1]")
p.waite(3)
p.activeEvent("link_text",u"退出登录")
p.waite(3)
p.closeBrowser()
# gt=dr.find_element_by_xpath(".//*[@id='global_login']/div[1]/a[1]").text
# if gt=="zcsfcy1225":
#     print u"登录成功"
# else:
#     print u"登录失败"