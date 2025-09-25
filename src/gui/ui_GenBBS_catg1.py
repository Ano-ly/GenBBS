# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GenBBS_catg1.ui'
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
    QStatusBar, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)
import app_resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(718, 571)
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
        self.frame1Catg1.setMinimumSize(QSize(700, 500))
        self.frame1Catg1.setMaximumSize(QSize(16777215, 900))
        self.frame1Catg1.setAutoFillBackground(False)
        self.frame1Catg1.setStyleSheet(u"background-color: white;")
        self.frame1Catg1.setFrameShape(QFrame.Shape.WinPanel)
        self.frame1Catg1.setFrameShadow(QFrame.Shadow.Sunken)
        self.horizontalLayout = QHBoxLayout(self.frame1Catg1)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frameLeftCatg2 = QFrame(self.frame1Catg1)
        self.frameLeftCatg2.setObjectName(u"frameLeftCatg2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(3)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frameLeftCatg2.sizePolicy().hasHeightForWidth())
        self.frameLeftCatg2.setSizePolicy(sizePolicy1)
        self.frameLeftCatg2.setAutoFillBackground(False)
        self.frameLeftCatg2.setStyleSheet(u"#btnCreateSubCatg2 {\n"
"background-color: rgb(85, 170, 0);\n"
"border-radius: 5px;\n"
"color: white;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"#btnCreateSubCatg2:hover {\n"
"background-color:rgb(139, 243, 59)\n"
"}\n"
"#btnCreateElementCatg2 {\n"
"background-color: rgb(85, 170, 0);\n"
"border-radius: 5px;\n"
"color: white;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"#btnCreateElementCatg2:hover {\n"
"background-color:rgb(139, 243, 59)\n"
"}\n"
"#btnSaveCatg1 {\n"
"border-radius: 5px;\n"
"color: black;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"#btnSaveCatg1:hover {\n"
"background-color:rgb(170, 170, 170)\n"
"}\n"
"#btnBackCatg1 {\n"
"\n"
"border-radius: 5px;\n"
"color: black;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"#btnBackCatg1:hover {\n"
"background-color:rgb(170, 170, 170)\n"
"}")
        self.frameLeftCatg2.setFrameShape(QFrame.Shape.Box)
        self.frameLeftCatg2.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_3 = QVBoxLayout(self.frameLeftCatg2)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnBackCatg1 = QPushButton(self.frameLeftCatg2)
        self.btnBackCatg1.setObjectName(u"btnBackCatg1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btnBackCatg1.sizePolicy().hasHeightForWidth())
        self.btnBackCatg1.setSizePolicy(sizePolicy2)
        self.btnBackCatg1.setMinimumSize(QSize(60, 0))
        self.btnBackCatg1.setMaximumSize(QSize(60, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(9)
        self.btnBackCatg1.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u":/images/Back_Button.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnBackCatg1.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.btnBackCatg1)

        self.btnSaveCatg1 = QPushButton(self.frameLeftCatg2)
        self.btnSaveCatg1.setObjectName(u"btnSaveCatg1")
        self.btnSaveCatg1.setAutoFillBackground(False)
        icon2 = QIcon()
        icon2.addFile(u":/images/Save button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnSaveCatg1.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.btnSaveCatg1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.label1Catg1 = QLabel(self.frameLeftCatg2)
        self.label1Catg1.setObjectName(u"label1Catg1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label1Catg1.sizePolicy().hasHeightForWidth())
        self.label1Catg1.setSizePolicy(sizePolicy3)
        self.label1Catg1.setMinimumSize(QSize(0, 30))
        self.label1Catg1.setMaximumSize(QSize(16777215, 30))
        self.label1Catg1.setBaseSize(QSize(0, 30))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setStrikeOut(False)
        self.label1Catg1.setFont(font2)
        self.label1Catg1.setAutoFillBackground(False)
        self.label1Catg1.setStyleSheet(u"\n"
"	\n"
"	background-image: url(:/images/Reinf_Backdrop.jpeg);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    background-attachment: fixed;\n"
"color: white;\n"
"")
        self.label1Catg1.setMargin(5)

        self.verticalLayout_3.addWidget(self.label1Catg1)

        self.label2Catg2 = QLabel(self.frameLeftCatg2)
        self.label2Catg2.setObjectName(u"label2Catg2")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setStrikeOut(False)
        self.label2Catg2.setFont(font3)

        self.verticalLayout_3.addWidget(self.label2Catg2)

        self.layout1Catg2 = QHBoxLayout()
        self.layout1Catg2.setSpacing(5)
        self.layout1Catg2.setObjectName(u"layout1Catg2")
        self.layout1Catg2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.layout1Catg2.setContentsMargins(10, 0, 20, 10)
        self.inputNewElementCatg = QLineEdit(self.frameLeftCatg2)
        self.inputNewElementCatg.setObjectName(u"inputNewElementCatg")
        sizePolicy3.setHeightForWidth(self.inputNewElementCatg.sizePolicy().hasHeightForWidth())
        self.inputNewElementCatg.setSizePolicy(sizePolicy3)
        self.inputNewElementCatg.setMinimumSize(QSize(0, 30))
        self.inputNewElementCatg.setMaximumSize(QSize(600, 16777215))
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
        self.inputNewElementCatg.setPalette(palette)
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        self.inputNewElementCatg.setFont(font4)
        self.inputNewElementCatg.setStyleSheet(u"border-radius: 3px;\n"
"border: 1px solid rgb(170, 0, 0);\n"
"padding-left: 5px;\n"
"")
        self.inputNewElementCatg.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.inputNewElementCatg.setClearButtonEnabled(True)

        self.layout1Catg2.addWidget(self.inputNewElementCatg)

        self.btnCreateElementCatg2 = QPushButton(self.frameLeftCatg2)
        self.btnCreateElementCatg2.setObjectName(u"btnCreateElementCatg2")
        sizePolicy2.setHeightForWidth(self.btnCreateElementCatg2.sizePolicy().hasHeightForWidth())
        self.btnCreateElementCatg2.setSizePolicy(sizePolicy2)
        self.btnCreateElementCatg2.setMinimumSize(QSize(60, 30))
        self.btnCreateElementCatg2.setMaximumSize(QSize(50, 16777215))
        palette1 = QPalette()
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        brush1 = QBrush(QColor(85, 170, 0, 255))
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
        self.btnCreateElementCatg2.setPalette(palette1)
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(12)
        font5.setBold(False)
        font5.setItalic(False)
        self.btnCreateElementCatg2.setFont(font5)
        self.btnCreateElementCatg2.setAutoFillBackground(False)
        self.btnCreateElementCatg2.setStyleSheet(u"")
        self.btnCreateElementCatg2.setCheckable(True)

        self.layout1Catg2.addWidget(self.btnCreateElementCatg2)

        self.hSpacer2_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.layout1Catg2.addItem(self.hSpacer2_1)

        self.layout1Catg2.setStretch(0, 6)
        self.layout1Catg2.setStretch(1, 2)
        self.layout1Catg2.setStretch(2, 1)

        self.verticalLayout_3.addLayout(self.layout1Catg2)

        self.label_2 = QLabel(self.frameLeftCatg2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)

        self.verticalLayout_3.addWidget(self.label_2)

        self.layout2Catg2 = QHBoxLayout()
        self.layout2Catg2.setSpacing(5)
        self.layout2Catg2.setObjectName(u"layout2Catg2")
        self.layout2Catg2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.layout2Catg2.setContentsMargins(10, 0, 20, 10)
        self.inputNewSubCatg1 = QLineEdit(self.frameLeftCatg2)
        self.inputNewSubCatg1.setObjectName(u"inputNewSubCatg1")
        sizePolicy3.setHeightForWidth(self.inputNewSubCatg1.sizePolicy().hasHeightForWidth())
        self.inputNewSubCatg1.setSizePolicy(sizePolicy3)
        self.inputNewSubCatg1.setMinimumSize(QSize(0, 30))
        self.inputNewSubCatg1.setMaximumSize(QSize(600, 16777215))
        palette2 = QPalette()
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush)
        self.inputNewSubCatg1.setPalette(palette2)
        self.inputNewSubCatg1.setFont(font4)
        self.inputNewSubCatg1.setStyleSheet(u"border-radius: 3px;\n"
"border: 1px solid rgb(170, 0, 0);\n"
"padding-left: 5px;\n"
"")
        self.inputNewSubCatg1.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.inputNewSubCatg1.setClearButtonEnabled(True)

        self.layout2Catg2.addWidget(self.inputNewSubCatg1)

        self.btnCreateSubCatg2 = QPushButton(self.frameLeftCatg2)
        self.btnCreateSubCatg2.setObjectName(u"btnCreateSubCatg2")
        sizePolicy2.setHeightForWidth(self.btnCreateSubCatg2.sizePolicy().hasHeightForWidth())
        self.btnCreateSubCatg2.setSizePolicy(sizePolicy2)
        self.btnCreateSubCatg2.setMinimumSize(QSize(60, 30))
        self.btnCreateSubCatg2.setMaximumSize(QSize(50, 16777215))
        palette3 = QPalette()
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Highlight, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush3)
#endif
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Highlight, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush3)
#endif
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Highlight, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush3)
#endif
        self.btnCreateSubCatg2.setPalette(palette3)
        self.btnCreateSubCatg2.setFont(font5)
        self.btnCreateSubCatg2.setAutoFillBackground(False)
        self.btnCreateSubCatg2.setStyleSheet(u"")
        self.btnCreateSubCatg2.setCheckable(True)

        self.layout2Catg2.addWidget(self.btnCreateSubCatg2)

        self.hSpacer2_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.layout2Catg2.addItem(self.hSpacer2_2)

        self.layout2Catg2.setStretch(0, 6)
        self.layout2Catg2.setStretch(1, 2)
        self.layout2Catg2.setStretch(2, 1)

        self.verticalLayout_3.addLayout(self.layout2Catg2)

        self.vSpacer2_1 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.vSpacer2_1)

        self.vSpacer2_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.vSpacer2_2)

        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 1)
        self.verticalLayout_3.setStretch(3, 1)
        self.verticalLayout_3.setStretch(4, 1)
        self.verticalLayout_3.setStretch(5, 1)
        self.verticalLayout_3.setStretch(6, 1)
        self.verticalLayout_3.setStretch(7, 1)

        self.horizontalLayout.addWidget(self.frameLeftCatg2)

        self.frameRightCatg1 = QFrame(self.frame1Catg1)
        self.frameRightCatg1.setObjectName(u"frameRightCatg1")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(2)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frameRightCatg1.sizePolicy().hasHeightForWidth())
        self.frameRightCatg1.setSizePolicy(sizePolicy4)
        self.frameRightCatg1.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frameRightCatg1.setAutoFillBackground(False)
        self.frameRightCatg1.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(170, 0, 0);\n"
