import os
import signal
import time

from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsDropShadowEffect, QRadioButton,QWidget, QMenu, QMessageBox
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve, QProcess, QEvent, QBasicTimer
from PyQt5.QtGui import QColor, QIcon

# import common
from ui import my_interface_, my_item_window_interface_
import boot


from win10toast import ToastNotifier
import pyautogui
import psutil
import shutil
from datetime import datetime, date
import sys
from jbavdLibrary import StyleSheet, VideoDatabase, GeneralFunctions, AddNewDownloadThread, AddNewOkThread
from jbaMenu import JbaMenuClass as jba_menu
from itemWindow import ItemWindow


class UserActions():
    def __init__(self, myself):
        self.myself = myself
        self.threadController = self.myself.threadController
        self.generalFunction = GeneralFunctions()
        self.database = self.myself.database
        self.busy = False
        self.raw_data = None
        self.isPlaylist = None

    def add_new_download(self):
        self.myself.show_add_new_page()
        myparent = self.myself

        def add_new_download_connector(data):
            try:
                if 'raw_data' in data:
                    self.raw_data = data['raw_data']
                    self.isPlaylist = data['isplaylist']

                if 'message' in data:
                    print(data['message'])
                    self.myself.message = data['message']

                if 'finished' in data:
                    print('Now Finished')
                    # self.threadController.pop('add new download', None)
                    self.myself.busy = False

                # check url validity and display it accordingly
                if 'valid_url' in data:
                    if data['valid_url'] is True:
                        self.myself.textURL.setText(data['url'])
                        self.myself.buttonGetInfo.setVisible(False)
                        self.myself.textURL.setStyleSheet("background-color: None")
                    else:
                        self.myself.buttonGetInfo.setVisible(True)
                        self.myself.textURL.setStyleSheet("background-color: red; color:white;")

                if 'unsupported_url' in data:
                    QMessageBox.warning(self.myself, "unsupported URL", f"Unable to process the provided URL "
                                                                 f"possibly a non video URL was supplied. Please"
                                                                 f" check the supplied URL below and try again."
                                                                 f"\n\n {data['url']}")
                    # self.buttonGetInfo.setVisible(True)
                    self.myself.clear()
                    self.myself.textURL.setFocus()
                    self.myself.textURL.setStyleSheet("background-color: red; color: white;")

                if 'download_location' in data:
                    self.myself.textAddNewDownloadLocation.setText(data['download_location'])

                if 'status' in data:
                    if data['status'] != 'waiting' and data['status'] != 'completed':
                        # data.append(f"{status['result']}")
                        self.rb = QRadioButton()
                        self.rb.setText(f"{data['status']}")
                        # self.videoFormatLayout.layout().addWidget(self.rb)
                        self.myself.scrollAreaWidgetContents_VideoFormat.layout().addWidget(self.rb)
                        # container.addWidget(self.rb)

                if 'url_exists' in data:
                    # if url exists in database do not proceed.
                    url = str(data["url"])
                    status = self.database.get_status_by_playlist_url(url)
                    print(f'status: {status}')
                    if status != 'deleted':
                        QMessageBox.information(self.myself, 'URL exists', f'Provided URL  below exists in the download list. Please select/copy another URL to download. \n\n "[ {str(data["url"])} ]"')
                        self.myself.buttonAddNewCancel.click()
                    else:
                        ans = QMessageBox.question(self.myself, "Restore Deleted download", "This URL exists but was deleted. Will you like to restore it?", QMessageBox.Yes | QMessageBox.No)
                        if ans == QMessageBox.No:
                            self.myself.buttonAddNewCancel.click()
                        else:
                            self.myself.buttonAddNewCancel.click()
                            allDataInDb = self.database.get_all_video_data()
                            for data in allDataInDb:
                                d = self.generalFunction.database_list_to_dictionary(data)
                                # print(d)
                                if d['playlist_url'] == url:
                                    self.database.set_status(d['url'], "waiting")
                                    win = ItemWindow(d, self.myself)
                                    self.myself.scrollAreaWidgetContents.layout().addWidget(win)

                            pass
                if 'download_data' in data:
                    # print('OK clicked and data acquired.')
                    data = data['download_data']

                    items = self.generalFunction.database_list_to_dictionary(data)
                    print(f'items after: {items}')

                    win = ItemWindow(data=items, my_parent=myparent)
                    self.myself.scrollAreaWidgetContents.layout().addWidget(win)
                    pass

            except Exception as e:
                print(f"An error occurred in 'add new download thread' > 'add new download connector': \n{e}")

        try:
            if self.busy is False:
                # self.threadController['add new download'] = self.downloadThread(self.database, self)
                self.threadController['add new download'] = AddNewDownloadThread(self.database, self.myself)
                self.threadController['add new download'].start()
                self.threadController['add new download'].any_signal.connect(add_new_download_connector)
                self.myself.buttonMenu.click()
            else:
                QMessageBox.information(self.myself, "Please Wait","Please wait for current download data to be acquired or click cancel to abort. Then try again.")

        except Exception as e:
            print(f"An error occurred in 'add new download thread':\n{e}")

    def add_new_ok(self):
        myparent = self.myself

        def add_new_ok_thread_connector(data):
            try:
                # items = [0] # a list object to hold the data. extra data, the first data which is index in database
                # # requried when adding the list to the item window is added manually here. and set to 0
                # item = self.generalFunction.dict_to_list( data) # convert dictionaryto list
                # # add the list item to list object created above with initial data
                # for i in item:
                #     items.append(i)
                # # add the data to item window and visual dispaly
                # print(data)
                win = ItemWindow(data=data, my_parent=myparent)
                self.myself.scrollAreaWidgetContents.layout().addWidget(win)

                self.ready = True

                data = self.generalFunction.purify_raw_data_from_database_dict(data)
                self.database.insert_into_video_database(data)

            except Exception as e:
                print(f"An error occurred in Main Window > add new ok thread > add new ok thread connector: {e}")

        try:

            if self.raw_data is not None and self.isPlaylist is not None:
                if self.busy is False:
                    self.myself.show_download_page()
                    self.threadController['ok thread'] = AddNewOkThread(self.myself, self.raw_data, self.isPlaylist)
                    # self.threadController['add new download'] = AddNewDownloadThread(self.database, self)
                    self.threadController['ok thread'].start()
                    self.threadController['ok thread'].any_signal.connect(add_new_ok_thread_connector)
                else:
                    QMessageBox.information(self,"Please Wait!", 'Acquiring video data. Please wait for data to be fully acquired or click cancel to abort the process..')
            else:
                print(f'An Error occurred due to missing data [raw_data acquired or isPlaylist data missing]')
        except Exception as e:
            print(f"An error occurred in 'add new download thread':\n{e}")
