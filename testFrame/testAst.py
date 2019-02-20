#coding:utf-8
__author__ = 'zcs'
import unittest
from Bussniss.Bussniss import Bussniss
class Tt(unittest.TestCase):
    def setUp(self):
        self.b=Bussniss()
        self.b.p.openBrowser("http://www.yhd.com")
    def tearDown(self):
        self.b.p.closeBrowser()
    def test001(self):
        self.assertEquals("acd","afd")
    def test003(self):
        self.assertEquals(self.b.searchPrice(u"Apple 苹果 iPhone 7 (A1660) 32G 玫瑰金色 移动联通电信4G手机"),"4988")
if __name__=="__main__":
    unittest.main()
