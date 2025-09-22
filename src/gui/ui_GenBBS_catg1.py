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
    QStatusBar, QTreeView, QVBoxLayout, QWidget)
import app_resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(718, 597)
        font = QFont()
        font.setStrikeOut(False)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/images/GenBBS Logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        self.centralwidgetCatg1 = QWidget(MainWindow)
        self.centralwidgetCatg1.setObjectName(u"centralwidgetCatg1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidgetCatg1.sizePolicy().hasHeightForWidth())
        self.centralwidgetCatg1.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.centralwidgetCatg1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame1Catg1 = QFrame(self.centralwidgetCatg1)
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
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frameLeftCatg1 = QFrame(self.frame1Catg1)
        self.frameLeftCatg1.setObjectName(u"frameLeftCatg1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(3)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frameLeftCatg1.sizePolicy().hasHeightForWidth())
        self.frameLeftCatg1.setSizePolicy(sizePolicy1)
        self.frameLeftCatg1.setAutoFillBackground(False)
        self.frameLeftCatg1.setStyleSheet(u"QPushButton {\n"
"background-color: rgb(85, 170, 0);\n"
"border-radius: 5px;\n"
"color: white;\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(139, 243, 59)\n"
"}")
        self.frameLeftCatg1.setFrameShape(QFrame.Shape.Box)
        self.frameLeftCatg1.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_3 = QVBoxLayout(self.frameLeftCatg1)
        self.verticalLayout_3.setSpacing(30)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.label1Catg1 = QLabel(self.frameLeftCatg1)
        self.label1Catg1.setObjectName(u"label1Catg1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label1Catg1.sizePolicy().hasHeightForWidth())
        self.label1Catg1.setSizePolicy(sizePolicy2)
        self.label1Catg1.setMinimumSize(QSize(0, 30))
        self.label1Catg1.setMaximumSize(QSize(16777215, 30))
        self.label1Catg1.setBaseSize(QSize(0, 30))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setStrikeOut(False)
        self.label1Catg1.setFont(font1)
        self.label1Catg1.setAutoFillBackground(False)
        self.label1Catg1.setStyleSheet(u"\n"
"	\n"
"	background-image: url(:/images/Reinf_Backdrop.jpeg);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    background-attachment: fixed;\n"
"color: white;\n"
"")

        self.verticalLayout_3.addWidget(self.label1Catg1)

        self.layout1Catg = QHBoxLayout()
        self.layout1Catg.setSpacing(5)
        self.layout1Catg.setObjectName(u"layout1Catg")
        self.layout1Catg.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.layout1Catg.setContentsMargins(10, 0, 20, 300)
        self.newInputCatg1 = QLineEdit(self.frameLeftCatg1)
        self.newInputCatg1.setObjectName(u"newInputCatg1")
        sizePolicy2.setHeightForWidth(self.newInputCatg1.sizePolicy().hasHeightForWidth())
        self.newInputCatg1.setSizePolicy(sizePolicy2)
        self.newInputCatg1.setMinimumSize(QSize(0, 30))
        self.newInputCatg1.setMaximumSize(QSize(600, 16777215))
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
        self.newInputCatg1.setPalette(palette)
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(False)
        self.newInputCatg1.setFont(font2)
        self.newInputCatg1.setStyleSheet(u"border-radius: 3px;\n"
"border: 1px solid rgb(170, 0, 0);\n"
"padding-left: 5px;\n"
"")
        self.newInputCatg1.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.newInputCatg1.setClearButtonEnabled(True)

        self.layout1Catg.addWidget(self.newInputCatg1)

        self.btnCreateCatg1 = QPushButton(self.frameLeftCatg1)
        self.btnCreateCatg1.setObjectName(u"btnCreateCatg1")
        self.btnCreateCatg1.setMinimumSize(QSize(0, 30))
        self.btnCreateCatg1.setMaximumSize(QSize(70, 16777215))
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
        self.btnCreateCatg1.setPalette(palette1)
        self.btnCreateCatg1.setFont(font2)
        self.btnCreateCatg1.setAutoFillBackground(False)
        self.btnCreateCatg1.setStyleSheet(u"")
        self.btnCreateCatg1.setCheckable(True)

        self.layout1Catg.addWidget(self.btnCreateCatg1)

        self.hSpacer1_1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.layout1Catg.addItem(self.hSpacer1_1)

        self.layout1Catg.setStretch(0, 6)
        self.layout1Catg.setStretch(1, 2)
        self.layout1Catg.setStretch(2, 1)

        self.verticalLayout_3.addLayout(self.layout1Catg)

        self.vSpacer1_1 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.vSpacer1_1)


        self.horizontalLayout.addWidget(self.frameLeftCatg1)

        self.frameRightCatg1 = QFrame(self.frame1Catg1)
        self.frameRightCatg1.setObjectName(u"frameRightCatg1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(2)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frameRightCatg1.sizePolicy().hasHeightForWidth())
        self.frameRightCatg1.setSizePolicy(sizePolicy3)
        self.frameRightCatg1.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.frameRightCatg1.setAutoFillBackground(False)
        self.frameRightCatg1.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(170, 0, 0);\n"
"	border-radius: 3px;\n"
"	color: white;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(181, 78, 78)\n"
"}\n"
"\n"
"")
        self.frameRightCatg1.setFrameShape(QFrame.Shape.Box)
        self.frameRightCatg1.setFrameShadow(QFrame.Shadow.Sunken)
        self.verticalLayout_2 = QVBoxLayout(self.frameRightCatg1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label2Catg1 = QLabel(self.frameRightCatg1)
        self.label2Catg1.setObjectName(u"label2Catg1")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setStrikeOut(False)
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
        self.horizontalLayout_2 = QHBoxLayout(self.frame2Catg1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.treeViewCatg1 = QTreeView(self.frame2Catg1)
        self.treeViewCatg1.setObjectName(u"treeViewCatg1")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.treeViewCatg1.sizePolicy().hasHeightForWidth())
        self.treeViewCatg1.setSizePolicy(sizePolicy4)

        self.horizontalLayout_2.addWidget(self.treeViewCatg1)


        self.verticalLayout_2.addWidget(self.frame2Catg1)

        self.btnExportCatg1 = QPushButton(self.frameRightCatg1)
        self.btnExportCatg1.setObjectName(u"btnExportCatg1")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.btnExportCatg1.sizePolicy().hasHeightForWidth())
        self.btnExportCatg1.setSizePolicy(sizePolicy5)
        self.btnExportCatg1.setMinimumSize(QSize(70, 30))
        self.btnExportCatg1.setMaximumSize(QSize(60, 25))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(12)
        self.btnExportCatg1.setFont(font4)
        self.btnExportCatg1.setStyleSheet(u"")
        self.btnExportCatg1.setCheckable(True)

        self.verticalLayout_2.addWidget(self.btnExportCatg1)

        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(2, 25)

        self.horizontalLayout.addWidget(self.frameRightCatg1)


        self.verticalLayout.addWidget(self.frame1Catg1)

        MainWindow.setCentralWidget(self.centralwidgetCatg1)
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
        self.label1Catg1.setText(QCoreApplication.translate("MainWindow", u" Create New Category", None))
        self.newInputCatg1.setText("")
        self.newInputCatg1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter name of new category", None))
        self.btnCreateCatg1.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.label2Catg1.setText(QCoreApplication.translate("MainWindow", u"Categories", None))
        self.btnExportCatg1.setText(QCoreApplication.translate("MainWindow", u"Export", None))
    # retranslateUi

