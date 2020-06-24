__author__ = 'lee'
#coding=utf-8

'''1.【字符串循环左移】给定一个字符串S，要求把S的前k个字符移动到S的尾部，
如把字符串“abcdef”前面的2个字符‘a’、‘b’移动到字符串的尾部，得到新字符串“cdefab”，称作字符串循环左移k位。
输入格式:输入在第1行中给出一个不超过100个字符长度的、以回车结束的非空字符串；第2行给出非负整数N。
输出格式：在一行中输出循环左移N次后的字符串。'''

'''2.【最后一个单词】计算字符串最后一个单词的长度，单词以空格隔开。
输入格式:一行字符串，非空，长度小于5000。输出格式：整数N，最后一个单词的长度。
输入样例：
hello world
输出样例：
5
'''
#
# str=input('输入字符串'+"\n")
# list=str.split(' ')
# print(len(list[len(list)-1]))

'''9.【合并两个列表并去重】 输入两个列表alist和blist，要求列表中的每个元素都为正整数且不超过10，
合并alist和blist，并将重复的元素去掉后输出一个新的列表clist。
输入格式:共两行，每一行都用来输入列表中的元素值，以空格隔开。
输出格式：共一行，以列表形式打印输出。
输入样例：
1 2 3
4 3 2
输出样例：
[1,2,3,4]'''

# a=[1,2,3]
# b=[4,3,2]
# a=a.extend(b)
# print(a)
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import  datetime
import os
import time
import yagmail
def send():
    sender = '616798887@qq.com'     # 发送人邮箱账号
    password = 'qhsjktvnndarbdig'    # 发送人邮箱授权码，而不是邮箱密码
    res = 'hanhongmin@dinsmooth.com'
    yag = yagmail.SMTP(user=sender, password=password, host='smtp.qq.com', smtp_ssl=True)
    content = r'/root/gaokaodaojishi.zip'
    yag.send(to=res, subject='高考倒计时压测报告{}'.format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")), contents=content)

def job():
    os.system('jmeter -n -t xiaochengxu.jmx -l result -e -o gaokaodaojishi')

bs=BlockingScheduler()
bs.add_job(job,'cron',day_of_week='1-5',hour=22,minute=30)
bs.start()
time.sleep(1900)
os.system('zip -r gaokaodaojishi.zip gaokaodaojishi')
time.sleep(10)
send()