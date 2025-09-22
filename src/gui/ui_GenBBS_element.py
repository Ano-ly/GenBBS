# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GenBBS_element.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTreeView, QVBoxLayout, QWidget)
import app_resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(918, 677)
        font = QFont()
        font.setStrikeOut(False)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/images/GenBBS Logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame1Catg1 = QFrame(self.centralwidget)
        self.frame1Catg1.setObjectName(u"frame1Catg1")
        sizePolicy.setHeightForWidth(self.frame1Catg1.sizePolicy().hasHeightForWidth())
        self.frame1Catg1.setSizePolicy(sizePolicy)
        self.frame1Catg1.setMinimumSize(QSize(900, 500))
        self.frame1Catg1.setMaximumSize(QSize(16777215, 900))
        self.frame1Catg1.setAutoFillBackground(False)
        self.frame1Catg1.setStyleSheet(u"background-color: white;")
        self.frame1Catg1.setFrameShape(QFrame.Shape.WinPanel)
        self.frame1Catg1.setFrameShadow(QFrame.Shadow.Sunken)
        self.horizontalLayout = QHBoxLayout(self.frame1Catg1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frameLeftElement = QFrame(self.frame1Catg1)
        self.frameLeftElement.setObjectName(u"frameLeftElement")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(3)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frameLeftElement.sizePolicy().hasHeightForWidth())
        self.frameLeftElement.setSizePolicy(sizePolicy1)
        self.frameLeftElement.setAutoFillBackground(False)
        self.frameLeftElement.setStyleSheet(u"#editElement {\n"
"	background-color: rgb(170, 0, 0);\n"
"	border-radius: 3px;\n"
"	color: white;\n"
"}\n"
"#editElement:hover {\n"
"	background-color: rgb(181, 78, 78)\n"
"}\n"
"\n"
"#createCatg {\n"
"	background-color: rgb(241, 241, 241);\n"
"	border: 1px solid green;\n"
"	font: 9pt \"Consolas\";\n"
"	border-radius: 5px;\n"
"	color: white;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}\n"
"#createCatg:hover {\n"
"	border: 2px solid rgb(170, 0, 0);\n"
"}")
        self.frameLeftElement.setFrameShape(QFrame.Shape.Box)
        self.frameLeftElement.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_3 = QVBoxLayout(self.frameLeftElement)
        self.verticalLayout_3.setSpacing(30)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.label1Element = QLabel(self.frameLeftElement)
        self.label1Element.setObjectName(u"label1Element")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label1Element.sizePolicy().hasHeightForWidth())
        self.label1Element.setSizePolicy(sizePolicy2)
        self.label1Element.setMinimumSize(QSize(0, 30))
        self.label1Element.setMaximumSize(QSize(16777215, 30))
        self.label1Element.setBaseSize(QSize(0, 30))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setStrikeOut(False)
        self.label1Element.setFont(font1)
        self.label1Element.setAutoFillBackground(False)
        self.label1Element.setStyleSheet(u"\n"
"	\n"
"	background-image: url(:/images/Reinf_Backdrop.jpeg);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    background-attachment: fixed;\n"
"color: white;\n"
"")

        self.verticalLayout_3.addWidget(self.label1Element)

        self.label2Element = QLabel(self.frameLeftElement)
        self.label2Element.setObjectName(u"label2Element")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.label2Element.setFont(font2)

        self.verticalLayout_3.addWidget(self.label2Element)

        self.layoutElement1 = QHBoxLayout()
        self.layoutElement1.setSpacing(5)
        self.layoutElement1.setObjectName(u"layoutElement1")
        self.layoutElement1.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.layoutElement1.setContentsMargins(10, 0, 20, 300)
        self.inputNumElement = QLineEdit(self.frameLeftElement)
        self.inputNumElement.setObjectName(u"inputNumElement")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.inputNumElement.sizePolicy().hasHeightForWidth())
        self.inputNumElement.setSizePolicy(sizePolicy3)
        self.inputNumElement.setMinimumSize(QSize(400, 30))
        self.inputNumElement.setMaximumSize(QSize(600, 16777215))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush)
        self.inputNumElement.setPalette(palette)
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setItalic(False)
        self.inputNumElement.setFont(font3)
        self.inputNumElement.setStyleSheet(u"border-radius: 3px;\n"
"border: 1px solid rgb(170, 0, 0);\n"
"padding-left: 5px;\n"
"")
        self.inputNumElement.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.inputNumElement.setClearButtonEnabled(True)

        self.layoutElement1.addWidget(self.inputNumElement)

        self.btnDoneElement = QPushButton(self.frameLeftElement)
        self.btnDoneElement.setObjectName(u"btnDoneElement")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btnDoneElement.sizePolicy().hasHeightForWidth())
        self.btnDoneElement.setSizePolicy(sizePolicy4)
        self.btnDoneElement.setMinimumSize(QSize(30, 30))
        self.btnDoneElement.setMaximumSize(QSize(30, 30))
        palette1 = QPalette()
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        brush1 = QBrush(QColor(241, 241, 241, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        brush2 = QBrush(QColor(39, 191, 115, 255))
        brush2.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Highlight, brush2)
        brush3 = QBrush(QColor(255, 255, 255, 128))
        brush3.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush3)
