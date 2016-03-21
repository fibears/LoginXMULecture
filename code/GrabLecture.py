#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: zengphil
# @Date:   2016-03-20 16:36:35
# @Last Modified by:   fibears
# @Last Modified time: 2016-03-21 10:22:02

# Load packages
import time
import urllib
import urllib2
import cookielib
import re
from lxml.html import parse

class GrabLecture(object):
    """docstring for GrabLecture"""
    def __init__(self):
        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:44.0) Gecko/20100101 Firefox/44.0'
        self.headers = {'User-Agent': self.user_agent}
        self.LectureUrl = 'http://event.wisesoe.com/LectureOrder.aspx'


    def getOpener(self):
        cookie = cookielib.MozillaCookieJar()
        cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        return opener

    def getParsed(self):
        opener = self.getOpener()
        parsed = parse(opener.open(self.LectureUrl))
        return parsed

    def getPostdata(self):
        parsed = self.getParsed()
        # construct regex to extract JSLink of Reservation
        pattern = re.compile(r"javascript:__doPostBack\('(.*?)','(.*?)'\)")
        # replace 'cancel' to 'success'
        # JSLink = parsed.xpath('//td/a[contains(@name, "cancel")]/@href')[0]
        JSLink = parsed.xpath('//td/a[contains(@id, "btnreceive")]/@href')[0]

        # Extract the parameters from html
        ViewState = parsed.xpath('//input[@name="__VIEWSTATE"]/@value')[0]
        ViewStateGenerator = parsed.xpath('//input[@name=__VIEWSTATEGENERATOR]/@value')
        ViewStateEncrypted = parsed.xpath('//input[@name=__VIEWSTATEENCRYPTED]/@value')
        EventValidation = parsed.xpath('//input[@name="__EVENTVALIDATION"]/@value')[0]
        EventTarget = pattern.match(JSLink).groups()[0]
        EventArgument = pattern.match(JSLink).groups()[1]

        # Create PostData
        PostData = urllib.urlencode({
            '__EVENTTARGET': EventTarget,
            '__EVENTARGUMENT': EventArgument,
            '__VIEWSTATE': ViewState,
            '__VIEWSTATEGENERATOR': ViewStateGenerator,
            '__VIEWSTATEENCRYPTED': ViewStateEncrypted,
            '__EVENTVALIDATION': EventValidation
            })
        return PostData

    def start(self):
        self.headers.update({
            'Host': 'event.wisesoe.com',
            'Referer': 'http://event.wisesoe.com/Authenticate.aspx?returnUrl=/LectureOrder.aspx',
            'Connection': 'keep-alive'
            })
        opener = self.getOpener()
        PostData = self.getPostdata()
        QKRequest = urllib2.Request(self.LectureUrl, PostData, self.headers)
        response = opener.open(QKRequest)


if __name__ == '__main__':
    robot = GrabLecture()
    robot.start()













