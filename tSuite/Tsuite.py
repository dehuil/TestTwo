#coding:utf-8
__author__ = 'lee'
import unittest
from Commonlib.CreateReporter import CreaterReporter
from Commonlib.send import SendEmail
c=CreaterReporter()
S=SendEmail()
class Tsuite(unittest.TestCase):
    def testT(self):
        from testFrame import testlogin
        Tsuite1=unittest.TestSuite()#声明测试套
        Tsuite1.addTest(unittest.makeSuite(testlogin.Login))#添加测试类
        #unittest.TextTestRunner(verbosity=2).run(Tsuite1)#运行测试套并生成测试报告
        c.createReporter(Tsuite1)
        S.sendEmail("../Reporter/yhd.htm")
if __name__=="__main__":
    unittest.main()