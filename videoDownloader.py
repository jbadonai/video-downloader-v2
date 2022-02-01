import os
import signal
import time

from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsDropShadowEffect, QSizeGrip,QWidget, QMenu, QMessageBox
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
from jbavdLibrary import StyleSheet, VideoDatabase, GeneralFunctions
from userAction import UserActions
from jbaMenu import JbaMenuClass as jba_menu

restart_ready = False



class ItemWindow(QMainWindow, my_item_window_interface_.Ui_MainWindow):
    def __init__(self, data, my_parent, parent=None):
        super(ItemWindow, self).__init__(parent)
        self.setupUi(self)
        self.centralwidget.setStyleSheet(StyleSheet().central_widget)


class MainWindow(QMainWindow, my_interface_.Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.bootLoader = boot

        self.threadController = {}  # Create thread controller holds all threads so they can be shutdown when requrired
        self.database = VideoDatabase()  # create a database object
        self.generalFunctions = GeneralFunctions()  # create general function object

        self.interfaceLoader = self.bootLoader.LoadInterface(self)  # code for loading interface executes here
        self.dataLoader = self.bootLoader.LoadDataFromDB(self)  # code for loading data from database executes here
        self.engineLoader = self.bootLoader.LoadEngines(self)   #   controls engine loading

        self.my_menu = jba_menu(self)   # create instance of menu content and it's functions.
        self.userAction = UserActions(self)

        #   initialize download monitoring variables
        self.totalNumber = 0
        self.numberCompleted = 0
        self.numberStopped = 0
        self.numberWaiting = 0
        self.numberDownloading = 0

        # settings that controls downloads
        self.max_download_allowed = 0
        self.is_max_download_exceeded = True
        self.max_retries = 0
        self.default_download_location = None
        self.is_there_waiting_download = False

        self.statistics_data = {}  # holds the statistics data that will be transmitted by load statistics getter engine

        self.message = "Info"
        self.timer = QBasicTimer()
        self.timer.start(200, self)

        self.is_internet = False

        self.busy = False
        self.isReady = False

        self.initialize()
        # self.generalFunctions.run_function(self.initialize)
        # self.scrollAreaWidgetContents.layout().addWidget()

    def initialize(self):
        #   1.  Initialize the database: check required tables and create them if not existing
        self.message = "Initializing database..."
        print("Initializing database...")
        self.database.initialize_database()     # SET UP THE DATABASE
        # time.sleep(0.2)

        #   2. check if there is data in the database
        self.message = "Checking content of the database..."
        print("Checking content of the database...")
        # time.sleep(0.2)
        total_data = self.database.get_total_number()    # get total no data in the database
        if total_data > 0:  # which implies there is data in the database
            #   3a. Load all data in the database
            self.message = "Loading Items from Database..."
            print("Loading Items from Database...")
            # time.sleep(0.2)
            self.dataLoader.start_loading()     # LOAD DATA FROM THE DATABASE
            # self.generalFunctions.run_function(self.dataLoader.start_loading)
        else:   # no data in the database
            self.message = "No data in the database yet. Click Add New from the menu to start downloading"
            print("No data in the database yet. Click Add New from the menu to start downloading")
            self.isReady = True

        #   4. load engines
        self.engineLoader.load_internet_checker_engine()    # load internet availability checker engine
        self.engineLoader.load_statistics_getter_engine()   # load statistics getter engine
        # load download monitoring engine [ not implemented yet ]
        self.engineLoader.load_downloader_engine()

    def add_new_download(self):
        if self.busy is False:
            self.busy = True
            self.userAction.add_new_download()
        else:
            QMessageBox.information(self, "Wait", "Please wait for data acquisition to be completed or Cancel")
        pass

    def filter(self):
        pass

    def filter_all(self):
        pass

    def settings(self):
        pass

    def browse_folder_location(self):
        pass

    def settings_cancel(self):
        pass

    def settings_ok(self):
        pass

    def stop_all(self):
        pass

    def delete_completed(self):
        pass

    def add_new_ok(self):
        if self.busy is False:
            self.userAction.add_new_ok()
        else:
            QMessageBox.information(self,"Wait","Please wait for data acquisition to be completed or Cancel")
        pass

    def scrollToBottom(self):
        # scrollBar = self.scrollArea_downloadItems.verticalScrollBar()
        self.scrollArea_downloadItems.verticalScrollBar().setValue(10000000)

    def show_add_new_page(self):
        self.stackedWidget.setCurrentWidget(self.page_add_new)

    def show_download_page(self):
        self.stackedWidget.setCurrentWidget(self.page_download)

    def show_settings_page(self):
        self.stackedWidget.setCurrentWidget(self.page_settings)
        # load and set settings from the database

        self.spinBox_MaxDownload.setValue(int(self.max_download_allowed))
        self.spinBox_MaxRetries.setValue(int(self.max_retries))
        self.textDefaultDownloadLocation.setText(self.default_download_location)

    def mousePressEvent(self, event):
        try:
            self.clickPosition = event.globalPos()
        except Exception as e:
            print(f"An Error occurred in MainWindow > mousePressEvent(): \n >>>{e}")

    def eventFilter(self, source, event):
        try:
            if event.type() == QEvent.MouseButtonDblClick and source == self.frame_title:
                try:
                    if self.isMaximized():
                        self.showNormal()
                        self.button_restore.setIcon(QIcon(":/white icons/White icon/maximize-2.svg"))
                    else:
                        self.showMaximized()
                        self.button_restore.setIcon(QIcon(":/white icons/White icon/minimize-2.svg"))
                except Exception as e:
                    print(f"An Error occurred in MainWindow > eventFilter : \n >>>{e}")

        except Exception as e:
            print(f"An Error Occurred in ItemWindow > eventFilter : \n{e}")

        return QWidget.eventFilter(self, source, event)
        # return QtGui.QWidget.eventFilter(self, source, event)

    def contextMenuEvent(self, event):
        try:
            menu = QMenu(self)  # create an instance of the menu
            menu.setStyleSheet(StyleSheet().menu_style)     # apply custom sytle to the menu
            menu_list = self.my_menu.main_menu_list    # get the content of the menu

            # loop through the menu item list to apply icon and display them.
            for m in menu_list:
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
            pass

        except Exception as e:
            print(f"An Error Occurred in MainWindow > contextMenuEvent: \n >>> {e}")

    def timerEvent(self, a0):
        # constantly communicate to the use
        self.labelInfo.setText(self.message)

        # getting and updating statistics
        self.is_there_waiting_download = self.statistics_data['is_waiting_download']
        self.is_max_download_exceeded = self.statistics_data['is_max_download_exceeded']
        self.max_download_allowed = self.statistics_data['max_download_allowed']
        self.max_retries = self.statistics_data['max_retries']
        self.default_download_location = self.statistics_data['default_download_location']

    def closeEvent(self, e):
        try:
            self.hide()
            for root, dirs, files in os.walk('temp'):
                for file in files:
                    try:
                        os.remove(os.path.join(root, file))
                        print(f"removing {file}...")
                    except:
                        continue
            print('finally clossing....................')
        except Exception as e:
            print(f"An Error occurred in MainWindow > closeEvent(): \n >>>{e}")


def start():
    if __name__ == '__main__':
        app = QApplication([])
        app.setStyle('fusion')

        win = MainWindow()
        win.show()

        app.exec_()


start()
