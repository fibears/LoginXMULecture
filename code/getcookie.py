#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: zengphil
# @Date:   2016-03-20 18:36:34
# @Last Modified by:   zengphil
# @Last Modified time: 2016-03-20 18:41:40

import time
import sys
import json
import urllib
import urllib2
import cookielib

# 设置保存cookie的文件
firename = 'cookie.txt'
# 创建MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(firename)
# 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# Part1. 构建PostData，第一步输入Post的数据：用户名和密码
UserData = urllib.urlencode({
    'UserName': sys.argv[1],
    'Password': sys.argv[2]
})
urlLogon = 'http://event.wisesoe.com/Logon.aspx'
result1 = opener.open(urlLogon, UserData)
# 此时已经获取到部分cookie值

# Part2.
TimeStamp1 = int(time.time()*1000)
TimeStamp1Data = urllib.urlencode({
    'UserName': sys.argv[1],
    'Password': sys.argv[2],
    '_': TimeStamp1
    })

urltoken = 'http://account.wisesoe.com/WcfServices/SSOService.svc/Account/Logon?' + TimeStamp1Data
result2 = opener.open(urltoken).read()

# Part 3.
TimeStamp2 = int(time.time()*1000)
TimeStamp2Data = urllib.urlencode({
    '_' : TimeStamp2
    })
urlRequestToken = 'http://account.wisesoe.com/WcfServices/SSOService.svc/Account/RequestToken?' + TimeStamp2Data
result3 = opener.open(urlRequestToken).read()
token = json.loads(result3)['Token']

# Part 4.
AuthUrl = 'http://event.wisesoe.com/Authenticate.aspx'
TokenData = urllib.urlencode({
    'token': str(token)
    })
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3)',
    'Referer': 'http://event.wisesoe.com/Authenticate.aspx?returnUrl=Default.aspx',
    'X-Requested-With': 'XMLHttpRequest'
}
request = urllib2.Request(AuthUrl, TokenData, headers)
result4 = opener.open(request)
cookie.save(ignore_discard=True, ignore_expires=True)




