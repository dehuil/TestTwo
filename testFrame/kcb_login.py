#coding:utf-8
__author__ = 'zcs'
import unittest
from Bussniss.Bussniss import Bussniss
from Commonlib.Readxml import Readxml
r=Readxml()
class Login(unittest.TestCase):
    def setUp(self):
        self.b=Bussniss()
        self.b.p.openBrowser("http://www.521ke.com")

    def test001(self):
        self.assertEquals(self.b.login(r.readXml("login","username1"),r.readXml("login","passwd1")),r.readXml("login","expect1"))


    def tearDown(self):
        self.b.p.closeBrowser()
if __name__=="__main__":
    unittest.main()