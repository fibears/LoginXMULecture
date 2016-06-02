# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
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
        self.label_5 = QtGui.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_5)
        self.pushButton_2 = QtGui.QPushButton(self.formLayoutWidget)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.pushButton_2)
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


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

