#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: zengphil
# @Date:   2016-03-20 16:36:35
# @Last Modified by:   fibears
# @Last Modified time: 2016-03-21 14:58:01

# Load packages
import time
import urllib
import urllib2
import cookielib
import re
import sys
from lxml.html import parse

class GrabLecture(object):
    """docstring for GrabLecture"""
    def __init__(self):
        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:44.0) Gecko/20100101 Firefox/44.0'
        self.headers = {'User-Agent': self.user_agent}
        self.LectureUrl = 'http://event.wisesoe.com/LectureOrder.aspx'

    # Define the opener
    def getOpener(self):
        cookie = cookielib.MozillaCookieJar()
        cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        return opener

    # Get the html parsed result
    def getParsed(self):
        opener = self.getOpener()
        parsed = parse(opener.open(self.LectureUrl))
        return parsed

    # Construct the PostData from parsed result
    def getPostdata(self):
        parsed = self.getParsed()
        # construct regex to extract JSLink of Reservation
        pattern = re.compile(r"javascript:__doPostBack\('(.*?)','(.*?)'\)")
        # The link of cancelling reservation.
        # JSLink = parsed.xpath('//td/a[contains(@onclick, "Cancel")]/@href')

        JSLink = parsed.xpath('//td/a[contains(@id, "btnreceive")]/@href')
        # check whether JSLink exists
        if JSLink == []:
            print("Sorry!!!=======>No Seminar is active at present!")
            print("Bye-Bye!")
            # Exit python and print information.
            sys.exit()

        PostData = []

        for i in range(0, len(JSLink)):
            link = JSLink[i]
            EventTarget = pattern.match(link).groups()[0]
            EventArgument = pattern.match(link).groups()[1]

            # Extract the parameters from html
            ViewState = parsed.xpath('//input[@name="__VIEWSTATE"]/@value')[0]
            ViewStateGenerator = parsed.xpath('//input[@name=__VIEWSTATEGENERATOR]/@value')
            ViewStateEncrypted = parsed.xpath('//input[@name=__VIEWSTATEENCRYPTED]/@value')
            EventValidation = parsed.xpath('//input[@name="__EVENTVALIDATION"]/@value')[0]

            # Create PostData
            PostData.append(urllib.urlencode({
                '__EVENTTARGET': EventTarget,
                '__EVENTARGUMENT': EventArgument,
                '__VIEWSTATE': ViewState,
                '__VIEWSTATEGENERATOR': ViewStateGenerator,
                '__VIEWSTATEENCRYPTED': ViewStateEncrypted,
                '__EVENTVALIDATION': EventValidation
                }))

        return PostData


    def start(self):
        self.headers.update({
            'Host': 'event.wisesoe.com',
            'Referer': 'http://event.wisesoe.com/Authenticate.aspx?returnUrl=/LectureOrder.aspx',
            'Connection': 'keep-alive'
            })
        print("The robot is starting!!!")
        print("Searching active seminar...........")
        opener = self.getOpener()
        PostData = self.getPostdata()
        for i in range(0, len(PostData)):
            Data = PostData[i]
            QKRequest = urllib2.Request(self.LectureUrl, Data, self.headers)
            response = opener.open(QKRequest)
            print("Congratulation!!!You have reserved one seminar!!!")


if __name__ == '__main__':
    robot = GrabLecture()
    robot.start()







