#coding:utf-8
__author__ = 'zcs'

import time
import os
import sys
sys.path.append(os.getcwd())
from Commonlib.Commonlib import Commonlib
p=Commonlib()
p.openBrowser("http://www.521ke.com")
time.sleep(3)
p.inputKeys("xpath",".//input[@name='wd']",u"课程帮")
# dr.find_element_by_xpath(".//input[@name='q']").send_keys(u"我的前半生")
# time.sleep(2)
p.activeEvent("xpath",u".//input[@value=' ']")
time.sleep(5)
p.closeBrowser()
#dr.find_element_by_xpath(u".//input[@value='搜 索']").click()
# time.sleep(3)
# #dr.find_element_by_link_text(u"火狐主页").click()
# #dr.find_element_by_partial_link_text(u"主页").click()
# time.sleep(3)
# dr.quit()

