# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GenBBS_reinf.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTableView, QVBoxLayout,
    QWidget)
import app_resources_rc
import app_resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(918, 748)
        font = QFont()
        font.setStrikeOut(False)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/images/GenBBS Logo.jpeg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        self.centralwidgetReinf = QWidget(MainWindow)
        self.centralwidgetReinf.setObjectName(u"centralwidgetReinf")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidgetReinf.sizePolicy().hasHeightForWidth())
        self.centralwidgetReinf.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.centralwidgetReinf)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame1Reinf = QFrame(self.centralwidgetReinf)
        self.frame1Reinf.setObjectName(u"frame1Reinf")
        sizePolicy.setHeightForWidth(self.frame1Reinf.sizePolicy().hasHeightForWidth())
        self.frame1Reinf.setSizePolicy(sizePolicy)
        self.frame1Reinf.setMinimumSize(QSize(700, 500))
        self.frame1Reinf.setMaximumSize(QSize(16777215, 900))
        self.frame1Reinf.setAutoFillBackground(False)
        self.frame1Reinf.setStyleSheet(u"background-color: white;")
        self.frame1Reinf.setFrameShape(QFrame.Shape.WinPanel)
        self.frame1Reinf.setFrameShadow(QFrame.Shadow.Sunken)
        self.horizontalLayout = QHBoxLayout(self.frame1Reinf)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame3Reinf = QFrame(self.frame1Reinf)
        self.frame3Reinf.setObjectName(u"frame3Reinf")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(3)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame3Reinf.sizePolicy().hasHeightForWidth())
        self.frame3Reinf.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        self.frame3Reinf.setFont(font1)
        self.frame3Reinf.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame3Reinf.setAutoFillBackground(False)
        self.frame3Reinf.setStyleSheet(u"QMainWindow {\n"
"	font: 9pt \"Titillium Web\";\n"
"}\n"
"QPushButton {\n"
"background-color: rgb(85, 170, 0);\n"
"font: 12pt ;\n"
"border-radius: 5px;\n"
"color: white;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(139, 243, 59)\n"
"}")
        self.frame3Reinf.setFrameShape(QFrame.Shape.Box)
        self.frame3Reinf.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_4 = QVBoxLayout(self.frame3Reinf)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.layout1Reinf = QHBoxLayout()
        self.layout1Reinf.setObjectName(u"layout1Reinf")
        self.labelHeaderReinf = QLabel(self.frame3Reinf)
        self.labelHeaderReinf.setObjectName(u"labelHeaderReinf")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        self.labelHeaderReinf.setFont(font2)
        self.labelHeaderReinf.setStyleSheet(u"\n"
"	\n"
"background-image: url(:/images/Reinf_Dispersed_Backdrop.jpeg);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    background-attachment: fixed;\n"
"color: black;\n"
"")
        self.labelHeaderReinf.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout1Reinf.addWidget(self.labelHeaderReinf)

        self.labelHeaderReinf2 = QLabel(self.frame3Reinf)
        self.labelHeaderReinf2.setObjectName(u"labelHeaderReinf2")
        self.labelHeaderReinf2.setFont(font2)
        self.labelHeaderReinf2.setStyleSheet(u"\n"
"	\n"
"background-image: url(:/images/Reinf_Dispersed_Backdrop.jpeg);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    background-attachment: fixed;\n"
"color: black;\n"
"")
        self.labelHeaderReinf2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout1Reinf.addWidget(self.labelHeaderReinf2)

        self.labelHeaderReinf3 = QLabel(self.frame3Reinf)
        self.labelHeaderReinf3.setObjectName(u"labelHeaderReinf3")
        self.labelHeaderReinf3.setFont(font2)
        self.labelHeaderReinf3.setStyleSheet(u"\n"
"	\n"
"background-image: url(:/images/Reinf_Dispersed_Backdrop.jpeg);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    background-attachment: fixed;\n"
"color: black;\n"
"")
        self.labelHeaderReinf3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.layout1Reinf.addWidget(self.labelHeaderReinf3)


        self.verticalLayout_4.addLayout(self.layout1Reinf)

        self.btnBackReinf = QPushButton(self.frame3Reinf)
        self.btnBackReinf.setObjectName(u"btnBackReinf")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btnBackReinf.sizePolicy().hasHeightForWidth())
        self.btnBackReinf.setSizePolicy(sizePolicy2)
        self.btnBackReinf.setMinimumSize(QSize(120, 30))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setItalic(False)
        self.btnBackReinf.setFont(font3)
        self.btnBackReinf.setStyleSheet(u"")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoPrevious))
        self.btnBackReinf.setIcon(icon1)

        self.verticalLayout_4.addWidget(self.btnBackReinf)

        self.formReinf = QWidget(self.frame3Reinf)
        self.formReinf.setObjectName(u"formReinf")
        self.verticalLayout_3 = QVBoxLayout(self.formReinf)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.vSpacer6_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.vSpacer6_3)

        self.barSizeReinf = QHBoxLayout()
        self.barSizeReinf.setObjectName(u"barSizeReinf")
        self.label3Reinf = QLabel(self.formReinf)
        self.label3Reinf.setObjectName(u"label3Reinf")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label3Reinf.sizePolicy().hasHeightForWidth())
        self.label3Reinf.setSizePolicy(sizePolicy3)
        self.label3Reinf.setMinimumSize(QSize(200, 0))
        self.label3Reinf.setMaximumSize(QSize(200, 16777215))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(12)
        font4.setBold(False)
        self.label3Reinf.setFont(font4)

        self.barSizeReinf.addWidget(self.label3Reinf)

        self.inputBarSizeReinf = QComboBox(self.formReinf)
        self.inputBarSizeReinf.setObjectName(u"inputBarSizeReinf")
        sizePolicy3.setHeightForWidth(self.inputBarSizeReinf.sizePolicy().hasHeightForWidth())
        self.inputBarSizeReinf.setSizePolicy(sizePolicy3)
        self.inputBarSizeReinf.setMinimumSize(QSize(200, 25))
        self.inputBarSizeReinf.setStyleSheet(u"border-radius: 3px;\n"
"border: 1px solid rgb(170, 0, 0);\n"
"font: 9pt \"Consolas\";\n"
"padding-left: 5px;\n"
"")
        self.inputBarSizeReinf.setEditable(True)

        self.barSizeReinf.addWidget(self.inputBarSizeReinf)

        self.hSpacer6_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.barSizeReinf.addItem(self.hSpacer6_2)

        self.barSizeReinf.setStretch(0, 2)
        self.barSizeReinf.setStretch(1, 1)
        self.barSizeReinf.setStretch(2, 1)

        self.verticalLayout_3.addLayout(self.barSizeReinf)

        self.shapeCodeReinf = QHBoxLayout()
        self.shapeCodeReinf.setObjectName(u"shapeCodeReinf")
        self.label6Reinf = QLabel(self.formReinf)
        self.label6Reinf.setObjectName(u"label6Reinf")
        sizePolicy3.setHeightForWidth(self.label6Reinf.sizePolicy().hasHeightForWidth())
        self.label6Reinf.setSizePolicy(sizePolicy3)
        self.label6Reinf.setMinimumSize(QSize(200, 0))
        self.label6Reinf.setMaximumSize(QSize(200, 16777215))
        self.label6Reinf.setFont(font4)

        self.shapeCodeReinf.addWidget(self.label6Reinf)

        self.inputShapeCode = QComboBox(self.formReinf)
        self.inputShapeCode.setObjectName(u"inputShapeCode")
        sizePolicy3.setHeightForWidth(self.inputShapeCode.sizePolicy().hasHeightForWidth())
        self.inputShapeCode.setSizePolicy(sizePolicy3)
        self.inputShapeCode.setMinimumSize(QSize(200, 25))
        self.inputShapeCode.setStyleSheet(u"border-radius: 3px;\n"
"border: 1px solid rgb(170, 0, 0);\n"
"font: 9pt \"Consolas\";\n"
"padding-left: 5px;\n"
"")
        self.inputShapeCode.setEditable(True)

        self.shapeCodeReinf.addWidget(self.inputShapeCode)

        self.hSpacer6_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.shapeCodeReinf.addItem(self.hSpacer6_4)

        self.shapeCodeReinf.setStretch(0, 2)
        self.shapeCodeReinf.setStretch(1, 1)
        self.shapeCodeReinf.setStretch(2, 1)

        self.verticalLayout_3.addLayout(self.shapeCodeReinf)

        self.barMarkReinf = QHBoxLayout()
        self.barMarkReinf.setObjectName(u"barMarkReinf")
        self.label4Reinf = QLabel(self.formReinf)
        self.label4Reinf.setObjectName(u"label4Reinf")
        sizePolicy3.setHeightForWidth(self.label4Reinf.sizePolicy().hasHeightForWidth())
        self.label4Reinf.setSizePolicy(sizePolicy3)
        self.label4Reinf.setMinimumSize(QSize(100, 0))
        self.label4Reinf.setMaximumSize(QSize(200, 16777215))
        self.label4Reinf.setFont(font4)

        self.barMarkReinf.addWidget(self.label4Reinf)

        self.inputBarMark = QLineEdit(self.formReinf)
        self.inputBarMark.setObjectName(u"inputBarMark")
        sizePolicy3.setHeightForWidth(self.inputBarMark.sizePolicy().hasHeightForWidth())
        self.inputBarMark.setSizePolicy(sizePolicy3)
        self.inputBarMark.setMinimumSize(QSize(0, 25))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(9)
        font5.setBold(False)
        font5.setItalic(False)
        self.inputBarMark.setFont(font5)
        self.inputBarMark.setStyleSheet(u"border-radius: 3px;\n"
"border: 1px solid rgb(170, 0, 0);\n"
"padding-left: 5px;\n"
"")

        self.barMarkReinf.addWidget(self.inputBarMark)

        self.hSpacer6_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.barMarkReinf.addItem(self.hSpacer6_1)

        self.barMarkReinf.setStretch(0, 2)
        self.barMarkReinf.setStretch(1, 1)
        self.barMarkReinf.setStretch(2, 1)

        self.verticalLayout_3.addLayout(self.barMarkReinf)

        self.noOfBarsReinf = QHBoxLayout()
        self.noOfBarsReinf.setObjectName(u"noOfBarsReinf")
        self.label5Reinf = QLabel(self.formReinf)
        self.label5Reinf.setObjectName(u"label5Reinf")
        sizePolicy3.setHeightForWidth(self.label5Reinf.sizePolicy().hasHeightForWidth())
        self.label5Reinf.setSizePolicy(sizePolicy3)
        self.label5Reinf.setMinimumSize(QSize(200, 0))
        self.label5Reinf.setMaximumSize(QSize(200, 16777215))
        self.label5Reinf.setFont(font4)

        self.noOfBarsReinf.addWidget(self.label5Reinf)

        self.inputNoOfBars = QLineEdit(self.formReinf)
        self.inputNoOfBars.setObjectName(u"inputNoOfBars")
        sizePolicy3.setHeightForWidth(self.inputNoOfBars.sizePolicy().hasHeightForWidth())
        self.inputNoOfBars.setSizePolicy(sizePolicy3)
        self.inputNoOfBars.setMinimumSize(QSize(0, 25))
        self.inputNoOfBars.setFont(font5)
        self.inputNoOfBars.setStyleSheet(u"border-radius: 3px;\n"
"border: 1px solid rgb(170, 0, 0);\n"
"padding-left: 5px;\n"
"")

        self.noOfBarsReinf.addWidget(self.inputNoOfBars)

        self.hSpacer6_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.noOfBarsReinf.addItem(self.hSpacer6_3)

        self.noOfBarsReinf.setStretch(0, 2)
        self.noOfBarsReinf.setStretch(1, 1)
        self.noOfBarsReinf.setStretch(2, 1)

        self.verticalLayout_3.addLayout(self.noOfBarsReinf)

        self.formDimensionsReinf = QWidget(self.formReinf)
        self.formDimensionsReinf.setObjectName(u"formDimensionsReinf")
        self.verticalLayout_5 = QVBoxLayout(self.formDimensionsReinf)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label7Reinf = QLabel(self.formDimensionsReinf)
        self.label7Reinf.setObjectName(u"label7Reinf")
        sizePolicy3.setHeightForWidth(self.label7Reinf.sizePolicy().hasHeightForWidth())
        self.label7Reinf.setSizePolicy(sizePolicy3)
        self.label7Reinf.setMaximumSize(QSize(16777215, 30))
        self.label7Reinf.setFont(font4)

        self.verticalLayout_5.addWidget(self.label7Reinf)

        self.layout2Reinf = QGridLayout()
        self.layout2Reinf.setObjectName(u"layout2Reinf")
        self.layout2Reinf.setVerticalSpacing(10)
        self.layout6Reinf = QHBoxLayout()
        self.layout6Reinf.setObjectName(u"layout6Reinf")
        self.label12Reinf = QLabel(self.formDimensionsReinf)
        self.label12Reinf.setObjectName(u"label12Reinf")
        sizePolicy2.setHeightForWidth(self.label12Reinf.sizePolicy().hasHeightForWidth())
        self.label12Reinf.setSizePolicy(sizePolicy2)
        self.label12Reinf.setMinimumSize(QSize(20, 0))
        self.label12Reinf.setMaximumSize(QSize(20, 16777215))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(12)
        font6.setBold(False)
        font6.setStrikeOut(False)
        self.label12Reinf.setFont(font6)

        self.layout6Reinf.addWidget(self.label12Reinf)

        self.aDimension = QLineEdit(self.formDimensionsReinf)
        self.aDimension.setObjectName(u"aDimension")
        self.aDimension.setMinimumSize(QSize(0, 25))
        self.aDimension.setStyleSheet(u"border-radius: 3px;\n"
"border: 1px solid rgb(170, 0, 0);\n"
"font: 9pt \"Consolas\";\n"
"padding-left: 5px;\n"
"")

        self.layout6Reinf.addWidget(self.aDimension)

        self.hSpacer6_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout6Reinf.addItem(self.hSpacer6_7)


        self.layout2Reinf.addLayout(self.layout6Reinf, 0, 0, 1, 1)

        self.layout3Reinf = QHBoxLayout()
        self.layout3Reinf.setObjectName(u"layout3Reinf")
        self.label14Reinf = QLabel(self.formDimensionsReinf)
        self.label14Reinf.setObjectName(u"label14Reinf")
        sizePolicy2.setHeightForWidth(self.label14Reinf.sizePolicy().hasHeightForWidth())
        self.label14Reinf.setSizePolicy(sizePolicy2)
        self.label14Reinf.setMinimumSize(QSize(20, 0))
        self.label14Reinf.setMaximumSize(QSize(20, 16777215))
        self.label14Reinf.setFont(font6)

        self.layout3Reinf.addWidget(self.label14Reinf)

        self.bDimension = QLineEdit(self.formDimensionsReinf)
        self.bDimension.setObjectName(u"bDimension")
        self.bDimension.setMinimumSize(QSize(0, 25))
        self.bDimension.setStyleSheet(u"border-radius: 3px;\n"
"border: 1px solid rgb(170, 0, 0);\n"
"font: 9pt \"Consolas\";\n"
"padding-left: 5px;\n"
"")

        self.layout3Reinf.addWidget(self.bDimension)

        self.hSpacer6_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout3Reinf.addItem(self.hSpacer6_11)


        self.layout2Reinf.addLayout(self.layout3Reinf, 1, 0, 1, 1)

        self.layout8Reinf = QHBoxLayout()
        self.layout8Reinf.setObjectName(u"layout8Reinf")
        self.label9Reinf = QLabel(self.formDimensionsReinf)
        self.label9Reinf.setObjectName(u"label9Reinf")
        sizePolicy2.setHeightForWidth(self.label9Reinf.sizePolicy().hasHeightForWidth())
        self.label9Reinf.setSizePolicy(sizePolicy2)
        self.label9Reinf.setMinimumSize(QSize(20, 0))
        self.label9Reinf.setMaximumSize(QSize(20, 16777215))
        self.label9Reinf.setFont(font6)

        self.layout8Reinf.addWidget(self.label9Reinf)

        self.dDimension = QLineEdit(self.formDimensionsReinf)
        self.dDimension.setObjectName(u"dDimension")
        self.dDimension.setMinimumSize(QSize(0, 25))
        self.dDimension.setStyleSheet(u"border-radius: 3px;\n"
"border: 1px solid rgb(170, 0, 0);\n"
"font: 9pt \"Consolas\";\n"
"padding-left: 5px;\n"
"")

        self.layout8Reinf.addWidget(self.dDimension)

        self.hSpacer6_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout8Reinf.addItem(self.hSpacer6_10)


        self.layout2Reinf.addLayout(self.layout8Reinf, 3, 0, 1, 1)

        self.layout10Reinf = QHBoxLayout()
        self.layout10Reinf.setObjectName(u"layout10Reinf")
        self.label11Reinf = QLabel(self.formDimensionsReinf)
        self.label11Reinf.setObjectName(u"label11Reinf")
        sizePolicy2.setHeightForWidth(self.label11Reinf.sizePolicy().hasHeightForWidth())
        self.label11Reinf.setSizePolicy(sizePolicy2)
        self.label11Reinf.setMinimumSize(QSize(20, 0))
        self.label11Reinf.setMaximumSize(QSize(20, 16777215))
        self.label11Reinf.setFont(font6)

        self.layout10Reinf.addWidget(self.label11Reinf)

        self.cDimension = QLineEdit(self.formDimensionsReinf)
        self.cDimension.setObjectName(u"cDimension")
        self.cDimension.setMinimumSize(QSize(0, 25))
        self.cDimension.setStyleSheet(u"border-radius: 3px;\n"
"border: 1px solid rgb(170, 0, 0);\n"
"font: 9pt \"Consolas\";\n"
"padding-left: 5px;\n"
"")

        self.layout10Reinf.addWidget(self.cDimension)

        self.hSpacer6_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout10Reinf.addItem(self.hSpacer6_8)


        self.layout2Reinf.addLayout(self.layout10Reinf, 2, 0, 1, 1)

        self.layout7Reinf = QHBoxLayout()
        self.layout7Reinf.setObjectName(u"layout7Reinf")
        self.label10Reinf = QLabel(self.formDimensionsReinf)
        self.label10Reinf.setObjectName(u"label10Reinf")
        sizePolicy2.setHeightForWidth(self.label10Reinf.sizePolicy().hasHeightForWidth())
        self.label10Reinf.setSizePolicy(sizePolicy2)
        self.label10Reinf.setMinimumSize(QSize(20, 0))
        self.label10Reinf.setMaximumSize(QSize(20, 16777215))
        self.label10Reinf.setFont(font6)

        self.layout7Reinf.addWidget(self.label10Reinf)

        self.eDimension = QLineEdit(self.formDimensionsReinf)
        self.eDimension.setObjectName(u"eDimension")
        self.eDimension.setMinimumSize(QSize(0, 25))
        self.eDimension.setStyleSheet(u"border-radius: 3px;\n"
"border: 1px solid rgb(170, 0, 0);\n"
"font: 9pt \"Consolas\";\n"
"padding-left: 5px;\n"
"")

        self.layout7Reinf.addWidget(self.eDimension)

        self.hSpacer6_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout7Reinf.addItem(self.hSpacer6_9)


        self.layout2Reinf.addLayout(self.layout7Reinf, 0, 1, 1, 1)

        self.layout5Reinf = QHBoxLayout()
        self.layout5Reinf.setObjectName(u"layout5Reinf")
        self.label15Reinf = QLabel(self.formDimensionsReinf)
        self.label15Reinf.setObjectName(u"label15Reinf")
        sizePolicy2.setHeightForWidth(self.label15Reinf.sizePolicy().hasHeightForWidth())
        self.label15Reinf.setSizePolicy(sizePolicy2)
        self.label15Reinf.setMinimumSize(QSize(20, 0))
        self.label15Reinf.setMaximumSize(QSize(20, 16777215))
        self.label15Reinf.setFont(font6)

        self.layout5Reinf.addWidget(self.label15Reinf)

        self.fDimension = QLineEdit(self.formDimensionsReinf)
        self.fDimension.setObjectName(u"fDimension")
        self.fDimension.setMinimumSize(QSize(0, 25))
        self.fDimension.setStyleSheet(u"border-radius: 3px;\n"
"border: 1px solid rgb(170, 0, 0);\n"
"font: 9pt \"Consolas\";\n"
"padding-left: 5px;\n"
"")

        self.layout5Reinf.addWidget(self.fDimension)

        self.hSpacer6_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout5Reinf.addItem(self.hSpacer6_12)


        self.layout2Reinf.addLayout(self.layout5Reinf, 1, 1, 1, 1)

        self.layout4Reinf = QHBoxLayout()
        self.layout4Reinf.setObjectName(u"layout4Reinf")
        self.label13Reinf = QLabel(self.formDimensionsReinf)
        self.label13Reinf.setObjectName(u"label13Reinf")
        sizePolicy2.setHeightForWidth(self.label13Reinf.sizePolicy().hasHeightForWidth())
        self.label13Reinf.setSizePolicy(sizePolicy2)
        self.label13Reinf.setMinimumSize(QSize(20, 0))
        self.label13Reinf.setMaximumSize(QSize(20, 16777215))
        self.label13Reinf.setFont(font6)

        self.layout4Reinf.addWidget(self.label13Reinf)

        self.rDimension = QLineEdit(self.formDimensionsReinf)
        self.rDimension.setObjectName(u"rDimension")
        self.rDimension.setMinimumSize(QSize(0, 25))
        self.rDimension.setStyleSheet(u"border-radius: 3px;\n"
"border: 1px solid rgb(170, 0, 0);\n"
"font: 9pt \"Consolas\";\n"
"padding-left: 5px;\n"
"")

        self.layout4Reinf.addWidget(self.rDimension)

        self.hSpacer6_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout4Reinf.addItem(self.hSpacer6_6)


        self.layout2Reinf.addLayout(self.layout4Reinf, 2, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.layout2Reinf)

        self.vSpacer6_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.vSpacer6_4)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 8)

        self.verticalLayout_3.addWidget(self.formDimensionsReinf)

        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 1)
        self.verticalLayout_3.setStretch(3, 1)
        self.verticalLayout_3.setStretch(4, 1)
        self.verticalLayout_3.setStretch(5, 10)

        self.verticalLayout_4.addWidget(self.formReinf)

        self.btnNextReinf = QPushButton(self.frame3Reinf)
        self.btnNextReinf.setObjectName(u"btnNextReinf")
        sizePolicy2.setHeightForWidth(self.btnNextReinf.sizePolicy().hasHeightForWidth())
        self.btnNextReinf.setSizePolicy(sizePolicy2)
        self.btnNextReinf.setMinimumSize(QSize(70, 30))
        self.btnNextReinf.setFont(font3)
        self.btnNextReinf.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.btnNextReinf.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.btnNextReinf)

        self.vSpacer6_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.vSpacer6_2)

        self.vSpacer6_1 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.vSpacer6_1)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(2, 15)
        self.verticalLayout_4.setStretch(3, 1)

        self.horizontalLayout.addWidget(self.frame3Reinf)

        self.frame2Reinf = QFrame(self.frame1Reinf)
        self.frame2Reinf.setObjectName(u"frame2Reinf")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(2)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame2Reinf.sizePolicy().hasHeightForWidth())
        self.frame2Reinf.setSizePolicy(sizePolicy4)
        self.frame2Reinf.setAutoFillBackground(False)
        self.frame2Reinf.setFrameShape(QFrame.Shape.Box)
        self.frame2Reinf.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_2 = QVBoxLayout(self.frame2Reinf)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label2Reinf = QLabel(self.frame2Reinf)
        self.label2Reinf.setObjectName(u"label2Reinf")
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        font7.setPointSize(12)
        font7.setBold(True)
        font7.setItalic(False)
        self.label2Reinf.setFont(font7)

        self.verticalLayout_2.addWidget(self.label2Reinf)

        self.shapeDisplayReinf = QLabel(self.frame2Reinf)
        self.shapeDisplayReinf.setObjectName(u"shapeDisplayReinf")
        font8 = QFont()
        font8.setFamilies([u"Segoe UI"])
        font8.setItalic(True)
        self.shapeDisplayReinf.setFont(font8)
        self.shapeDisplayReinf.setFrameShape(QFrame.Shape.WinPanel)
        self.shapeDisplayReinf.setFrameShadow(QFrame.Shadow.Sunken)
        self.shapeDisplayReinf.setLineWidth(5)
        self.shapeDisplayReinf.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.shapeDisplayReinf)

        self.label1Reinf = QLabel(self.frame2Reinf)
        self.label1Reinf.setObjectName(u"label1Reinf")
        self.label1Reinf.setFont(font7)

        self.verticalLayout_2.addWidget(self.label1Reinf)

        self.tableViewReinf = QTableView(self.frame2Reinf)
        self.tableViewReinf.setObjectName(u"tableViewReinf")
        self.tableViewReinf.setFrameShape(QFrame.Shape.WinPanel)

        self.verticalLayout_2.addWidget(self.tableViewReinf)

        self.verticalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.setStretch(3, 3)

        self.horizontalLayout.addWidget(self.frame2Reinf)


        self.verticalLayout.addWidget(self.frame1Reinf)

        MainWindow.setCentralWidget(self.centralwidgetReinf)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 918, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelHeaderReinf.setText(QCoreApplication.translate("MainWindow", u"i.e Ground Floor Beams", None))
        self.labelHeaderReinf2.setText(QCoreApplication.translate("MainWindow", u"i.e Ground Floor", None))
        self.labelHeaderReinf3.setText(QCoreApplication.translate("MainWindow", u"i.e Beam 01", None))
        self.btnBackReinf.setText(QCoreApplication.translate("MainWindow", u"Back to Categories", None))
        self.label3Reinf.setText(QCoreApplication.translate("MainWindow", u"Bar Size", None))
        self.label6Reinf.setText(QCoreApplication.translate("MainWindow", u"Shape Code", None))
        self.inputShapeCode.setPlaceholderText(QCoreApplication.translate("MainWindow", u"i.e 44", None))
        self.label4Reinf.setText(QCoreApplication.translate("MainWindow", u"Bar Mark", None))
        self.inputBarMark.setPlaceholderText(QCoreApplication.translate("MainWindow", u"i.e 01", None))
        self.label5Reinf.setText(QCoreApplication.translate("MainWindow", u"Number of Bars", None))
        self.inputNoOfBars.setPlaceholderText(QCoreApplication.translate("MainWindow", u"i.e 4", None))
        self.label7Reinf.setText(QCoreApplication.translate("MainWindow", u"Dimensions", None))
        self.label12Reinf.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.label14Reinf.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.label9Reinf.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.label11Reinf.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.label10Reinf.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.label15Reinf.setText(QCoreApplication.translate("MainWindow", u"F", None))
        self.label13Reinf.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.btnNextReinf.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label2Reinf.setText(QCoreApplication.translate("MainWindow", u"Shape", None))
        self.shapeDisplayReinf.setText(QCoreApplication.translate("MainWindow", u"Shape will be displayed here", None))
        self.label1Reinf.setText(QCoreApplication.translate("MainWindow", u"Bars", None))
    # retranslateUi

