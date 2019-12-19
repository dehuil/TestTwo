#coding:utf-8
__author__ = 'lee'
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from datetime import datetime
import traceback
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait as ww

class Commonlib():
    def __init__(self):
        self.dr=webdriver.Chrome()
    def openBrowser(self,myurl):
        self.dr.get(myurl)
        self.dr.maximize_window()
        time.sleep(2)
    def closeBrowser(self):
        self.dr.quit()
    def moreWindow(self):
        all=self.dr.window_handles
        self.dr.switch_to.window(all[-1])
    def localElement(self,type,value):
        if type=="id":
            return self.dr.find_element_by_id(value)
        elif type=="name":
            return self.dr.find_element_by_name(value)
        elif type=="xpath":
            return self.dr.find_element_by_xpath(value)
        elif type=="link_text":
            return self.dr.find_element_by_link_text(value)
        elif type=="partail_link_text":
            return self.dr.find_element_by_partial_link_text(value)
    def activeEvent(self,type,value):
        if type=="id":
            self.dr.find_element_by_id(value).click()
        elif type=="name":
            self.dr.find_element_by_name(value).click()
        elif type=="xpath":
            self.dr.find_element_by_xpath(value).click()
        elif type=="link_text":
            self.dr.find_element_by_link_text(value).click()
        elif type=="partail_link_text":
            self.dr.find_element_by_partial_link_text(value).click()
    def inputKeys(self,type,value,sk):
        if type=="id":
            self.dr.find_element_by_id(value).send_keys(sk)
        elif type=="name":
            self.dr.find_element_by_name(value).send_keys(sk)
        elif type=="xpath":
            self.dr.find_element_by_xpath(value).send_keys(sk)
        elif type=="link_text":
            self.dr.find_element_by_link_text(value).send_keys(sk)
        elif type=="partail_link_text":
            self.dr.find_element_by_partial_link_text(value).send_keys(sk)

    def getText(self,type,value):
        if type=="id":
            return self.dr.find_element_by_id(value).text
        elif type=="name":
            return self.dr.find_element_by_name(value).text
        elif type=="xpath":
            return self.dr.find_element_by_xpath(value).text
        elif type=="link_text":
            return self.dr.find_element_by_link_text(value).text
        elif type=="partail_link_text":
            return self.dr.find_element_by_partial_link_text(value).text

    def createDir(self):
          '''生成当前日期字符串'''
          date = time.localtime()
          str1='-'.join([str(date.tm_year), str(date.tm_mon),str(date.tm_mday)])
          '''生成当前时间字符串'''
          date = time.localtime()
          str2='-'.join([str(date.tm_hour), str(date.tm_min),str(date.tm_sec)])
          '''创建当前日期和当前时间目录'''
          path = os.path.dirname(os.path.abspath(__file__))
          dateDir = os.path.join(path,str1)
          #如果当前日期目录不存的话就创建
          if not os.path.exists(dateDir):
                os.mkdir(dateDir)
          timeDir= os.path.join(dateDir,str2)
          #如果当前时间目录不存的话就创建
          if not os.path.exists(timeDir):
                os.mkdir(timeDir)
          return timeDir

    def takeScreenshot(driver,savePath,pictureName):
        picturePath = os.path.join(savePath, pictureName+'.png')
        try:
            driver.get_screenshot_as_file(picturePath)
        except Exception  as e:
            print(traceback.print_exc())

    def seeWait(self,type,text,time1,time2):
        if type=="ID":
            loginstr=(By.ID,text)
            ww(webdriver,time1,time2).until(ec.presence_of_element_located(loginstr))
        elif type=="NAME":
            loginstr=(By.NAME,text)
            ww(webdriver,time1,time2).until(ec.presence_of_element_located(loginstr))
        elif type=="XPATH":
            loginstr=(By.XPATH,text)
            ww(webdriver,time1,time2).until(ec.presence_of_element_located(loginstr))
        elif type=="LINK_TEXT":
            loginstr=(By.LINK_TEXT,text)
            ww(self.dr,time1,time2).until(ec.presence_of_element_located(loginstr))
        elif type=="PARTIAL_LINK_TEXT":
            loginstr=(By.PARTIAL_LINK_TEXT,text)
            ww(webdriver,time1,time2).until(ec.presence_of_element_located(loginstr))

    def wait(self,number):
        time.sleep(number)

    def switchFrame(self,frameid):
        self.dr.switch_to.frame(frameid)

    def switchAlert(self,flag):
        if(flag):
            self.dr.switch_to.alert.accept()
        else:
            self.dr.switch_to.alert.dismiss()

    def moveElement(self,type,value):
        gt=self.localElement(type,value)
        ActionChains(self.dr).move_to_element(gt).perform()