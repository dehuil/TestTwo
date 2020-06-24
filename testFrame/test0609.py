__author__ = 'lee'
#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import json

caps = {
    'browserName': 'chrome',
    'loggingPrefs': {
        'browser': 'ALL',
        'driver': 'ALL',
        'performance': 'ALL',
    },
    'goog:chromeOptions': {
        'perfLoggingPrefs': {
            'enableNetwork': True,
        },
        'w3c': False,
    },
}
driver = webdriver.Chrome(desired_capabilities=caps)

driver.get('https://partner.oceanengine.com/union/media/login/')
time.sleep(3)
request_log = driver.get_log('performance')
print(request_log)
for i in range(len(request_log)):
    message=json.loads(request_log[i]['message'])
    message=message['message']['params']
