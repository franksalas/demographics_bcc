# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo.ui'
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
        Dialog.resize(400, 300)
        self.title = QtGui.QLabel(Dialog)
        self.title.setGeometry(QtCore.QRect(20, 10, 351, 71))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(False)
        font.setWeight(50)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName(_fromUtf8("title"))
        self.messageLabel = QtGui.QLabel(Dialog)
        self.messageLabel.setGeometry(QtCore.QRect(40, 90, 321, 31))
        self.messageLabel.setText(_fromUtf8(""))
        self.messageLabel.setObjectName(_fromUtf8("messageLabel"))
        self.messageLabel_2 = QtGui.QLabel(Dialog)
        self.messageLabel_2.setGeometry(QtCore.QRect(40, 130, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.messageLabel_2.setFont(font)
        self.messageLabel_2.setText(_fromUtf8(""))
        self.messageLabel_2.setObjectName(_fromUtf8("messageLabel_2"))
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(40, 220, 307, 43))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(-1, 10, 0, 10)
        self.horizontalLayout.setSpacing(40)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.buttonLoad = QtGui.QPushButton(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonLoad.sizePolicy().hasHeightForWidth())
        self.buttonLoad.setSizePolicy(sizePolicy)
        self.buttonLoad.setObjectName(_fromUtf8("buttonLoad"))
        self.horizontalLayout.addWidget(self.buttonLoad)
        self.buttonConvert = QtGui.QPushButton(self.widget)
        self.buttonConvert.setObjectName(_fromUtf8("buttonConvert"))
        self.horizontalLayout.addWidget(self.buttonConvert)
        self.buttonExit = QtGui.QPushButton(self.widget)
        self.buttonExit.setObjectName(_fromUtf8("buttonExit"))
        self.horizontalLayout.addWidget(self.buttonExit)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.title.setText(_translate("Dialog", "Demographics Chane Report", None))
        self.buttonLoad.setText(_translate("Dialog", "Load", None))
        self.buttonConvert.setText(_translate("Dialog", "Convert", None))
        self.buttonExit.setText(_translate("Dialog", "Exit", None))

