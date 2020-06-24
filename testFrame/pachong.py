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
data={"taskStep":"0","page":1,"limit":20,"offset":0,"sort":"createTime","order":"desc","sourceType":"0"}
data=json.dumps(data)
url='http://dev-gate.rishis.cn/qstore/entry/findPaperCenterListByParam'
url1='http://dev-gate.rishis.cn/qstore/paperStru/getPaperPrevByPaperId?paperId={}'
paperids=[]
ques=[]

'''
    1用户循环
    2试卷循环
    3
'''
def get_paper():
    while True:
        count=0
        arr=[]
        for user in users.items():
            for i in user:
                arr.append(i)
            userkey=arr[count*2]
            headers = {
                'Accept':'application/json, text/plain, */*',
                'Connection': 'keep-alive',
                'Content-Type':'application/json;charset=UTF-8',
                'Authorization':get_cookies(userkey)}
            global url1
            f=open('./data.txt','w+')
            res=rq.post(url=url,data=data,headers=headers)
            print(res.text)
            time.sleep(5)
            try:
                for ids in json.loads(res.text)['data']['rows']:
                    id=ids['papersId']
                    res = rq.get(url1.format(id),data=data, headers=headers)
                    time.sleep(5)
                    soup = BeautifulSoup(res.text, 'html.parser')
                    try:
                        # print(soup.find_all('p'))
                        for p in soup.find_all('p'):
                            f.write(str(p)+'\n')
                    except Exception as e:
                        print(e)
                f.close()
            except Exception as e:
                print(e)
        count+=1
        if count>len(users):
            count=0

if __name__ == '__main__':
    get_paper()