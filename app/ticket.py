# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(427, 355)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralWidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(240, 10, 160, 131))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setMargin(11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.textBrowser = QtGui.QTextBrowser(self.verticalLayoutWidget_2)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.formLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(30, 10, 211, 131))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setMargin(11)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.formLayoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.textEdit = QtGui.QTextEdit(self.formLayoutWidget)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.textEdit)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.textEdit_2 = QtGui.QTextEdit(self.formLayoutWidget)
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.textEdit_2)
        self.pushButton_3 = QtGui.QPushButton(self.formLayoutWidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.pushButton_3)
        self.line = QtGui.QFrame(self.formLayoutWidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.line)
        self.pushButton_2 = QtGui.QPushButton(self.formLayoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.pushButton_2)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 427, 22))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "UserName", None))
        self.label_2.setText(_translate("MainWindow", "Password", None))
        self.pushButton_3.setText(_translate("MainWindow", "Login", None))
        self.pushButton_2.setText(_translate("MainWindow", "抢讲座", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

