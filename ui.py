# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Mon Sep  8 16:32:02 2014
#      by: PyQt5 UI code generator 5.3.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets


class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName("Window")
        Window.resize(215, 166)
        self.centralwidget = QtWidgets.QWidget(Window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_time1 = QtWidgets.QLabel(self.centralwidget)
        self.label_time1.setObjectName("label_time1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole,
                                  self.label_time1)
        self.label_time2 = QtWidgets.QLabel(self.centralwidget)
        self.label_time2.setObjectName("label_time2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole,
                                  self.label_time2)
        self.timeEdit1 = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit1.setObjectName("timeEdit1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole,
                                  self.timeEdit1)
        self.timeEdit2 = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit2.setObjectName("timeEdit2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole,
                                  self.timeEdit2)
        self.label_timeDiff = QtWidgets.QLabel(self.centralwidget)
        self.label_timeDiff.setObjectName("label_timeDiff")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole,
                                  self.label_timeDiff)
        self.label_timeDiffOut = QtWidgets.QLabel(self.centralwidget)
        self.label_timeDiffOut.setText("")
        self.label_timeDiffOut.setObjectName("label_timeDiffOut")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole,
                                  self.label_timeDiffOut)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 215, 21))
        self.menubar.setObjectName("menubar")
        Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Window)
        self.statusbar.setObjectName("statusbar")
        Window.setStatusBar(self.statusbar)

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Tardisff"))
        self.label_time1.setText(_translate("Window", "Time 1:"))
        self.label_time2.setText(_translate("Window", "Time 2:"))
        self.label_timeDiff.setText(_translate("Window", "Difference"))
