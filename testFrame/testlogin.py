#coding:utf-8
__author__ = 'zcs'
import unittest
from Bussniss.Bussniss import Bussniss
from Commonlib.Readxml import Readxml
r=Readxml()
class Login(unittest.TestCase):
    def setUp(self):
        self.b=Bussniss()
        self.b.p.openBrowser("http://www.yhd.com")
    def tearDown(self):
        self.b.p.closeBrowser()
    def test001(self):
        print r.readXml("login","username1")
        self.assertEquals(self.b.login(r.readXml("login","username1"),r.readXml("login","passwd1")),r.readXml("login","expect1"))
    def test002(self):
        self.assertEquals(self.b.login(r.readXml("login","username2"),r.readXml("login","passwd2")),r.readXml("login","expect2"))

if __name__=="__main__":
    unittest.main()

