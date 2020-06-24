__author__ = 'lee'
#coding=utf-8
import time
import chardet
import json
import requests as rq
from bs4 import BeautifulSoup
import os
from testFrame.paperIn import get_cookies

#  body > div.topReadContent > div > div.readDetail > div.read_chapterName.tc > h1
users={'lidehui':'111111','caoxianglan':'111111','mahaoxin':'15036119602'}
data={"gradeType":"","status":"null","taskStep":"0","page":1,"limit":200,"offset":0,"sort":"getTime","order":"desc"}
data=json.dumps(data)
url='http://dev-gate.rishis.cn/qstore/entry/findPaperCenterListByParam'
url1='http://dev-gate.rishis.cn/qstore/paperStru/getPaperPrevByPaperId?paperId={}'
paperids=[]
ques=[]

'''
    1获取试卷id列表
    2循环拼接 获取试卷内容
'''
def get_paper1():
        headers = {
            'Accept':'application/json, text/plain, */*',
            'Connection': 'keep-alive',
            'Content-Type':'application/json;charset=UTF-8',
            'Authorization':'Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIzNzI5MTY5ODI0MTU0ODI4OCIsImlhdCI6MTU5Mjg5MTMyNiwiaXNzIjoic3NvIiwibmJmIjoxNTkyODkxMzI2LCJleHAiOjE1OTI5MjAxMjZ9.hMgRJJCU_xszKw19o0mzGPeEHPhcrFzXzbD3dTaBGeE'}
        global url1
        f=open('./data.txt','w+')
        res=rq.post(url=url,data=data,headers=headers)
        print(res.text)
        time.sleep(10)
        try:
            for ids in json.loads(res.text)['data']['rows']:
                id=ids['papersId']
                res = rq.get(url1.format(id),data=data, headers=headers)
                time.sleep(10)
                soup = BeautifulSoup(res.text, 'html.parser')
                try:
                    for p in soup.find_all('p'):
                        f.write(str(p)+'\n')
                except Exception as e:
                    print(e)
            f.close()
        except Exception as e:
            print(e)

if __name__ == '__main__':
    get_paper1()