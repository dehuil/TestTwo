#coding:utf-8
__author__ = 'zcs'
import time
from selenium import webdriver
dr=webdriver.Firefox()
dr.maximize_window()
dr.get("https://www.duba.com")
time.sleep(5)
dr.find_element_by_partial_link_text(u"网易").click()
time.sleep(5)
all=dr.window_handles
dr.switch_to.window(all[-1])
dr.find_element_by_link_text(u"网易邮箱").click()
time.sleep(3)
all=dr.window_handles
dr.switch_to.window(all[-1])
dr.find_element_by_xpath(".//*[@id='userNameIpt']").send_keys("zcs")
