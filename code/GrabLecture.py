#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: zengphil
# @Date:   2016-03-20 16:36:35
# @Last Modified by:   fibears
# @Last Modified time: 2016-03-25 19:14:49

# Load packages
import time
import urllib
import urllib2
import cookielib
import re
import sys
import random
import lxml

from agents import AGENTS
from lxml.html import parse

class GrabLecture(object):
    """docstring for GrabLecture"""
    def __init__(self):
        self.user_agent = random.choice(AGENTS)
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
            print("-------------分割线------------")
            # Exit python and print information.
            self.PrintInformation()
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

    def PrintInformation(self):
        # Print SelectedLectures Information
        opener = self.getOpener()
        NewResponse = opener.open(self.LectureUrl).read().decode('utf-8')
        parsed = lxml.html.fromstring(NewResponse)
        SelectedLecture = parsed.xpath("//td/a[contains(@onclick, 'Cancel')]/../../td[2]/text()")
        Speaker = parsed.xpath("//td/a[contains(@onclick, 'Cancel')]/../../td[3]/text()")
        LectureLocation = parsed.xpath("//td/a[contains(@onclick, 'Cancel')]/../../td[5]/text()")
        LectureTime = parsed.xpath("//td/a[contains(@onclick, 'Cancel')]/../../td[6]/text()")
        if len(SelectedLecture) == 0:
            print "You haven't reserved any lecture."
        if len(SelectedLecture) != 0:
            print "You have reserved", len(SelectedLecture), "lectures!!!"
            print "More details......"
            for i in range(0, len(SelectedLecture)):
                print "-------------","Lecture", i+1, "--------------"
                print "Name", ':', SelectedLecture[i]
                print "Speaker", ":", Speaker[i]
                print "Location", ':', LectureLocation[i]
                print "Time", ':', LectureTime[i]



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
        # Print information
        self.PrintInformation()


if __name__ == '__main__':
    robot = GrabLecture()
    robot.start()







