#coding:utf-8
__author__ = 'lee'
import unittest
from Commonlib.Commonlib import Commonlib
from selenium import webdriver
from Bussniss.Bussniss import Bussniss
from Commonlib.Readxml import Readxml
from bs4 import BeautifulSoup
from selenium import webdriver
r=Readxml()
wb=webdriver.Chrome()
class Login(unittest.TestCase):
    def setUp(self):
        self.p=Commonlib()
        url="http://ques.rishis.cn/#/login"
        self.b=Bussniss()
        self.b.p.openBrowser(myurl=url)

    def test001(self):
        self.b.kcb_login("wangqiuyun","111111")
        self.p.wait(2)
        self.p.activeEvent('xpath',"//a[2]//div[1]")
        self.p.wait(2)
        self.p.activeEvent('xpath',"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/ul[1]/div[1]/li[1]/ul[1]/div[5]/a[1]/li[1]/span[1]")
        print(BeautifulSoup(wb.page_source,'html.parser'))

    def tearDown(self):
        self.b.p.closeBrowser()
        
if __name__=="__main__":
    unittest.main()