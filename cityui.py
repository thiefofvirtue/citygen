# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testGen.ui'
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
        MainWindow.resize(412, 724)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        MainWindow.setDocumentMode(False)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.cityOutputL = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Waree"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.cityOutputL.setFont(font)
        self.cityOutputL.setAlignment(QtCore.Qt.AlignCenter)
        self.cityOutputL.setObjectName(_fromUtf8("cityOutputL"))
        self.verticalLayout.addWidget(self.cityOutputL)
        self.cityOutput = QtGui.QTextEdit(self.centralwidget)
        self.cityOutput.setObjectName(_fromUtf8("cityOutput"))
        self.verticalLayout.addWidget(self.cityOutput)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.ctyNameL = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ctyNameL.setFont(font)
        self.ctyNameL.setObjectName(_fromUtf8("ctyNameL"))
        self.horizontalLayout.addWidget(self.ctyNameL)
        self.cityNameF = QtGui.QLineEdit(self.centralwidget)
        self.cityNameF.setMinimumSize(QtCore.QSize(0, 0))
        self.cityNameF.setSizeIncrement(QtCore.QSize(0, 0))
        self.cityNameF.setBaseSize(QtCore.QSize(0, 0))
        self.cityNameF.setObjectName(_fromUtf8("cityNameF"))
        self.horizontalLayout.addWidget(self.cityNameF)
        self.ctyTypeL = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ctyTypeL.setFont(font)
        self.ctyTypeL.setObjectName(_fromUtf8("ctyTypeL"))
        self.horizontalLayout.addWidget(self.ctyTypeL)
        self.cityTypeF = QtGui.QLineEdit(self.centralwidget)
        self.cityTypeF.setObjectName(_fromUtf8("cityTypeF"))
        self.horizontalLayout.addWidget(self.cityTypeF)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.genButtons = QtGui.QHBoxLayout()
        self.genButtons.setObjectName(_fromUtf8("genButtons"))
        self.resetCity = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.resetCity.setFont(font)
        self.resetCity.setObjectName(_fromUtf8("resetCity"))
        self.genButtons.addWidget(self.resetCity)
        self.generateCity = QtGui.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.generateCity.setFont(font)
        self.generateCity.setObjectName(_fromUtf8("generateCity"))
        self.genButtons.addWidget(self.generateCity)
        self.verticalLayout.addLayout(self.genButtons)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.resetCity, QtCore.SIGNAL(_fromUtf8("clicked()")), self.cityOutput.clear)
        QtCore.QObject.connect(self.cityNameF, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.statusbar.showMessage)
        QtCore.QObject.connect(self.cityTypeF, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.statusbar.showMessage)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.cityOutputL.setText(_translate("MainWindow", "City Output", None))
        self.ctyNameL.setText(_translate("MainWindow", "City Name", None))
        self.ctyTypeL.setText(_translate("MainWindow", "City Type", None))
        self.resetCity.setText(_translate("MainWindow", "Reset", None))
        self.generateCity.setText(_translate("MainWindow", "Generate", None))

