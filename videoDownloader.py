import os
import signal
import time

from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsDropShadowEffect, QSizeGrip,QWidget, QMenu, \
    QMessageBox, QFileDialog
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
from jbavdLibrary import StyleSheet, VideoDatabase, GeneralFunctions, ActivityStopperThread
from userAction import UserActions
from jbaMenu import JbaMenuClass as jba_menu

restart_ready = False
restart = False
replaceDB = False
dbReplacementFile = None



class ItemWindow(QMainWindow, my_item_window_interface_.Ui_MainWindow):
    def __init__(self, data, my_parent, parent=None):
        super(ItemWindow, self).__init__(parent)
        self.setupUi(self)
        self.centralwidget.setStyleSheet(StyleSheet().central_widget)


class MainWindow(QMainWindow, my_interface_.Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        try:
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
            self.stopAllSuccessful = False
            self.dbResetActivated = False

            self.container = self.scrollAreaWidgetContents.layout()

            self.initialize()
            # self.generalFunctions.run_function(self.initialize)
        except Exception as e:
            print(f"An Error Occurred in Main Window Init()")

    def initialize(self):
        global restart
        restart = False
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
        print(f'total:::: {total_data}')
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

        self.generalFunctions.run_function(self.engineLoader.load_internet_checker_engine())
        #
        self.generalFunctions.run_function(self.engineLoader.load_statistics_getter_engine())
        # self.engineLoader.load_statistics_getter_engine()

        self.generalFunctions.run_function(self.engineLoader.load_downloader_engine())

    def add_new_download(self):
        if self.busy is False:
            self.busy = True
            self.userAction.add_new_download()
        else:
            QMessageBox.information(self, "Wait", "Please wait for data acquisition to be completed or Cancel")
            self.show_add_new_page()
        pass

    def filter(self):
        self.filter_all()

        def start():
            sender = self.sender()
            status = None

            if sender.objectName() == self.buttonWaiting.objectName():
                status = 'waiting'
            elif sender.objectName() == self.buttonInProgress.objectName():
                status = 'downloading'
            elif sender.objectName() == self.buttonCompleted.objectName():
                status = 'completed'
            elif sender.objectName() == self.buttonStopped.objectName():
                status = 'stopped'
            try:
                self.selected_filter = status
                # self.filter_all()
                if status is not None:
                    for x in range(self.scrollAreaWidgetContents.layout().count()):
                        item = self.scrollAreaWidgetContents.layout().itemAt(x).widget()
                        item_status = item.textStatus.text()
                        if item_status == status:
                            item.show()
                        else:
                            item.hide()

            except Exception as e:
                print(f"An error occurred in MainWindow > filter all: {e}")

        self.generalFunctions.run_function(start)

        pass

    def filter_all(self):
        try:
            # self.selected_filter = None
            for x in range(self.scrollAreaWidgetContents.layout().count()):
                item = self.scrollAreaWidgetContents.layout().itemAt(x).widget()
                # status = item.textStatus.text()
                item.show()
        except Exception as e:
            print(f"An error occurred in MainWindow > filter all: {e}")
        pass

    def browse_folder_location(self):
        try:
            print('browsing for folder location...')
            dl = QFileDialog.getExistingDirectory(self, "open location")
            if dl != "":
                self.textDefaultDownloadLocation.setText(dl)
        except Exception as e:
            print(f"An error occurred in 'COMMON'>'ADD NEW DOWNLOAD THREAD'>'browse folder location:\n{e}")
            return 'Error'
        pass

    def browse_file_location(self):
        try:
            dl,_ = QFileDialog.getOpenFileName(self, "Open", "open location")
            if dl != "":
                print(dl)
                return dl
            else:
                return None
        except Exception as e:
            print(f"An Error occurred in MainWindow > browse_file_location(): \n >>>{e}")

    def settings(self):
        self.show_settings_page()

    def settings_cancel(self):
        if self.busy is True:
            self.show_add_new_page()
        else:
            self.show_download_page()

    def settings_ok(self):
        try:
            self.database.update_setting('max_download', int(self.spinBox_MaxDownload.value()))
            self.database.update_setting('max_retries', int(self.spinBox_MaxRetries.value()))
            self.database.update_setting('default_download_location', self.textDefaultDownloadLocation.text())

            if self.busy is True:
                self.show_add_new_page()
            else:
                self.show_download_page()
        except Exception as e:
            print(f"An Error Occurred in MainWindow > settings_ok")
        pass

    def stop_all(self):
        def run():
            self.stopAllSuccessful = False
            try:
                for x in range(self.scrollAreaWidgetContents.layout().count()):
                    url = self.scrollAreaWidgetContents.layout().itemAt(x).widget().videoURL
                    # status = self.scrollAreaWidgetContents.layout().itemAt(x).widget().status
                    status = self.database.get_status(url)
                    if status == 'list index out of range':
                        break
                    title = self.scrollAreaWidgetContents.layout().itemAt(x).widget().title
                    if status != 'completed' and status != 'stopped':
                        self.database.set_status(url, 'stopped')
                        print(f"stopping '{title}'...")
                        self.message = f"stopping '{title}'..."

                    time.sleep(0.1)

                self.stopAllSuccessful = True
            except Exception as e:
                print(f"An error occurred in mainwindow > stop all > run: \n>>> {e}")

        try:
            self.generalFunctions.run_function(run)
        except Exception as e:
            print(f"An error occurred in mainwindow > stop all: \n>>> {e}")
            pass
        pass

    def delete_completed(self):
        def run():
            try:
                print('delinting..................')
                # self.buttonAll.click()
                self.filter_all()

                def delete_one():
                    for x in range(self.scrollAreaWidgetContents.layout().count()):
                        url = self.scrollAreaWidgetContents.layout().itemAt(x).widget().videoURL
                        status = self.database.get_status(url)
                        # status = self.scrollAreaWidgetContents.layout().itemAt(x).widget().status
                        if status == 'completed':
                            self.database.set_status(url, 'deleted')
                            self.scrollAreaWidgetContents.layout().itemAt(x).widget().deleteLater()
                            return True

                    return False

                while True:
                    if self.scrollAreaWidgetContents.layout().count() > 0:
                        print(f'total = {self.scrollAreaWidgetContents.layout().count()}')
                        ans = delete_one()
                        if ans is False:
                            print('not finally but nothing is remaining')
                            break
                    else:
                        print('finally')
                        break
                    time.sleep(0.2)

                print('deleting completed is now completed.')

            except Exception as e:
                print(f'An Error occurred in mainwindow > delete completed:  \n >>> {e}')

        self.generalFunctions.run_function(run)
        # run()

    def add_new_ok(self):
        if self.busy is False:
            self.userAction.add_new_ok()
        else:
            QMessageBox.information(self,"Wait","Please wait for data acquisition to be completed or Cancel")
            self.show_add_new_page()
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

    def restart_application(self):
        global restart
        restart = True
        self.close()

    def replace_database(self, new_database, old_database):

        try:
            self.stop_all_thread(new_database, old_database)
            # self.engineLoader.stop()

        except Exception as e:
            print(f'semi final error: {e}')

    def stop_all_thread(self, new_database, old_database):

        def connector(data):
            global replaceDB
            global dbReplacementFile
            if 'message' in data:
                self.message = data['message']
                self.labelInfo.setText(self.message)

            if 'completed' in data:
                self.hide()
                replaceDB = True
                dbReplacementFile = (new_database, old_database)

                QMessageBox.information(self, 'Restat',
                                        'Application will now restart to load the backup database. Please wait.')

                self.close()
            pass

        try:
            self.x = ActivityStopperThread(self)
            self.x.start()
            self.x.any_signal.connect(connector)

        except Exception as e:
            print(f'final error: {e}')

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
        try:
            # constantly communicate to the use
            self.labelInfo.setText(self.message)

            # getting and updating statistics
            self.is_there_waiting_download = self.statistics_data['is_waiting_download']
            self.is_max_download_exceeded = self.statistics_data['is_max_download_exceeded']
            self.max_download_allowed = self.statistics_data['max_download_allowed']
            self.max_retries = self.statistics_data['max_retries']
            self.default_download_location = self.statistics_data['default_download_location']
        except Exception as e:
            # print(f"An error occurred in mainwindow timer event: \n>>>{e}")
            pass

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
    global restart
    global replaceDB
    global dbReplacementFile

    if __name__ == '__main__':
        app = QApplication([])
        app.setStyle('fusion')

        win = MainWindow()
        win.show()

        app.exec_()
        if restart is True:
            time.sleep(1)
            start()

        if replaceDB is True:
            try:
                print(dbReplacementFile, "<><>[][]<><>[][]")
                new_database = dbReplacementFile[0]
                old = dbReplacementFile[1]
                while True:
                    print('removing old database.....')
                    time.sleep(0.2)
                    try:
                        if os.path.exists('jbacfg'):
                            os.remove('jbacfg')
                            break
                        else:
                            break
                    except Exception as e:
                        print(e)
                        continue
                time.sleep(1)
                shutil.copy(new_database, old)
                replaceDB = False
                time.sleep(1)
                start()
            except:
                start()
                pass


start()
