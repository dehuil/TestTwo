__author__ = 'lee'
#coding=utf-8
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import  datetime
import schedule
import os
import time
import yagmail
path=os.getcwd()
if os.path.exists(path+'/gaokaodaojishi.zip'):
    os.remove(path+'/gaokaodaojishi.zip')
if os.path.exists(path+'/gaokaodaojishi'):
    os.system('rm -rf gaokaodaojishi/')
if os.path.exists(path+'/result.jtl'):
    os.remove(path+'/result.jtl')
def send():
    sender = '616798887@qq.com'
    password = 'qhsjktvnndarbdig'
    res = '56844906@qq.com'
    yag = yagmail.SMTP(user=sender, password=password, host='smtp.qq.com', smtp_ssl=True)
    content = '{}/gaokaodaojishi.zip'.format(path)
    yag.send(to=res,
             subject='高考倒计时压测报告',
             contents=content)

def job1():
    os.system(r'jmeter -n -t test1.jmx -l result.jtl -e -o gaokaodaojishi')
def job2():
    os.system('zip -r gaokaodaojishi.zip gaokaodaojishi')
schedule.every().day.at("15:33").do(job1)
schedule.every().day.at("15:34").do(job2)
schedule.every().day.at("15:35").do(send)
while True:
    schedule.run_pendin