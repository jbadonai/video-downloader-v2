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
from jbavdLibrary import StyleSheet, VideoDatabase, GeneralFunctions, LoadItemDataThread, ItemWindowDownloaderEngine
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

            self.my_menu = jba_menu(self)  # create instance of menu content and it's functions.

            self.container = self.myself.scrollAreaWidgetContents.layout()

            self.initialize()

        except Exception as e:
            print(f'An Error Occurred in ItemWindow > init(): \n>>>{e}')

    def initialize(self):

        # self.load_data()
        self.timer.start(200, self)
        self.functions.run_function(self.load_data)

    def restart(self):
        self.timer.start(200, self)

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

    def start_downloading(self):
        # time.sleep(20)
        if self.downloadingInProgress is False:
            print("Ready Now! Start downloading.")
            print(f'downloading triggered for: {self.videoURL}')
            self.downloadingInProgress = True
            self.emergencyStop = False
            # print("Now Downloading...")

            def item_downloading_connector(data):
                try:
                    # print(data)
                    # print(f"Receiving signal for {self.title}: {data}")
                    self.textETA.setText(data['eta'])
                    self.textDownloaded.setText(data['downloaded'])
                    self.textSpeed.setText(data['speed'])
                    self.textSize.setText(data['size'])
                    try:
                        percentage = data['percent']
                        percentage = str(percentage).replace("%","")
                        percentage = int(float(percentage).__round__())
                        # print(f"percentage: {percentage}", type(percentage))
                        self.progressBar.setValue(percentage)
                    except Exception as e:
                        print(f'Error in percentage: {e}')

                    if data['already_downloaded'] is True:

                        print("File already downloaded. Thanks")
                        self.database.set_status(self.videoURL, 'completed')
                        print("done!")
                        self.threadController[f"{str(self.title[:10]).strip().replace(' ','_')}"].stop()
                        # self.timer.stop()

                    if data['completed'] is True:
                        print("Download Completed. Thanks")
                        self.database.set_status(self.videoURL, 'completed')
                        print("done!")
                        self.threadController[f"{str(self.title[:10]).strip().replace(' ','_')}"].stop()

                    if data['emergency_stop'] is True:
                        print("Emergency stopped. thanks")
                        self.database.set_status(self.videoURL, 'stopped')
                        self.threadController[f"{str(self.title[:10]).strip().replace(' ','_')}"].stop()

                except Exception as e:
                    print(f'An Error Occurred in Common > ItemWindow > Start_downloading > item_downloading_conector: for [{self.title}]\n >>{e}')
                pass

            try:
                self.threadController[f"{str(self.title[:10]).strip().replace(' ','_')}"] = ItemWindowDownloaderEngine(self.downloadData, self)
                self.threadController[f"{str(self.title[:10]).strip().replace(' ','_')}"].start()
                self.threadController[f"{str(self.title[:10]).strip().replace(' ','_')}"].any_signal.connect(item_downloading_connector)
                pass
            except Exception as e:
                print(f"An Error Occurred in Common > ItemWindow > Start_downloading(): \n>>>{e}")

        pass

    def stop_downloading(self):
        if self.downloadingInProgress is True:
            # self.Logger.loggerEmergencyStop = True
            self.emergencyStop = True
            self.database.set_status(self.videoURL, 'stopped')
            self.downloadingInProgress = False
        else:
            self.database.set_status(self.videoURL, 'stopped')
        pass
        pass

    def get_index(self):
        try:
            if self.container.count() > 0:
                for x in range(self.container.count()):
                    title = self.container.itemAt(x).widget().title
                    if str(title).strip().lower() == str(self.title).strip().lower():
                        print(self.container.itemAt(x).widget().title)
                        return x

        except Exception as e:
            print(f"An error occurred in Common > ItemWindow > get_index(): \n>>{e}")

    def delete_index(self, index):
        try:
            self.container.itemAt(index).widget().deleteLater()
        except Exception as e:
            print(f"An error occurred in Common > ItemWindow > delete_index(): \n>>{e}")

    def timerEvent(self, e):
        try:
            self.status = self.database.get_status(self.videoURL)

            self.textStatus.setText(self.status)

            # if self.dataLoadingCompleted is True:
            if self.status == 'downloading':
                if self.myself.isReady is True:
                    self.start_downloading()
                else:
                    print("parent not ready...")

                pass

            if self.status == 'stopped' and self.downloadingInProgress is True:
                self.stop_downloading()
                print('stop action detected while still downloading. stopping now...')

            if self.status == 'waiting' and self.downloadingInProgress is True:
                self.stop_downloading()
                print('waiting action detected while still downloading. stopping now...')
                self.database.set_status(self.videoURL, 'waiting')

            if self.status == 'completed' and self.textStatus.text() == 'completed':
                print('stopping the timer')
                self.timer.stop()
            pass


        except Exception as e:
            print(f"An Error occurred in Common > Itemwindow > timer()::{self.title}: \n{e}")
            if str(e).strip() == 'list index out of range':
                self.timer.stop()
                self.close()

    def contextMenuEvent(self, event):
        try:
            menu = QMenu(self)  # create an instance of the menu
            menu.setStyleSheet(StyleSheet().menu_style)  # apply custom sytle to the menu
            menu_list = self.my_menu.auto_menu()  # get the content of the menu
            # print( menu_list)
            # loop through the menu item list to apply icon and display them.
            for m in menu_list:
                menu_list[m] = eval(str(menu_list[m]))

                if str(m).__contains__('separator'):
                    menu_list[m]['name'] = menu.addSeparator()
                else:
                    menu_list[m]['name'] = menu.addAction(menu_list[m]['text'])
                    menu_list[m]['name'].setIcon(QIcon(menu_list[m]['icon']))

            action = menu.exec_(self.mapToGlobal(event.pos()))

            for m in menu_list:

                if action == menu_list[m]['name']:
                    #   get the function name to be executed and run / evaluate it.
                    print('here')
                    eval(f"self.my_menu.{menu_list[m]['function_name']}")
                    break

        except Exception as e:
            print(f"An error occurred in  itemWindow >  contextMenuEvent(): \n>>{e}")

    def closeEvent(self, a0):
        if self.status != 'completed':
            self.stop_downloading()
