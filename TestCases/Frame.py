#coding:utf-8
__author__ = 'zcs'
from Commonlib.Commonlib import Commonlib
p=Commonlib()
p.openBrowser("http://www.diaochaquan.cn")
p.activeEvent("link_text",u"会员登录")
p.waite(3)
print p.getText("xpath",".//*[@id='popupTitle']")
# dr.switch_to.frame("TB_iframeContent")
# dr.find_element_by_xpath(".//*[@id='txtUsername']").send_keys("tttt")
p.closeBrowser()