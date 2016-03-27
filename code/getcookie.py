#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: zengphil
# @Date:   2016-03-20 18:36:34
# @Last Modified by:   fibears
# @Last Modified time: 2016-03-27 23:12:35

import time
import sys
import json
import urllib
import urllib2
import cookielib
import random
from agents import AGENTS

print("Crawl the cookie......")
# 设置保存cookie的文件
firename = 'cookie.txt'
# 创建MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(firename)
# 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# Part1. 构建PostData，第一步输入Post的数据：用户名,密码和时间戳
TimeStamp1 = int(time.time()*1000)
TimeStamp1Data = urllib.urlencode({
    'UserName': sys.argv[1],
    'Password': sys.argv[2],
    '_': TimeStamp1
    })
urltoken = 'http://account.wisesoe.com/WcfServices/SSOService.svc/Account/Logon?' + TimeStamp1Data
result1 = opener.open(urltoken)

# Part 2.
TimeStamp2 = int(time.time()*1000)
TimeStamp2Data = urllib.urlencode({
    '_' : TimeStamp2
    })
urlRequestToken = 'http://account.wisesoe.com/WcfServices/SSOService.svc/Account/RequestToken?' + TimeStamp2Data
result2 = opener.open(urlRequestToken).read()
token = json.loads(result2)['Token']

# Part 3.
AuthUrl = 'http://event.wisesoe.com/Authenticate.aspx'
TokenData = urllib.urlencode({
    'token': str(token)
    })
user_agent = random.choice(AGENTS)
headers = {
    'User-Agent': user_agent,
    'Referer': 'http://event.wisesoe.com/Authenticate.aspx?returnUrl=Default.aspx',
    'X-Requested-With': 'XMLHttpRequest'
}
request = urllib2.Request(AuthUrl, TokenData, headers)
result3 = opener.open(request)
cookie.save(ignore_discard=True, ignore_expires=True)
print("The cookie is saved on your computer!")
print("Next step =====> GrabLecture from website.")




