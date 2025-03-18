# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GestoSync.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont, QIcon)
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout)
import resources

class UI_GestoSync(object):
    def setupUi(self, GestoSync):
        if not GestoSync.objectName():
            GestoSync.setObjectName(u"GestoSync")
        GestoSync.resize(800, 650)
        GestoSync.setMinimumSize(QSize(800, 650))
        icon = QIcon()
        icon.addFile(u":/Labels/GestoSync.ico", QSize(), QIcon.Normal, QIcon.Off)
        GestoSync.setWindowIcon(icon)
        GestoSync.setStyleSheet(u"QWidget#Inmoov{\n"
"background-color: \n"
"	qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,\n"
"        stop: 0 rgb(50, 50, 50),\n"
"        stop: 0.5 rgb(30, 30, 30),\n"
"        stop: 1 rgb(50, 50, 50)\n"
"    );\n"
"}\n"
"\n"
"QSpinBox {\n"
"selection-background-color: transparent;\n"
"  background-color: rgba(80, 80, 80, 150);\n"
"  color: white;\n"
"  border: 2px solid rgba(150, 150, 150,150); \n"
"  border-radius: 10px;\n"
"  padding: 4 px;\n"
"  subcontrol-origin: margin;\n"
"  subcontrol-position: top right;\n"
"}\n"
"\n"
"QAbstractSpinBox::up-button {\n"
"  subcontrol-origin: padding;\n"
"  subcontrol-position: top right;\n"
"  width: 15px;\n"
"  height: 15px;\n"
"  border-left-width: 1px;\n"
"  border-left-color: rgb(150, 150, 150);\n"
"  border-left-style: solid;\n"
"  border-top-right-radius: 8px;\n"
"  background-color: rgb(255, 120, 20);\n"
"  image: url(:Icons/up_arrow.png);\n"
"}\n"
"\n"
"QAbstractSpinBox::down-button {\n"
"  subcontrol-origin: padding;\n"
"  subcontrol-position: bottom right;\n"
""
                        "  width: 15px;\n"
"  height: 15px;\n"
"  border-left-width: 1px;\n"
"  border-left-color: rgb(150, 150, 150);\n"
"  border-left-style: solid;\n"
"  border-bottom-right-radius: 8px;\n"
"  background-color: rgb(255, 120, 20);\n"
"   image: url(:/Icons/down_arrow.png);\n"
"}\n"
"\n"
"QCheckBox  {\n"
"	spacing: 0 px;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 35 px;\n"
"    height: 35 px;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    image: url(:/Icons/male.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"     image: url(:/Icons/female.png);\n"
"}\n"
"\n"
"QCheckBox:hover {\n"
"   background-color: rgba(128,128,128,50);\n"
"}\n"
"\n"
"QCheckBox:pressed {\n"
"   background-color: rgba(128,128,128,100);\n"
"}\n"
"\n"
" QLineEdit {\n"
"    background-color: rgba(80, 80, 80, 150);\n"
"    border-radius: 10px;\n"
"    padding:2px;\n"
"    border: 2px solid rgba(150, 150, 150, 150);\n"
"    color: silver;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	background-color: rgba(80, 80, 8"
                        "0, 150);\n"
"    border: 2px solid rgba(255, 255, 255, 150);\n"
"}\n"
"\n"
"QFrame {\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	background-color: rgba(80, 80, 80, 150);\n"
"    border: 2px solid rgba(255, 255, 255, 150);\n"
"\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgba(80, 80, 80, 150);\n"
"	color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    padding: 5px; \n"
" 	border: 2px solid rgba(150, 150, 150,150); \n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"color: rgba(255,255,255,100);\n"
"}\n"
"\n"
"QRadioButton {\n"
"	color: white;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:  18px;\n"
"    height: 18px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    image: url(:/Icons/unchecked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked:hover {\n"
"    image: url(:/Icons/hover.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    image: url(:/Icons/checked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover {\n"
"    image: url(:/Icons/"
                        "checked_hover.png);\n"
"}\n"
"\n"
"QMessageBox {\n"
" background-color: \n"
"	qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,\n"
"        stop: 0 rgb(50, 50, 50),\n"
"        stop: 0.5 rgb(30, 30, 30),\n"
"        stop: 1 rgb(50, 50, 50)\n"
"    );\n"
"  width: 400px; \n"
"  height: 400px;\n"
"}\n"
"QMessageBox QLabel {\n"
"color: white;\n"
"font-size: 15px;\n"
"}\n"
"QMessageBox QPushButton {\n"
"   	background-color: rgba(80, 80, 80, 150);\n"
"	color: rgb(255, 255, 255);\n"
"    border-radius: 10px;\n"
"    padding: 5px; \n"
" 	border: 2px solid rgba(150, 150, 150,150); \n"
"  	font-size: 14px;\n"
"  	min-height: 15px; \n"
"  	min-width: 60px;\n"
"}\n"
"\n"
"QMessageBox QPushButton:hover {\n"
"  background-color:rgba(255, 144, 0, 50);    \n"
"}\n"
"\n"
"QMessageBox QPushButton:pressed {\n"
"   background-color:rgba(255, 144, 0, 150);\n"
"    border: 2px solid #CCCCCC; \n"
"}\n"
"\n"
"\n"
"QAbstractScrollArea\n"
"{\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-"
                        "color:rgb(30, 30, 30);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border: none;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background: rgb(200, 200, 200);\n"
"    min-height: 5px;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover\n"
"{\n"
"   background: rgb(255, 144, 0);\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:pressed\n"
"{\n"
"   background: rgb(255, 80, 0);\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image:  url(:/Icons/up_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    margin: 3px 0px 3px 0px;\n"
"    border-image :url(:/Icons/down_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical:hover,QScrollBar::sub-line:verti"
                        "cal:on\n"
"{\n"
"\n"
"    border-image: url(:/Icons/up_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:hover, QScrollBar::add-line:vertical:on\n"
"{\n"
"    border-image: url(:/Icons/down_arrow.png);\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"}")
        self.verticalLayout = QVBoxLayout(GestoSync)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 10, 15, 10)
        self.middleFrame = QFrame(GestoSync)
        self.middleFrame.setObjectName(u"middleFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.middleFrame.sizePolicy().hasHeightForWidth())
        self.middleFrame.setSizePolicy(sizePolicy)
        self.middleFrame.setStyleSheet(u"QWidget {\n"
"    background-color: rgb(40, 40, 40);\n"
"}")
        self.middleFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.middleFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.cameraLayout = QHBoxLayout(self.middleFrame)
        self.cameraLayout.setSpacing(30)
        self.cameraLayout.setObjectName(u"cameraLayout")
        self.cameraLayout.setContentsMargins(20, 0, 20, 0)
        self.firstCameraFrame = QFrame(self.middleFrame)
        self.firstCameraFrame.setObjectName(u"firstCameraFrame")
        self.firstCameraFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.firstCameraFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.firstCameraFrame)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.firstCameraControlFrame = QFrame(self.firstCameraFrame)
        self.firstCameraControlFrame.setObjectName(u"firstCameraControlFrame")
        self.firstCameraControlFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.firstCameraControlFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.firstCameraControlFrame)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.firstRotateLeftButton = QPushButton(self.firstCameraControlFrame)
        self.firstRotateLeftButton.setObjectName(u"firstRotateLeftButton")
        self.firstRotateLeftButton.setStyleSheet(u"QPushButton{\n"
"background-color: transparent;\n"
"border: None;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: rgba(128,128,128,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   background-color: rgba(128,128,128,100);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/rotate_left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.firstRotateLeftButton.setIcon(icon1)
        self.firstRotateLeftButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_11.addWidget(self.firstRotateLeftButton)

        self.firstMirrorButton = QPushButton(self.firstCameraControlFrame)
        self.firstMirrorButton.setObjectName(u"firstMirrorButton")
        self.firstMirrorButton.setStyleSheet(u"QPushButton{\n"
"background-color: transparent;\n"
"border: None;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: rgba(128,128,128,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   background-color: rgba(128,128,128,100);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/mirror.png", QSize(), QIcon.Normal, QIcon.Off)
        self.firstMirrorButton.setIcon(icon2)
        self.firstMirrorButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_11.addWidget(self.firstMirrorButton)

        self.firstRotateRightButton = QPushButton(self.firstCameraControlFrame)
        self.firstRotateRightButton.setObjectName(u"firstRotateRightButton")
        self.firstRotateRightButton.setStyleSheet(u"QPushButton{\n"
"background-color: transparent;\n"
"border: None;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: rgba(128,128,128,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   background-color: rgba(128,128,128,100);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/rotate_right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.firstRotateRightButton.setIcon(icon3)
        self.firstRotateRightButton.setIconSize(QSize(25, 25))

        self.horizontalLayout_11.addWidget(self.firstRotateRightButton)

        self.firstToggleButton = QPushButton(self.firstCameraControlFrame)
        self.firstToggleButton.setObjectName(u"firstToggleButton")
        self.firstToggleButton.setStyleSheet(u"QPushButton{\n"
"background-color: transparent;\n"
"border: None;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"   background-color: rgba(128,128,128,50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"   background-color: rgba(128,128,128,100);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/Icons/camera_on.png", QSize(), QIcon.Normal, QIcon.Off)
        self.firstToggleButton.setIcon(icon4)
        self.firstToggleButton.setIconSize(QSize(30, 30))
        self.firstToggleButton.setChecked(False)

        self.horizontalLayout_11.addWidget(self.firstToggleButton)


        self.verticalLayout_4.addWidget(self.firstCameraControlFrame, 0, Qt.AlignmentFlag.AlignHCenter)

        self.firstCameraLabel = QLabel(self.firstCameraFrame)
        self.firstCameraLabel.setObjectName(u"firstCameraLabel")
        sizePolicy.setHeightForWidth(self.firstCameraLabel.sizePolicy().hasHeightForWidth())
        self.firstCameraLabel.setSizePolicy(sizePolicy)
        self.firstCameraLabel.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(18)
        self.firstCameraLabel.setFont(font)
        self.firstCameraLabel.setStyleSheet(u"border-width: 3px;\n"
"border-color: rgb(74,73,120);\n"
"border-radius: 15px;\n"
"color:white;\n"
"")
        self.firstCameraLabel.setScaledContents(True)
        self.firstCameraLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.firstCameraLabel)

        self.firstCameraUrlFrame = QFrame(self.firstCameraFrame)
        self.firstCameraUrlFrame.setObjectName(u"firstCameraUrlFrame")
        self.firstCameraUrlFrame.setStyleSheet(u"")
        self.firstCameraUrlFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.firstCameraUrlFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.firstCameraUrlFrame)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.changeFirstUrlLabel = QLabel(self.firstCameraUrlFrame)
        self.changeFirstUrlLabel.setObjectName(u"changeFirstUrlLabel")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        self.changeFirstUrlLabel.setFont(font1)
        self.changeFirstUrlLabel.setStyleSheet(u"color:white;")

        self.horizontalLayout_6.addWidget(self.changeFirstUrlLabel)

        self.firstUrlLineEdit = QLineEdit(self.firstCameraUrlFrame)
        self.firstUrlLineEdit.setObjectName(u"firstUrlLineEdit")
        self.firstUrlLineEdit.setMinimumSize(QSize(160, 0))
        self.firstUrlLineEdit.setFont(font1)

        self.horizontalLayout_6.addWidget(self.firstUrlLineEdit)


        self.verticalLayout_4.addWidget(self.firstCameraUrlFrame, 0, Qt.AlignmentFlag.AlignHCenter)


        self.cameraLayout.addWidget(self.firstCameraFrame)


        self.verticalLayout.addWidget(self.middleFrame)

        self.bottomFrame = QFrame(GestoSync)
        self.bottomFrame.setObjectName(u"bottomFrame")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.bottomFrame.setFont(font2)
        self.bottomFrame.setStyleSheet(u"QWidget {\n"
"    background-color: rgb(40, 40, 40);\n"
"}")
        self.bottomFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.bottomFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.bottomFrame)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(15, 0, 15, 0)
        self.capture_frame = QFrame(self.bottomFrame)
        self.capture_frame.setObjectName(u"capture_frame")
        self.capture_frame.setStyleSheet(u"QFrame #speakFrame{\n"
"background-color:rgba(55, 55, 55, 120);\n"
"}")
        self.capture_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.capture_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.capture_frame)
        self.verticalLayout_10.setSpacing(5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(10, 10, 10, 5)
        self.file_name_edit = QTextEdit(self.capture_frame)
        self.file_name_edit.setObjectName(u"textToSpeechEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.file_name_edit.sizePolicy().hasHeightForWidth())
        self.file_name_edit.setSizePolicy(sizePolicy1)
        self.file_name_edit.setMaximumSize(QSize(16777215, 60))
        font3 = QFont()
        font3.setPointSize(12)
        self.file_name_edit.setFont(font3)
        self.file_name_edit.setStyleSheet(u" QTextEdit {\n"
"    background-color: rgba(80, 80, 80, 150);\n"
"    border-radius: 10px;\n"
"    padding:2px;\n"
"    border: 2px solid rgba(150, 150, 150, 150);\n"
"    color: silver;\n"
"}\n"
"\n"
"QTextEdit:hover {\n"
"	background-color: rgba(80, 80, 80, 150);\n"
"    border: 2px solid rgba(255, 255, 255, 150);\n"
"}")
        self.file_name_edit.setAutoFormatting(QTextEdit.AutoFormattingFlag.AutoNone)
        self.file_name_edit.setOverwriteMode(True)

        self.verticalLayout_10.addWidget(self.file_name_edit)

        self.capture_name = QFrame(self.capture_frame)
        self.capture_name.setObjectName(u"capture_name")
        self.capture_name.setFrameShape(QFrame.Shape.StyledPanel)
        self.capture_name.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.capture_name)
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.capture_button = QPushButton(self.capture_name)
        self.capture_button.setObjectName(u"speakButton")
        sizePolicy1.setHeightForWidth(self.capture_button.sizePolicy().hasHeightForWidth())
        self.capture_button.setSizePolicy(sizePolicy1)
        self.capture_button.setMinimumSize(QSize(50, 35))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(14)
        font4.setBold(False)
        self.capture_button.setFont(font4)
        self.capture_button.setStyleSheet(u"QPushButton:hover {\n"
"    background-color:rgba(255, 144, 0, 50);    \n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:rgba(255, 144, 0, 150);\n"
"    border: 2px solid #CCCCCC; \n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/Icons/male.png", QSize(), QIcon.Normal, QIcon.Off)
        self.capture_button.setIcon(icon5)
        self.capture_button.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.capture_button)


        self.verticalLayout_10.addWidget(self.capture_name)


        self.horizontalLayout_7.addWidget(self.capture_frame, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout.addWidget(self.bottomFrame)


        self.retranslateUi(GestoSync)

        QMetaObject.connectSlotsByName(GestoSync)
    # setupUi

    def retranslateUi(self, GestoSync):
        GestoSync.setWindowTitle(QCoreApplication.translate("GestoSync", u"GestoSync", None))
        self.firstRotateLeftButton.setText("")
        self.firstMirrorButton.setText("")
        self.firstRotateRightButton.setText("")
        self.firstToggleButton.setText("")
        self.firstCameraLabel.setText(QCoreApplication.translate("GestoSync", u"Cam 1\n"
"(No Link)", None))
        self.changeFirstUrlLabel.setText(QCoreApplication.translate("GestoSync", u"Camera URL:", None))
        self.firstUrlLineEdit.setText(QCoreApplication.translate("GestoSync", u"0", None))
        self.firstUrlLineEdit.setPlaceholderText(QCoreApplication.translate("GestoSync", u"Change Camera URL", None))
        self.file_name_edit.setDocumentTitle("")
        self.file_name_edit.setPlaceholderText(QCoreApplication.translate("GestoSync", u"Name The Capture", None))
        self.capture_button.setText(QCoreApplication.translate("GestoSync", u" Capture", None))
    # retranslateUi

