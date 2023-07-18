# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designervcbRaQ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1121, 800)
        self.widget = QWidget(MainWindow)
        self.widget.setObjectName(u"widget")
        self.footerFrame = QFrame(self.widget)
        self.footerFrame.setObjectName(u"footerFrame")
        self.footerFrame.setGeometry(QRect(9, 759, 1101, 40))
        self.footerFrame.setFrameShape(QFrame.StyledPanel)
        self.footerFrame.setFrameShadow(QFrame.Raised)
        self.creatorLabel = QLabel(self.footerFrame)
        self.creatorLabel.setObjectName(u"creatorLabel")
        self.creatorLabel.setGeometry(QRect(12, 12, 191, 16))
        self.githubLabel = QLabel(self.footerFrame)
        self.githubLabel.setObjectName(u"githubLabel")
        self.githubLabel.setGeometry(QRect(870, 10, 291, 20))
        self.githubLabel.setOpenExternalLinks(True)
        self.inputFrame = QFrame(self.widget)
        self.inputFrame.setObjectName(u"inputFrame")
        self.inputFrame.setGeometry(QRect(9, 629, 1101, 121))
        self.inputFrame.setFrameShape(QFrame.StyledPanel)
        self.inputFrame.setFrameShadow(QFrame.Raised)
        self.funcLabel = QLabel(self.inputFrame)
        self.funcLabel.setObjectName(u"funcLabel")
        self.funcLabel.setGeometry(QRect(10, 50, 261, 41))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.funcLabel.setFont(font)
        self.xRangeLabel = QLabel(self.inputFrame)
        self.xRangeLabel.setObjectName(u"xRangeLabel")
        self.xRangeLabel.setGeometry(QRect(450, 0, 201, 41))
        self.xRangeLabel.setFont(font)
        self.minLabel = QLabel(self.inputFrame)
        self.minLabel.setObjectName(u"minLabel")
        self.minLabel.setGeometry(QRect(420, 40, 71, 41))
        self.minLabel.setFont(font)
        self.maxLabel = QLabel(self.inputFrame)
        self.maxLabel.setObjectName(u"maxLabel")
        self.maxLabel.setGeometry(QRect(420, 80, 81, 41))
        self.maxLabel.setFont(font)
        self.instructionsLabel = QLabel(self.inputFrame)
        self.instructionsLabel.setObjectName(u"instructionsLabel")
        self.instructionsLabel.setGeometry(QRect(725, 15, 361, 91))
        self.instructionsLabel.setAlignment(Qt.AlignCenter)
        self.instructionsLabel.setWordWrap(True)
        self.funcInput = QLineEdit(self.inputFrame)
        self.funcInput.setObjectName(u"funcInput")
        self.funcInput.setGeometry(QRect(160, 60, 113, 21))
        self.xMinInput = QLineEdit(self.inputFrame)
        self.xMinInput.setObjectName(u"xMinInput")
        self.xMinInput.setGeometry(QRect(530, 50, 71, 21))
        self.xMaxInput = QLineEdit(self.inputFrame)
        self.xMaxInput.setObjectName(u"xMaxInput")
        self.xMaxInput.setGeometry(QRect(530, 90, 71, 21))
        self.verticalLayoutWidget = QWidget(self.widget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 9, 1101, 611))
        self.plotWidget = QVBoxLayout(self.verticalLayoutWidget)
        self.plotWidget.setObjectName(u"plotWidget")
        self.plotWidget.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.widget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.creatorLabel.setText(QCoreApplication.translate("MainWindow", u"Ahmed Ayman Saad", None))
        self.githubLabel.setText(QCoreApplication.translate("MainWindow", u"github.com/AhmedAymanSaad", None))
        self.funcLabel.setText(QCoreApplication.translate("MainWindow", u"Function", None))
        self.xRangeLabel.setText(QCoreApplication.translate("MainWindow", u"X - Range", None))
        self.minLabel.setText(QCoreApplication.translate("MainWindow", u"Min", None))
        self.maxLabel.setText(QCoreApplication.translate("MainWindow", u"Max", None))
        self.instructionsLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.funcInput.setText(QCoreApplication.translate("MainWindow", u"x", None))
        self.xMinInput.setText(QCoreApplication.translate("MainWindow", u"-5", None))
        self.xMaxInput.setText(QCoreApplication.translate("MainWindow", u"5", None))
    # retranslateUi