#endif
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Highlight, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush3)
#endif
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Highlight, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush3)
#endif
        self.btnDoneElement.setPalette(palette1)
        self.btnDoneElement.setAutoFillBackground(False)
        self.btnDoneElement.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/images/done.jpeg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnDoneElement.setIcon(icon1)
        self.btnDoneElement.setIconSize(QSize(25, 25))
        self.btnDoneElement.setCheckable(True)

        self.layoutElement1.addWidget(self.btnDoneElement)

        self.hSpacer3_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layoutElement1.addItem(self.hSpacer3_1)


        self.verticalLayout_3.addLayout(self.layoutElement1)

        self.btnEditElement = QPushButton(self.frameLeftElement)
        self.btnEditElement.setObjectName(u"btnEditElement")
        self.btnEditElement.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.btnEditElement.sizePolicy().hasHeightForWidth())
        self.btnEditElement.setSizePolicy(sizePolicy4)
        self.btnEditElement.setMinimumSize(QSize(50, 30))
        self.btnEditElement.setMaximumSize(QSize(70, 30))
        self.btnEditElement.setFont(font2)
        self.btnEditElement.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.btnEditElement.setAutoFillBackground(False)
        self.btnEditElement.setStyleSheet(u"")

        self.verticalLayout_3.addWidget(self.btnEditElement)

        self.vSpacer3_1 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.vSpacer3_1)


        self.horizontalLayout.addWidget(self.frameLeftElement)

        self.label2Catg1_2 = QFrame(self.frame1Catg1)
        self.label2Catg1_2.setObjectName(u"label2Catg1_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(2)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label2Catg1_2.sizePolicy().hasHeightForWidth())
        self.label2Catg1_2.setSizePolicy(sizePolicy5)
        self.label2Catg1_2.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label2Catg1_2.setAutoFillBackground(False)
        self.label2Catg1_2.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(170, 0, 0);\n"
"	border-radius: 3px;\n"
"	color: white;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(181, 78, 78)\n"
"}\n"
"\n"
"")
        self.label2Catg1_2.setFrameShape(QFrame.Shape.Box)
        self.label2Catg1_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_2 = QVBoxLayout(self.label2Catg1_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label2Catg1 = QLabel(self.label2Catg1_2)
        self.label2Catg1.setObjectName(u"label2Catg1")
        self.label2Catg1.setFont(font1)

        self.verticalLayout_2.addWidget(self.label2Catg1)

        self.lineCatg1 = QFrame(self.label2Catg1_2)
        self.lineCatg1.setObjectName(u"lineCatg1")
        self.lineCatg1.setFrameShape(QFrame.Shape.HLine)
        self.lineCatg1.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.lineCatg1)

        self.frame2Catg1 = QFrame(self.label2Catg1_2)
        self.frame2Catg1.setObjectName(u"frame2Catg1")
        self.frame2Catg1.setAutoFillBackground(False)
        self.frame2Catg1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame2Catg1.setFrameShadow(QFrame.Shadow.Raised)
        self.treeViewCatg = QTreeView(self.frame2Catg1)
        self.treeViewCatg.setObjectName(u"treeViewCatg")
        self.treeViewCatg.setGeometry(QRect(10, 10, 311, 361))

        self.verticalLayout_2.addWidget(self.frame2Catg1)

        self.btnExportCatg1 = QPushButton(self.label2Catg1_2)
        self.btnExportCatg1.setObjectName(u"btnExportCatg1")
        sizePolicy4.setHeightForWidth(self.btnExportCatg1.sizePolicy().hasHeightForWidth())
        self.btnExportCatg1.setSizePolicy(sizePolicy4)
        self.btnExportCatg1.setMinimumSize(QSize(60, 25))
        self.btnExportCatg1.setMaximumSize(QSize(70, 30))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(12)
        font4.setBold(False)
        self.btnExportCatg1.setFont(font4)
        self.btnExportCatg1.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.btnExportCatg1.setStyleSheet(u"")
        self.btnExportCatg1.setCheckable(True)

        self.verticalLayout_2.addWidget(self.btnExportCatg1)

        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(2, 25)

        self.horizontalLayout.addWidget(self.label2Catg1_2)


        self.verticalLayout.addWidget(self.frame1Catg1)

        MainWindow.setCentralWidget(self.centralwidget)
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
        self.label1Element.setText(QCoreApplication.translate("MainWindow", u"Placeholder for element name, i.e [BEAM 01]", None))
        self.label2Element.setText(QCoreApplication.translate("MainWindow", u"Number", None))
        self.inputNumElement.setText("")
        self.inputNumElement.setPlaceholderText(QCoreApplication.translate("MainWindow", u"..how many?", None))
        self.btnDoneElement.setText("")
        self.btnEditElement.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.label2Catg1.setText(QCoreApplication.translate("MainWindow", u"Categories", None))
        self.btnExportCatg1.setText(QCoreApplication.translate("MainWindow", u"Export", None))
    # retranslateUi

