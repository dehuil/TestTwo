#coding:utf-8
import requests
import unittest
class kcbDemo(unittest.TestCase):

        def test1(self):
                url="http://lan.dinsmooth.com"
                headers={"Content-Type":"application/json"}
                data={"username":"lidehu",
                        "password":111111,
                }
                r=requests.post(url,data=data,headers=headers)
                self.assertFalse(r.status_code==400,"密码错误")

        def test2(self):
                print