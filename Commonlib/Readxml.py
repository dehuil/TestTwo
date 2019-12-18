#coding:utf-8
__author__ = 'zcs'
from xml.dom import minidom
class Readxml():
    def readXml(self,Onenode,Twonode):
        root=minidom.parse("../DataShare/kcb.xml")
        firstnode=root.getElementsByTagName(Onenode)[0]
        try:
            secondnode=firstnode.getElementsByTagName(Twonode)[0].firstChild.data
        except:
            secondnode=""
        return secondnode
