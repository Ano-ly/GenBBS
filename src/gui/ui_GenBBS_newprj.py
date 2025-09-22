# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GenBBS_newprj.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)
import app_resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1111, 561)
        font = QFont()
        font.setStrikeOut(False)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/images/GenBBS Logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        self.centralwidgetNewprj = QWidget(MainWindow)
        self.centralwidgetNewprj.setObjectName(u"centralwidgetNewprj")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidgetNewprj.sizePolicy().hasHeightForWidth())
        self.centralwidgetNewprj.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.centralwidgetNewprj)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame1Newprj = QFrame(self.centralwidgetNewprj)
        self.frame1Newprj.setObjectName(u"frame1Newprj")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame1Newprj.sizePolicy().hasHeightForWidth())
        self.frame1Newprj.setSizePolicy(sizePolicy1)
        self.frame1Newprj.setMinimumSize(QSize(700, 500))
        self.frame1Newprj.setMaximumSize(QSize(16777215, 900))
        self.frame1Newprj.setAutoFillBackground(False)
        self.frame1Newprj.setStyleSheet(u"#frame1Newprj {\n"
"background-color: white;\n"
"}\n"
"#btnCreateNewprj {\n"
"background-color: rgb(85, 170, 0);\n"
"border-radius: 5px;\n"
"color: white;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"btnCreateNewprj:hover {\n"
"background-color:rgb(139, 243, 59)\n"
"}\n"
"#btnBackNewprj{\n"
"\n"
"border-radius: 5px;\n"
"color: black;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"btnBackNewprj:hover {\n"
"background-color:rgb(182, 72, 72)\n"
"}")
        self.frame1Newprj.setFrameShape(QFrame.Shape.WinPanel)
        self.frame1Newprj.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_3 = QVBoxLayout(self.frame1Newprj)
        self.verticalLayout_3.setSpacing(30)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, 0, 0)
        self.layout1Newprj = QHBoxLayout()
        self.layout1Newprj.setObjectName(u"layout1Newprj")
        self.btnBackNewprj = QPushButton(self.frame1Newprj)
        self.btnBackNewprj.setObjectName(u"btnBackNewprj")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(9)
        self.btnBackNewprj.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u":/images/Back_Button.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnBackNewprj.setIcon(icon1)

        self.layout1Newprj.addWidget(self.btnBackNewprj)

        self.hSpacer5_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout1Newprj.addItem(self.hSpacer5_2)

        self.frame3Newprj = QFrame(self.frame1Newprj)
        self.frame3Newprj.setObjectName(u"frame3Newprj")
        self.frame3Newprj.setStyleSheet(u"")
        self.frame3Newprj.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame3Newprj.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame3Newprj)
        self.verticalLayout_2.setSpacing(30)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 20, -1, -1)
        self.label1Newprj = QLabel(self.frame3Newprj)
        self.label1Newprj.setObjectName(u"label1Newprj")
        font2 = QFont()
        font2.setFamilies([u"Arial Nova"])
        font2.setPointSize(15)
        font2.setBold(True)
        self.label1Newprj.setFont(font2)
        self.label1Newprj.setStyleSheet(u"color: rgb(170, 0, 0);")

        self.verticalLayout_2.addWidget(self.label1Newprj)

        self.layout2Newprj = QHBoxLayout()
        self.layout2Newprj.setObjectName(u"layout2Newprj")
        self.label2Newprj = QLabel(self.frame3Newprj)
        self.label2Newprj.setObjectName(u"label2Newprj")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label2Newprj.sizePolicy().hasHeightForWidth())
        self.label2Newprj.setSizePolicy(sizePolicy2)
        self.label2Newprj.setMinimumSize(QSize(130, 0))
        self.label2Newprj.setMaximumSize(QSize(200, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Arial Nova"])
        font3.setPointSize(12)
        font3.setBold(True)
        self.label2Newprj.setFont(font3)

        self.layout2Newprj.addWidget(self.label2Newprj)

        self.inputNameNewprj = QLineEdit(self.frame3Newprj)
        self.inputNameNewprj.setObjectName(u"inputNameNewprj")
        sizePolicy2.setHeightForWidth(self.inputNameNewprj.sizePolicy().hasHeightForWidth())
        self.inputNameNewprj.setSizePolicy(sizePolicy2)
        self.inputNameNewprj.setMinimumSize(QSize(300, 30))
        self.inputNameNewprj.setStyleSheet(u"border-radius: 3px;\n"
"border: 1px solid rgb(170, 0, 0);\n"
"padding-left: 5px;\n"
"")

        self.layout2Newprj.addWidget(self.inputNameNewprj)

        self.btnCreateNewprj = QPushButton(self.frame3Newprj)
        self.btnCreateNewprj.setObjectName(u"btnCreateNewprj")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btnCreateNewprj.sizePolicy().hasHeightForWidth())
        self.btnCreateNewprj.setSizePolicy(sizePolicy3)
        self.btnCreateNewprj.setMinimumSize(QSize(60, 30))
        self.btnCreateNewprj.setMaximumSize(QSize(50, 16777215))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        brush1 = QBrush(QColor(85, 170, 0, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        brush2 = QBrush(QColor(39, 191, 115, 255))
        brush2.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Highlight, brush2)
        brush3 = QBrush(QColor(255, 255, 255, 128))
        brush3.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Highlight, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Highlight, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush3)
#endif
        self.btnCreateNewprj.setPalette(palette)
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setItalic(False)
        self.btnCreateNewprj.setFont(font4)
        self.btnCreateNewprj.setAutoFillBackground(False)
        self.btnCreateNewprj.setStyleSheet(u"")
        self.btnCreateNewprj.setCheckable(True)

        self.layout2Newprj.addWidget(self.btnCreateNewprj)

        self.hSpacer5_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout2Newprj.addItem(self.hSpacer5_1)

        self.layout2Newprj.setStretch(3, 1)

        self.verticalLayout_2.addLayout(self.layout2Newprj)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 5)

        self.layout1Newprj.addWidget(self.frame3Newprj)

        self.hSpacer5_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout1Newprj.addItem(self.hSpacer5_3)


        self.verticalLayout_3.addLayout(self.layout1Newprj)

        self.frame2Newprj = QFrame(self.frame1Newprj)
        self.frame2Newprj.setObjectName(u"frame2Newprj")
        self.frame2Newprj.setStyleSheet(u"#frame2Newprj {\n"
"	\n"
"	background-image: url(:/images/Reinf_Backdrop.jpeg);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    background-attachment: fixed;\n"
"}")
        self.frame2Newprj.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame2Newprj.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame2Newprj)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.genBBSLogo = QLabel(self.frame2Newprj)
        self.genBBSLogo.setObjectName(u"genBBSLogo")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.genBBSLogo.sizePolicy().hasHeightForWidth())
        self.genBBSLogo.setSizePolicy(sizePolicy4)
        self.genBBSLogo.setMaximumSize(QSize(100, 100))
        self.genBBSLogo.setPixmap(QPixmap(u":/images/GenBBS Logo.png"))
        self.genBBSLogo.setScaledContents(True)

        self.horizontalLayout.addWidget(self.genBBSLogo)


        self.verticalLayout_3.addWidget(self.frame2Newprj)

        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(1, 3)

        self.verticalLayout.addWidget(self.frame1Newprj)

        MainWindow.setCentralWidget(self.centralwidgetNewprj)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1111, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnBackNewprj.setText(QCoreApplication.translate("MainWindow", u"Back to Main Window", None))
        self.label1Newprj.setText(QCoreApplication.translate("MainWindow", u"Create New Project", None))
        self.label2Newprj.setText(QCoreApplication.translate("MainWindow", u"Name of Project", None))
        self.btnCreateNewprj.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.genBBSLogo.setText("")
    # retranslateUi

