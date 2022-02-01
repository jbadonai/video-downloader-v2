# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'splash.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(360, 111)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QFrame{\n"
"border: none;\n"
"}\n"
"\n"
"#centralwidget{\n"
"background-color: rgb(30, 30, 30);\n"
"}\n"
"\n"
" QLabel{\n"
"            color: rgb(0, 255, 127);\n"
"        }\n"
"\n"
"#frame_title{\n"
"border-bottom:5px solid qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));\n"
"border-top:5px solid qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));\n"
"    \n"
"    \n"
"}\n"
"\n"
"#labelStatus {\n"
"color: yellow;\n"
"}\n"
"\n"
"#frame_status{\n"
"margin-top: 5px;\n"
"margin-bottom: 5px;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_main = QtWidgets.QFrame(self.centralwidget)
        self.frame_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setObjectName("frame_main")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_main)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.frame_main)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.buttonClose = QtWidgets.QPushButton(self.frame_2)
        self.buttonClose.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/white icons/White icon/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonClose.setIcon(icon)
        self.buttonClose.setFlat(True)
        self.buttonClose.setObjectName("buttonClose")
        self.horizontalLayout_2.addWidget(self.buttonClose)
        self.horizontalLayout.addWidget(self.frame_2)
        self.verticalLayout_2.addWidget(self.frame, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.frame_title = QtWidgets.QFrame(self.frame_main)
        self.frame_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title.setObjectName("frame_title")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_title)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.labelTitle = QtWidgets.QLabel(self.frame_title)
        font = QtGui.QFont()
        font.setFamily("Ravie")
        font.setPointSize(14)
        self.labelTitle.setFont(font)
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle.setObjectName("labelTitle")
        self.verticalLayout_6.addWidget(self.labelTitle)
        self.verticalLayout_2.addWidget(self.frame_title)
        self.frame_status = QtWidgets.QFrame(self.frame_main)
        self.frame_status.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_status.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_status.setObjectName("frame_status")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_status)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.labelStatus = QtWidgets.QLabel(self.frame_status)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelStatus.setFont(font)
        self.labelStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.labelStatus.setWordWrap(True)
        self.labelStatus.setObjectName("labelStatus")
        self.verticalLayout_5.addWidget(self.labelStatus)
        self.verticalLayout_2.addWidget(self.frame_status)
        self.frame_progressbar = QtWidgets.QFrame(self.frame_main)
        self.frame_progressbar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_progressbar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_progressbar.setObjectName("frame_progressbar")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_progressbar)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.progressBar = QtWidgets.QProgressBar(self.frame_progressbar)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 10))
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 10))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_4.addWidget(self.progressBar)
        self.verticalLayout_2.addWidget(self.frame_progressbar)
        self.frame_loading = QtWidgets.QFrame(self.frame_main)
        self.frame_loading.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_loading.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_loading.setObjectName("frame_loading")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_loading)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelLoading = QtWidgets.QLabel(self.frame_loading)
        self.labelLoading.setAlignment(QtCore.Qt.AlignCenter)
        self.labelLoading.setObjectName("labelLoading")
        self.verticalLayout_3.addWidget(self.labelLoading)
        self.verticalLayout_2.addWidget(self.frame_loading, 0, QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.frame_main)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelTitle.setText(_translate("MainWindow", "JBAdonai Video Downloader"))
        self.labelStatus.setText(_translate("MainWindow", "Status message"))
        self.labelLoading.setText(_translate("MainWindow", "Loading..."))
import icons_rc
