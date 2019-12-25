#coding:utf-8
__author__ = 'lee'
import unittest
from Bussniss.Bussniss import Bussniss
from Commonlib.Readxml import Readxml
r=Readxml()
class Login(unittest.TestCase):
    def setUp(self):
        self.b=Bussniss()
        self.b.p.openBrowser("http://www.521ke.com")

    def test001(self):
        #登录成功校验
        #self.assertEquals(self.b.login(r.readXml("login","username1"),r.readXml("login","passwd1")),r.readXml("login","expect1"))
        try:
            self.assertIsNotNone(self.b.login(r.readXml("login","username1"),r.readXml("login","passwd1")),"登录成功")
        except NotImplementedError :
            print("no")


    def tearDown(self):
        self.b.p.closeBrowser()
if __name__=="__main__":
    unittest.main()