#coding:utf-8
__author__ = 'zcs'
import HTMLTestRunner
class CreaterReporter():
    def createReporter(self,mysuite):
        filepath="../Reporter/yhd.htm"
        with open(filepath,'wb') as ftm:
            HTMLTestRunner.HTMLTestRunner(
                stream=ftm,
                verbosity=2,
                title=u"一号店测试报告",
                description=u"登录和查价测试报告"
        ).run(mysuite)

