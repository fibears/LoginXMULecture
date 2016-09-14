# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import time
import sys
import json
import urllib
import urllib2
import cookielib
import random
import lxml
import re

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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(404, 353)
        self.formLayoutWidget = QtGui.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 50, 238, 171))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.formLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtGui.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setInputMask(_fromUtf8(""))
        self.lineEdit_2.setText(_fromUtf8(""))
        self.lineEdit_2.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_4 = QtGui.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.pushButton = QtGui.QPushButton(self.formLayoutWidget)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.pushButton)
        # add #
        self.pushButton.clicked.connect(self.GetCookies)
        self.label_5 = QtGui.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.pushButton_2 = QtGui.QPushButton(self.formLayoutWidget)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.pushButton_2)
        # add #
        self.pushButton_2.clicked.connect(self.Selected)
        self.label_10 = QtGui.QLabel(self.formLayoutWidget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_10)
        self.label_11 = QtGui.QLabel(self.formLayoutWidget)
        self.label_11.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.label_11)
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(100, 10, 201, 41))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.verticalLayoutWidget_2 = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(80, 220, 251, 130))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_7 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_2.addWidget(self.label_7)
        self.label_6 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_8 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout_2.addWidget(self.label_8)
        self.label_9 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout_2.addWidget(self.label_9)
        self.textBrowser = QtGui.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(250, 50, 151, 171))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "UserName", None))
        self.label_2.setText(_translate("Dialog", "Password", None))
        self.label_4.setText(_translate("Dialog", "Step1", None))
        self.pushButton.setText(_translate("Dialog", "LOGIN", None))
        self.label_5.setText(_translate("Dialog", "Step2", None))
        self.pushButton_2.setText(_translate("Dialog", "Selected!!!", None))
        self.label_10.setText(_translate("Dialog", "Drop Link", None))
        self.label_11.setText(_translate("Dialog", "http://event.wisesoe.com/", None))
        self.label_3.setText(_translate("Dialog", "     XMU WISE&SOE LECTURE", None))
        self.label_7.setText(_translate("Dialog", "Instruction:", None))
        self.label_6.setText(_translate("Dialog", "Step1: You should login your account;", None))
        self.label_8.setText(_translate("Dialog", "Step2: Click Selected Button;", None))
        self.label_9.setText(_translate("Dialog", "Done!", None))

    def GetCookies(self):
        self.textBrowser.append("Crawl the cookie......")
        print("Crawl the cookie......")
        filename = 'cookie.txt'
        cookie = cookielib.MozillaCookieJar(filename)
        # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        # Part1. 构建PostData，第一步输入Post的数据：用户名,密码和时间戳
        TimeStamp1 = int(time.time()*1000)
        TimeStamp1Data = urllib.urlencode({
            'UserName': self.label,
            'Password': self.label_2,
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
        self.textBrowser.append("The cookie is saved on your computer!")
        self.textBrowser.append("Next step =====> GrabLecture from website.")
        print("The cookie is saved on your computer!")
        print("Next step =====> GrabLecture from website.")
        return cookie

    def Selected(self):
        robot = GrabLecture()
        Headers = robot.headers
        Headers.update({
            'Host': 'event.wisesoe.com',
            'Referer': 'http://event.wisesoe.com/Authenticate.aspx?returnUrl=/LectureOrder.aspx',
            'Connection': 'keep-alive'
            })
        self.textBrowser.append("The robot is starting!!!")
        self.textBrowser.append("Searching active seminar...........")
        print("The robot is starting!!!")
        print("Searching active seminar...........")
        opener = robot.getOpener()
        PostData = robot.getPostdata()
        for i in range(0, len(PostData)):
            Data = PostData[i]
            QKRequest = urllib2.Request(robot.LectureUrl, Data, Headers)
            response = opener.open(QKRequest)
            self.textBrowser.append("Congratulation!!!You have reserved one seminar!!!")
            print("Congratulation!!!You have reserved one seminar!!!")
        # Print information
        robot.PrintInformation()
        #robot.start()

class GrabLecture(object):
    """docstring for GrabLecture"""

    def __init__(self):
        # choose a user_agent from AGENTS randomly
        self.user_agent = random.choice(AGENTS)
        # Construct headers file
        self.headers = {'User-Agent': self.user_agent}
        # Default URL
        self.LectureUrl = 'http://event.wisesoe.com/LectureOrder.aspx'

    # Define the opener
    def getOpener(self):
        # Create MozillaCookieJar Object
        cookie = cookielib.MozillaCookieJar()
        # Load cookie.txt file
        cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
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

    # Main Function
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


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

