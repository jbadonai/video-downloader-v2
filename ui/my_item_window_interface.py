# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'my_item_window_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(603, 127)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 127))
        MainWindow.setStyleSheet("color: rgb(0, 255, 127);\n"
"background-color: rgb(30, 30, 30);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QFrame{\n"
"border: 1px solid green\n"
"\n"
"}\n"
"\n"
"QLabel{\n"
"color: rgb(0, 255, 127);\n"
"}\n"
"\n"
"\n"
"#frame_main{\n"
"margin:5px;\n"
"padding:5px;\n"
"border:1px solid white;\n"
"\n"
"}\n"
"\n"
"#frame_status{\n"
"\n"
"\n"
"}\n"
"\n"
"#frame_progress_bar{\n"
"\n"
"}\n"
"\n"
"#frame_statistics{\n"
"margin-bottom:-2px;\n"
"padding:4px;\n"
"border-top:1px solid white;\n"
"border-left:1px solid white;\n"
"border-right:1px solid white;\n"
"border-radius:5px;\n"
"background:rgb(30, 30, 30);\n"
"}\n"
"\n"
"#textSize, #textDownloaded, #textSpeed, #textETA{\n"
"color:white;\n"
"}\n"
"\n"
"#centralwidget{\n"
"background:rgb(60, 60, 60);\n"
"}\n"
"\n"
"\n"
"#frame_image{\n"
"border-radius:50px;\n"
"margin-right:5px;\n"
"margin-left:2px;\n"
"\n"
"}\n"
"\n"
"#frame_image QLabel{\n"
"border-radius:50px;\n"
"background: rgb(121, 121, 121);\n"
"color: white;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame_select = QtWidgets.QFrame(self.centralwidget)
        self.frame_select.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_select.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_select.setObjectName("frame_select")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_select)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBoxSelect = QtWidgets.QCheckBox(self.frame_select)
        self.checkBoxSelect.setText("")
        self.checkBoxSelect.setObjectName("checkBoxSelect")
        self.verticalLayout.addWidget(self.checkBoxSelect)
        self.horizontalLayout_10.addWidget(self.frame_select)
        self.frame_main = QtWidgets.QFrame(self.centralwidget)
        self.frame_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setObjectName("frame_main")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_main)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_top = QtWidgets.QFrame(self.frame_main)
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_top)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_image = QtWidgets.QFrame(self.frame_top)
        self.frame_image.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_image.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_image.setObjectName("frame_image")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_image)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.labelImage = QtWidgets.QLabel(self.frame_image)
        self.labelImage.setMinimumSize(QtCore.QSize(80, 80))
        self.labelImage.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.labelImage.setFont(font)
        self.labelImage.setScaledContents(True)
        self.labelImage.setAlignment(QtCore.Qt.AlignCenter)
        self.labelImage.setWordWrap(True)
        self.labelImage.setObjectName("labelImage")
        self.verticalLayout_4.addWidget(self.labelImage)
        self.horizontalLayout.addWidget(self.frame_image, 0, QtCore.Qt.AlignLeft)
        self.frame_details = QtWidgets.QFrame(self.frame_top)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_details.sizePolicy().hasHeightForWidth())
        self.frame_details.setSizePolicy(sizePolicy)
        self.frame_details.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_details.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_details.setObjectName("frame_details")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_details)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_title = QtWidgets.QFrame(self.frame_details)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_title.sizePolicy().hasHeightForWidth())
        self.frame_title.setSizePolicy(sizePolicy)
        self.frame_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title.setObjectName("frame_title")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_title)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.textTitle = QtWidgets.QLabel(self.frame_title)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textTitle.sizePolicy().hasHeightForWidth())
        self.textTitle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textTitle.setFont(font)
        self.textTitle.setScaledContents(True)
        self.textTitle.setWordWrap(True)
        self.textTitle.setObjectName("textTitle")
        self.verticalLayout_7.addWidget(self.textTitle)
        self.verticalLayout_5.addWidget(self.frame_title)
        self.frame_statistics = QtWidgets.QFrame(self.frame_details)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_statistics.sizePolicy().hasHeightForWidth())
        self.frame_statistics.setSizePolicy(sizePolicy)
        self.frame_statistics.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_statistics.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_statistics.setObjectName("frame_statistics")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_statistics)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_size = QtWidgets.QFrame(self.frame_statistics)
        self.frame_size.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_size.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_size.setObjectName("frame_size")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_size)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelSize = QtWidgets.QLabel(self.frame_size)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelSize.setFont(font)
        self.labelSize.setObjectName("labelSize")
        self.horizontalLayout_3.addWidget(self.labelSize, 0, QtCore.Qt.AlignLeft)
        self.textSize = QtWidgets.QLabel(self.frame_size)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textSize.sizePolicy().hasHeightForWidth())
        self.textSize.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textSize.setFont(font)
        self.textSize.setAlignment(QtCore.Qt.AlignCenter)
        self.textSize.setObjectName("textSize")
        self.horizontalLayout_3.addWidget(self.textSize)
        self.horizontalLayout_2.addWidget(self.frame_size)
        self.frame_downloaded = QtWidgets.QFrame(self.frame_statistics)
        self.frame_downloaded.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_downloaded.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_downloaded.setObjectName("frame_downloaded")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_downloaded)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.labelDownloaded = QtWidgets.QLabel(self.frame_downloaded)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelDownloaded.setFont(font)
        self.labelDownloaded.setObjectName("labelDownloaded")
        self.horizontalLayout_4.addWidget(self.labelDownloaded, 0, QtCore.Qt.AlignLeft)
        self.textDownloaded = QtWidgets.QLabel(self.frame_downloaded)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textDownloaded.sizePolicy().hasHeightForWidth())
        self.textDownloaded.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textDownloaded.setFont(font)
        self.textDownloaded.setAlignment(QtCore.Qt.AlignCenter)
        self.textDownloaded.setObjectName("textDownloaded")
        self.horizontalLayout_4.addWidget(self.textDownloaded)
        self.horizontalLayout_2.addWidget(self.frame_downloaded)
        self.frame_speed = QtWidgets.QFrame(self.frame_statistics)
        self.frame_speed.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_speed.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_speed.setObjectName("frame_speed")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_speed)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.labelSpeed = QtWidgets.QLabel(self.frame_speed)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelSpeed.setFont(font)
        self.labelSpeed.setObjectName("labelSpeed")
        self.horizontalLayout_5.addWidget(self.labelSpeed, 0, QtCore.Qt.AlignLeft)
        self.textSpeed = QtWidgets.QLabel(self.frame_speed)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textSpeed.sizePolicy().hasHeightForWidth())
        self.textSpeed.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textSpeed.setFont(font)
        self.textSpeed.setAlignment(QtCore.Qt.AlignCenter)
        self.textSpeed.setObjectName("textSpeed")
        self.horizontalLayout_5.addWidget(self.textSpeed)
        self.horizontalLayout_2.addWidget(self.frame_speed)
        self.frame_eta = QtWidgets.QFrame(self.frame_statistics)
        self.frame_eta.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_eta.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_eta.setObjectName("frame_eta")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_eta)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.labelETA = QtWidgets.QLabel(self.frame_eta)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelETA.setFont(font)
        self.labelETA.setObjectName("labelETA")
        self.horizontalLayout_6.addWidget(self.labelETA, 0, QtCore.Qt.AlignLeft)
        self.textETA = QtWidgets.QLabel(self.frame_eta)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textETA.sizePolicy().hasHeightForWidth())
        self.textETA.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textETA.setFont(font)
        self.textETA.setAlignment(QtCore.Qt.AlignCenter)
        self.textETA.setObjectName("textETA")
        self.horizontalLayout_6.addWidget(self.textETA)
        self.horizontalLayout_2.addWidget(self.frame_eta)
        self.verticalLayout_5.addWidget(self.frame_statistics, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout.addWidget(self.frame_details)
        self.frame_status = QtWidgets.QFrame(self.frame_top)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_status.sizePolicy().hasHeightForWidth())
        self.frame_status.setSizePolicy(sizePolicy)
        self.frame_status.setMaximumSize(QtCore.QSize(130, 16777215))
        self.frame_status.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_status.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_status.setObjectName("frame_status")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_status)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame = QtWidgets.QFrame(self.frame_status)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.textStatus = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textStatus.sizePolicy().hasHeightForWidth())
        self.textStatus.setSizePolicy(sizePolicy)
        self.textStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.textStatus.setWordWrap(True)
        self.textStatus.setObjectName("textStatus")
        self.verticalLayout_9.addWidget(self.textStatus)
        self.verticalLayout_6.addWidget(self.frame)
        self.frame_3 = QtWidgets.QFrame(self.frame_status)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_6.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.frame_status)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.buttonWeb = QtWidgets.QPushButton(self.frame_5)
        self.buttonWeb.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonWeb.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/blue icons/blue icon/globe.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonWeb.setIcon(icon)
        self.buttonWeb.setIconSize(QtCore.QSize(20, 20))
        self.buttonWeb.setFlat(True)
        self.buttonWeb.setObjectName("buttonWeb")
        self.horizontalLayout_9.addWidget(self.buttonWeb)
        self.horizontalLayout_7.addWidget(self.frame_5, 0, QtCore.Qt.AlignLeft)
        self.buttonAudioOnly = QtWidgets.QPushButton(self.frame_2)
        self.buttonAudioOnly.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/white icons/White icon/music.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonAudioOnly.setIcon(icon1)
        self.buttonAudioOnly.setIconSize(QtCore.QSize(20, 20))
        self.buttonAudioOnly.setFlat(True)
        self.buttonAudioOnly.setObjectName("buttonAudioOnly")
        self.horizontalLayout_7.addWidget(self.buttonAudioOnly)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.buttonErrorAlert = QtWidgets.QPushButton(self.frame_4)
        self.buttonErrorAlert.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonErrorAlert.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.buttonErrorAlert.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/red icons/red icon/alert-triangle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonErrorAlert.setIcon(icon2)
        self.buttonErrorAlert.setIconSize(QtCore.QSize(20, 20))
        self.buttonErrorAlert.setFlat(True)
        self.buttonErrorAlert.setObjectName("buttonErrorAlert")
        self.horizontalLayout_8.addWidget(self.buttonErrorAlert)
        self.horizontalLayout_7.addWidget(self.frame_4, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_6.addWidget(self.frame_2)
        self.horizontalLayout.addWidget(self.frame_status)
        self.verticalLayout_3.addWidget(self.frame_top)
        self.frame_progress_bar = QtWidgets.QFrame(self.frame_main)
        self.frame_progress_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_progress_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_progress_bar.setObjectName("frame_progress_bar")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_progress_bar)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.progressBar = QtWidgets.QProgressBar(self.frame_progress_bar)
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 5))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        self.verticalLayout_3.addWidget(self.frame_progress_bar)
        self.horizontalLayout_10.addWidget(self.frame_main)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelImage.setText(_translate("MainWindow", "no image"))
        self.textTitle.setText(_translate("MainWindow", "Title"))
        self.labelSize.setText(_translate("MainWindow", "Size:"))
        self.textSize.setText(_translate("MainWindow", "0 Mb"))
        self.labelDownloaded.setText(_translate("MainWindow", "Downloaded:"))
        self.textDownloaded.setText(_translate("MainWindow", "0 Mb"))
        self.labelSpeed.setText(_translate("MainWindow", "Speed:"))
        self.textSpeed.setText(_translate("MainWindow", "0 kb/s"))
        self.labelETA.setText(_translate("MainWindow", "ETA:"))
        self.textETA.setText(_translate("MainWindow", "0 sec"))
        self.textStatus.setText(_translate("MainWindow", "jesusislordoverallthe and forever earth"))
import icons_rc
