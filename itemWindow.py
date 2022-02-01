import os
import signal
import time

from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsDropShadowEffect, QSizeGrip,QWidget, QMenu, QMessageBox
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve, QProcess, QEvent, QBasicTimer
from PyQt5.QtGui import QColor, QIcon,QPixmap

# import common
from ui import my_interface_, my_item_window_interface_
import boot


from win10toast import ToastNotifier
import pyautogui
import psutil
import shutil
from datetime import datetime, date
import sys
from jbavdLibrary import StyleSheet, VideoDatabase, GeneralFunctions, LoadItemDataThread
from jbaMenu import JbaMenuClass as jba_menu
import requests
import random

restart_ready = False


class ItemWindow(QMainWindow, my_item_window_interface_.Ui_MainWindow):
    def __init__(self, data, my_parent, parent=None):
        super(ItemWindow, self).__init__(parent)
        try:
            self.setupUi(self)
            self.centralwidget.setStyleSheet(StyleSheet().central_widget)

            self.downloadData = data
            self.myself = my_parent
            self.scrollAreaWidgetContentsLayout = self.myself.scrollAreaWidgetContents.layout()
            self.threadController = self.myself.threadController
            self.database = self.myself.database
            # print(data)
            self.downloadVideo = bool(data['download_video'])
            self.downloadAll = bool(data['download_all'])
            self.downloadFormat = data['format']
            self.videoURL = data['url']
            self.title = data['title']
            self.isPlaylist = bool(data['is_playlist'])
            self.playlistIndex = data['playlist_index']
            self.playlistTitle = data['playlist_title']
            self.playlistURL = data['playlist_url']
            self.thumbnail = data['thumbnail']
            self.status = data['status']
            self.downloadLocation = data['download_location']

            self.buttonErrorAlert.setVisible(False)
            self.buttonWeb.setVisible(False)
            self.checkBoxSelect.setVisible(False)

            self.dataLoadingCompleted = False   # controls loading of download info here like image....
            self.downloadingInProgress = False

            self.functions = GeneralFunctions()

            self.emergencyStop = False

            self.timer = QBasicTimer()

            self.initialize()

        except Exception as e:
            print(f'An Error Occurred in ItemWindow > init(): \n>>>{e}')

    def initialize(self):

        # self.load_data()
        # self.timer.start(200, self)
        self.functions.run_function(self.load_data)

    def display_content(self):

        def start():
            try:
                if self.isPlaylist is True:
                    self.textTitle.setText(f"{self.playlistIndex}. [{self.playlistTitle}] - {self.title}")
                    pass
                else:
                    self.textTitle.setText(self.title)
            except Exception as e:
                print(f"An error occurred in  Common > LoadItemDataThread > display_content() > start(): \n>>{e}")

            try:
                # image data is in byte. need to be saved to file
                if os.path.exists("temp") is False:
                    os.makedirs("temp")

                img_data = requests.get(self.thumbnail).content
                tempFilename = f"temp_{random.randrange(1000, 9999)}"

                # checkpoint 1
                with open(f"temp\\{tempFilename}", 'wb') as f:
                    f.write(img_data)

                try:
                    self.labelImage.setPixmap(QPixmap(f"temp\\{tempFilename}"))
                    self.labelImage.setScaledContents(True)
                except Exception as e:
                    self.labelImage.setText("image Error")

            except:
                self.my_parent.labelImage.setText("No Image")

        self.functions.run_function(start)
        # start()

    def load_data(self):
        if self.downloadVideo is True:
            self.buttonAudioOnly.setIcon(QIcon(':/white icons/White icon/film.svg'))
        else:
            self.buttonAudioOnly.setIcon(QIcon(':/white icons/White icon/music.svg'))

        def load_data_connector(data):
            pass

        try:
            tempFilename = f"temp_{random.randrange(1000, 9999)}"
            self.threadController[tempFilename] = LoadItemDataThread(self.downloadData, self)
            self.threadController[tempFilename].start()
            self.threadController[tempFilename].any_signal.connect(load_data_connector)

        except Exception as e:
            print(f"An Error Occurred in Common > ItemWindow > load_data(): {e}")
        pass
