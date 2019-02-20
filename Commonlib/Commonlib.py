#coding:utf-8
__author__ = 'zcs'
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
class Commonlib():
    def __init__(self):
        self.dr=webdriver.Firefox()
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

    def waite(self,number):
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