#coding:utf-8
__author__ = 'zcs'
from selenium import webdriver
import time
dr=webdriver.Firefox()
dr.get("http://www.buyiju.com/")
dr.maximize_window()
time.sleep(3)
dr.find_element_by_xpath(u".//input[@value='开始算命']").click()
time.sleep(2)
dr.switch_to.alert.accept()
dr.close()