"	border-radius: 3px;\n"
"	color: white;\n"
"	margin-right: 5pt;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(181, 78, 78);\n"
"}\n"
"\n"
"")
        self.frameRightCatg1.setFrameShape(QFrame.Shape.Box)
        self.frameRightCatg1.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_2 = QVBoxLayout(self.frameRightCatg1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label2Catg1 = QLabel(self.frameRightCatg1)
        self.label2Catg1.setObjectName(u"label2Catg1")
        self.label2Catg1.setFont(font3)

        self.verticalLayout_2.addWidget(self.label2Catg1)

        self.lineCatg1 = QFrame(self.frameRightCatg1)
        self.lineCatg1.setObjectName(u"lineCatg1")
        self.lineCatg1.setFrameShape(QFrame.Shape.HLine)
        self.lineCatg1.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.lineCatg1)

        self.frame2Catg1 = QFrame(self.frameRightCatg1)
        self.frame2Catg1.setObjectName(u"frame2Catg1")
        self.frame2Catg1.setAutoFillBackground(False)
        self.frame2Catg1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame2Catg1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame2Catg1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.treeWidgetCatg1 = QTreeWidget(self.frame2Catg1)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(1, u"2");
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidgetCatg1.setHeaderItem(__qtreewidgetitem)
        self.treeWidgetCatg1.setObjectName(u"treeWidgetCatg1")
        self.treeWidgetCatg1.setTabKeyNavigation(True)
        self.treeWidgetCatg1.setColumnCount(2)

        self.horizontalLayout_3.addWidget(self.treeWidgetCatg1)


        self.verticalLayout_2.addWidget(self.frame2Catg1)

        self.btnExportCatg1 = QPushButton(self.frameRightCatg1)
        self.btnExportCatg1.setObjectName(u"btnExportCatg1")
        sizePolicy2.setHeightForWidth(self.btnExportCatg1.sizePolicy().hasHeightForWidth())
        self.btnExportCatg1.setSizePolicy(sizePolicy2)
        self.btnExportCatg1.setMinimumSize(QSize(70, 30))
        self.btnExportCatg1.setMaximumSize(QSize(60, 25))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(12)
        font6.setStrikeOut(False)
        self.btnExportCatg1.setFont(font6)
        self.btnExportCatg1.setStyleSheet(u"")
        self.btnExportCatg1.setCheckable(True)

        self.verticalLayout_2.addWidget(self.btnExportCatg1)

        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(2, 25)

        self.horizontalLayout.addWidget(self.frameRightCatg1)


        self.verticalLayout.addWidget(self.frame1Catg1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 718, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnBackCatg1.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.btnSaveCatg1.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label1Catg1.setText(QCoreApplication.translate("MainWindow", u"Category Placeholder, i.e [GROUND FLOOR]", None))
        self.label2Catg2.setText(QCoreApplication.translate("MainWindow", u"Add Structural Element", None))
        self.inputNewElementCatg.setText("")
        self.inputNewElementCatg.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter name of structural element", None))
        self.btnCreateElementCatg2.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Add Sub-Category", None))
        self.inputNewSubCatg1.setText("")
        self.inputNewSubCatg1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter name of new category", None))
        self.btnCreateSubCatg2.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.label2Catg1.setText(QCoreApplication.translate("MainWindow", u"Categories", None))
        self.btnExportCatg1.setText(QCoreApplication.translate("MainWindow", u"Export", None))
    # retranslateUi

