# -*- coding: utf-8 -*-

import time
import sys
import json
import urllib
import urllib2
import cookielib
import random
import lxml
import re
import webbrowser

from lxml.html import parse
from agents import AGENTS
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Widget(object):

    def __init__(self):
        # choose a user_agent from AGENTS randomly
        self.user_agent = random.choice(AGENTS)
        # Construct headers file
        self.headers = {'User-Agent': self.user_agent}
        # Default URL
        self.LectureUrl = 'http://event.wisesoe.com/LectureOrder.aspx'
        self.cookie = cookielib.MozillaCookieJar()

    def setupUi(self, Widget):
        Widget.setObjectName(_fromUtf8("Widget"))
        Widget.resize(529, 341)
        Widget.setAutoFillBackground(True)
        self.verticalLayoutWidget_2 = QtGui.QWidget(Widget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(220, 60, 301, 251))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setMargin(11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.textBrowser = QtGui.QTextBrowser(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("KaiTi"))
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.verticalLayoutWidget_3 = QtGui.QWidget(Widget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 511, 31))
        self.verticalLayoutWidget_3.setObjectName(_fromUtf8("verticalLayoutWidget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(11, 1, 11, 1)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_6 = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_3.addWidget(self.label_6)
        self.gridLayoutWidget = QtGui.QWidget(Widget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 60, 211, 251))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setMargin(11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.commandLinkButton_3 = QtGui.QCommandLinkButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commandLinkButton_3.sizePolicy().hasHeightForWidth())
        self.commandLinkButton_3.setSizePolicy(sizePolicy)
        self.commandLinkButton_3.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.commandLinkButton_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.commandLinkButton_3.setIconSize(QtCore.QSize(16, 16))
        self.commandLinkButton_3.setAutoDefault(False)
        self.commandLinkButton_3.setDefault(False)
        self.commandLinkButton_3.setObjectName(_fromUtf8("commandLinkButton_3"))
        self.gridLayout_2.addWidget(self.commandLinkButton_3, 6, 1, 1, 1)
        # Author Button #
        self.commandLinkButton_3.clicked.connect(self.Author)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.commandLinkButton = QtGui.QCommandLinkButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commandLinkButton.sizePolicy().hasHeightForWidth())
        self.commandLinkButton.setSizePolicy(sizePolicy)
        self.commandLinkButton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.commandLinkButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.commandLinkButton.setIconSize(QtCore.QSize(16, 16))
        self.commandLinkButton.setAutoDefault(False)
        self.commandLinkButton.setDefault(False)
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.gridLayout_2.addWidget(self.commandLinkButton, 4, 1, 1, 1)
        # DropLink Button #
        self.commandLinkButton.clicked.connect(self.DropLink)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.commandLinkButton_2 = QtGui.QCommandLinkButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commandLinkButton_2.sizePolicy().hasHeightForWidth())
        self.commandLinkButton_2.setSizePolicy(sizePolicy)
        self.commandLinkButton_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.commandLinkButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.commandLinkButton_2.setIconSize(QtCore.QSize(16, 16))
        self.commandLinkButton_2.setAutoDefault(False)
        self.commandLinkButton_2.setDefault(False)
        self.commandLinkButton_2.setObjectName(_fromUtf8("commandLinkButton_2"))
        self.gridLayout_2.addWidget(self.commandLinkButton_2, 5, 1, 1, 1)
        # MoreDetails Button #
        self.commandLinkButton_2.clicked.connect(self.MoreDetails)
        self.lineEdit = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 4, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setInputMask(_fromUtf8(""))
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout_2.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.pushButton = QtGui.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_2.addWidget(self.pushButton, 2, 1, 1, 1)
        # GetCookie Button #
        self.pushButton.clicked.connect(self.GetCookies)
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 5, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 6, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_2.addWidget(self.label_8, 3, 0, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.gridLayout_2.addWidget(self.pushButton_2, 3, 1, 1, 1)
        # GrabLecture Button #
        self.pushButton_2.clicked.connect(self.Selected)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(_translate("Widget", "Widget", None))
        self.label_6.setText(_translate("Widget", "XMU WISE&SOE LECTURE ROBOT", None))
        self.commandLinkButton_3.setText(_translate("Widget", "Fibears", None))
        self.label_2.setText(_translate("Widget", "PassWord", None))
        self.label.setText(_translate("Widget", "UserName", None))
        self.commandLinkButton.setText(_translate("Widget", "DropLink", None))
        self.label_3.setText(_translate("Widget", "Step1.", None))
        self.commandLinkButton_2.setText(_translate("Widget", "MoreDetails", None))
        self.label_4.setText(_translate("Widget", "DropLink", None))
        self.pushButton.setText(_translate("Widget", "GetCookie", None))
        self.label_5.setText(_translate("Widget", "MoreDetails", None))
        self.label_7.setText(_translate("Widget", "Author", None))
        self.label_8.setText(_translate("Widget", "Step2.", None))
        self.pushButton_2.setText(_translate("Widget", "GrabLecture", None))

    def DropLink(self):
        webbrowser.open('http://event.wisesoe.com/')

    def MoreDetails(self):
        webbrowser.open('http://fibears.top/2016/03/21/LectureRobot/')

    def Author(self):
        webbrowser.open('https://github.com/fibears')

    def GetCookies(self):
        self.textBrowser.append("Crawl the cookie......")
        print("Crawl the cookie......")
        # filename = 'cookie.txt'
        # cookie = cookielib.MozillaCookieJar(filename)
        # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))
        # Part1. 构建PostData，第一步输入Post的数据：用户名,密码和时间戳
        TimeStamp1 = int(time.time()*1000)
        TimeStamp1Data = urllib.urlencode({
            'UserName': self.lineEdit,
            'Password': self.lineEdit_2,
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
        # cookie.save(ignore_discard=True, ignore_expires=True)
        self.textBrowser.append("The cookie is saved on your computer!")
        self.textBrowser.append("Next step......")
        self.textBrowser.append("GrabLecture from website.")
        self.textBrowser.append("------------------------------------")
        self.textBrowser.append("Please Click GrabLecture Button!")
        self.textBrowser.append("------------------------------------")
        print("The cookie is saved on your computer!")
        print("Next step =====> GrabLecture from website.")
        return self.cookie


    # Define the opener
    def getOpener(self):
        # Create MozillaCookieJar Object
        cookie = self.cookie
        # Load cookie.txt file
        # cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
        # Construct opener processor
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        return opener

    # Get the html parsed result
    def getParsed(self):
        opener = self.getOpener()
        # Parse the response file by lxml.html.parse Method
        parsed = parse(opener.open(self.LectureUrl))
        return parsed

    # Construct the PostData from parsed result
    def getPostdata(self):
        parsed = self.getParsed()
        # construct regex to extract Reservation Javascript Link
        pattern = re.compile(r"javascript:__doPostBack\('(.*?)','(.*?)'\)")
        # The link of cancelling reservation.
        # JSLink = parsed.xpath('//td/a[contains(@onclick, "Cancel")]/@href')

        JSLink = parsed.xpath('//td/a[contains(@id, "btnreceive")]/@href')
        # check whether JSLink exists
        if JSLink == []:
            self.textBrowser.append("Sorry!!!")
            self.textBrowser.append("No Seminar is active at present!")
            self.textBrowser.append("Bye-Bye!")
            self.textBrowser.append("------------------------------------")
            self.textBrowser.append("--------- Final Result ---------")
            self.textBrowser.append("------------------------------------")
            print("Sorry!!!=======>No Seminar is active at present!")
            print("Bye-Bye!")
            print("-------------分割线------------")
            # Print information and Exit python.
            self.PrintInformation()
            #sys.exit()

        # TO GET PostData
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

    # Define Information Printing Function
    def PrintInformation(self):
        """Print SelectedLectures Information"""
        opener = self.getOpener()
        NewResponse = opener.open(self.LectureUrl).read().decode('utf-8')
        parsed = lxml.html.fromstring(NewResponse)
        # Extract Information of Reserved Lectures
        SelectedLecture = parsed.xpath("//td/a[contains(@onclick, 'Cancel')]/../../td[2]/text()")
        Speaker = parsed.xpath("//td/a[contains(@onclick, 'Cancel')]/../../td[3]/text()")
        LectureLocation = parsed.xpath("//td/a[contains(@onclick, 'Cancel')]/../../td[5]/text()")
        LectureTime = parsed.xpath("//td/a[contains(@onclick, 'Cancel')]/../../td[6]/text()")
        if len(SelectedLecture) == 0:
            self.textBrowser.append("You haven't reserved any lecture...")
            print "You haven't reserved any lecture."
        if len(SelectedLecture) != 0:
            self.textBrowser.append("You have reserved " + str(len(SelectedLecture)) + " lectures!!!")
            self.textBrowser.append("More details......")
            print "You have reserved", len(SelectedLecture), "lectures!!!"
            print "More details......"
            for i in range(0, len(SelectedLecture)):
                self.textBrowser.append("------ Lecture ", str(i+1), "------")
                self.textBrowser.append("Name: " + SelectedLecture[i])
                self.textBrowser.append("Speaker: " + Speaker[i])
                self.textBrowser.append("Location: " + LectureLocation[i])
                self.textBrowser.append("Time: " + LectureTime[i])
                print "-------------","Lecture", i+1, "--------------"
                print "Name", ':', SelectedLecture[i]
                print "Speaker", ":", Speaker[i]
                print "Location", ':', LectureLocation[i]
                print "Time", ':', LectureTime[i]

    def Selected(self):
        Headers = self.headers
        Headers.update({
            'Host': 'event.wisesoe.com',
            'Referer': 'http://event.wisesoe.com/Authenticate.aspx?returnUrl=/LectureOrder.aspx',
            'Connection': 'keep-alive'
            })
        self.textBrowser.append("The robot is starting!!!")
        print("The robot is starting!!!")
        print("Searching active seminar...........")
        opener = self.getOpener()
        self.textBrowser.append("Searching......")
        PostData = self.getPostdata()
        for i in range(0, len(PostData)):
            Data = PostData[i]
            QKRequest = urllib2.Request(self.LectureUrl, Data, Headers)
            response = opener.open(QKRequest)
            self.textBrowser.append("Congratulation!!!")
            self.textBrowser.append("You have reserved one seminar!!!")
            print("Congratulation!!!You have reserved one seminar!!!")
        # Print information
        self.PrintInformation()
        self.textBrowser.append("------------------------------------")
        self.textBrowser.append("--------- Ending Line ---------")
        self.textBrowser.append("------------------------------------")

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Widget = QtGui.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())

