from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsDropShadowEffect, QSizeGrip, QVBoxLayout
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve, QProcess
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
from jbavdLibrary import StyleSheet, LoadDataFromDatabaseThread, IsInternetThread, GetStatisticsThread
from itemWindow import ItemWindow


class LoadInterface():
    def __init__(self, myself):
        # myself is an instance of self from main window which was passed to this class.
        self.myself = myself    # for reusability purpose outside init create a variable for myself

        self.myself.setupUi(self.myself)  # set up the ui
        self.myself.setWindowFlag(Qt.FramelessWindowHint)  # remove windows title bar
        self.myself.setAttribute(Qt.WA_TranslucentBackground)
        self.myself.show()

        size = pyautogui.size()  # get screen resolution
        height = int(size.height * 70 / 100)  # set windows height to 70% of the the screen height
        width = int(size.width * 70 / 100)  # set window width to 70% of the screen width
        top = int(size.height / 2) - height / 2  # centralize the top
        left = int(size.width / 2) - width / 2  # centralize the width
        self.myself.setGeometry(left, top, width, height)  # set windows geometry.

        # create a shadow effect in memory and store it in shadow variable
        self.myself.shadow = QGraphicsDropShadowEffect(self.myself)
        self.myself.shadow.setBlurRadius(50)
        self.myself.shadow.setXOffset(0)
        self.myself.shadow.setYOffset(0)
        self.myself.shadow.setColor(QColor(255, 255, 255, 50))

        # apply the shadow to above to central widget and frame title
        self.myself.centralwidget.setGraphicsEffect(self.myself.shadow)
        self.myself.frame_title.setGraphicsEffect(self.myself.shadow)

        # set window icon
        self.myself.setWindowIcon(QIcon(":/blue icons/blue icon/arrow-down-circle.svg"))

        QSizeGrip(self.myself.resize_grip)  # Window size grip
        self.myself.button_minimize.clicked.connect(lambda: self.myself.showMinimized())  # minimize window
        self.myself.button_close.clicked.connect(lambda: self.myself.close())  # close window
        self.myself.button_restore.clicked.connect(self.restore_or_maximize_window)  # restore window

        def moveWindow(e):
            if not self.myself.isMaximized():
                if e.buttons() == Qt.LeftButton:
                    # move window
                    self.myself.move(self.myself.pos() + e.globalPos() - self.myself.clickPosition)
                    self.myself.clickPosition = e.globalPos()
                    e.accept()

        self.myself.frame_title.mouseMoveEvent = moveWindow

        self.myself.buttonMenu.clicked.connect(lambda: self.slideLeftMenu())

        # define layouts
        # creating layout and setting aligment for the item list window
        self.videoFormatLayout = QVBoxLayout()
        self.videoFormatLayout.setAlignment(Qt.AlignTop)
        self.itemLayout = QVBoxLayout()
        self.itemLayout.setAlignment(Qt.AlignTop)

        # apply the 2 layout created above to widget of vidoe format list and item window lists
        self.myself.scrollAreaWidgetContents_VideoFormat.setLayout(self.videoFormatLayout)
        self.myself.scrollAreaWidgetContents.setLayout(self.itemLayout)

        # apply style sheet to the main window
        self.myself.setStyleSheet(StyleSheet().main_window_style)

        # self.functions.run_function(self.initialize)
        try:
            self.myself.frame_title.installEventFilter(self.myself)
            pass
        except Exception as e:
            print(e)

        self.myself.buttonErrorDetected.setVisible(False)


        # connect buttons to functions
        self.myself.buttonAddNew.clicked.connect(lambda: self.myself.add_new_download())
        self.myself.buttonInProgress.clicked.connect(lambda : self.myself.filter())
        self.myself.buttonCompleted.clicked.connect(lambda: self.myself.filter())
        self.myself.buttonWaiting.clicked.connect(lambda: self.myself.filter())
        self.myself.buttonStopped.clicked.connect(lambda: self.myself.filter())
        self.myself.buttonAll.clicked.connect(lambda: self.myself.filter_all())
        self.myself.button_settings.clicked.connect(lambda: self.myself.settings())
        self.myself.buttonBrowseDefaultDownloadLocation.clicked.connect(lambda: self.myself.browse_folder_location())
        self.myself.buttonSettingsCancel.clicked.connect(lambda: self.myself.settings_cancel())
        self.myself.buttonSettingsOK.clicked.connect(lambda: self.myself.settings_ok())

        self.myself.buttonStopAll.clicked.connect(lambda: self.myself.stop_all())
        self.myself.buttonDeleteCompleted.clicked.connect(lambda: self.myself.delete_completed())

        self.myself.buttonAddNewOK.clicked.connect(self.myself.add_new_ok)

        self.show_download_page()

        # this is just a trick to enable resize grip
        self.myself.showMaximized()
        self.myself.showNormal()

    def restore_or_maximize_window(self):
        try:
            if self.myself.isMaximized():
                self.myself.showNormal()
                self.myself.button_restore.setIcon(QIcon(":/white icons/White icon/maximize-2.svg"))
            else:
                self.myself.showMaximized()
                self.myself.button_restore.setIcon(QIcon(":/white icons/White icon/minimize-2.svg"))
        except Exception as e:
            print(f"An Error occurred in boot > LoadInterface > restore_or_maximize_window(): \n >>>{e}")

    def slideLeftMenu(self):
        try:
            width = self.myself.left_frame.width()
            if width == 0:
                newWidth = 300
                self.myself.buttonMenu.setIcon(QIcon(":/white icons/White icon/chevrons-left.svg"))
            else:
                newWidth = 0
                self.myself.buttonMenu.setIcon(QIcon(":/white icons/White icon/menu.svg"))

            # animate the transition
            try:
                self.myself.animation = QPropertyAnimation(self.myself.left_frame, b"minimumWidth")  # Animate minimumWidth
                self.myself.animation.setDuration(100)
                self.myself.animation.setStartValue(width)
                self.myself.animation.setEndValue(newWidth)
                self.myself.animation.setEasingCurve(QEasingCurve.InOutQuart)
                self.myself.animation.start()
            except Exception as e:
                print(f"An Error occurred in boot > LoadInterface():>slideLeftMenu():> animation \n >>>{e}")
        except Exception as e:
            print(f"An Error occurred in boot > LoadInterface()> slideLeftMenu(): \n >>>{e}")

    def show_download_page(self):
        self.myself.stackedWidget.setCurrentWidget(self.myself.page_download)


class LoadDataFromDB():
    def __init__(self, myself):
        self.my_self = myself

        self.database = myself.database
        self.threadController = myself.threadController
        self.functions = myself.generalFunctions

    def start_loading(self):
        print("loading commenced....")
        self.my_self.message = "loading commenced...."
        self.total = self.database.get_total_number()
        self.counter = 1

        def loading_connector(data):
            # print(data)
            try:
                if 'data_loading_completed' not in data:
                    try:
                        p = ((self.counter/self.total)*100).__round__()
                    except:
                        p = 100
                        pass
                    self.my_self.message = f"[{p}%] - Loading {data['title']}"
                    self.counter += 1
                    win = ItemWindow(data, self.my_self)
                    self.my_self.scrollAreaWidgetContents.layout().addWidget(win)

                    # win.initialize()
                else:

                    print('data loading completed')
                    self.my_self.message = "Data loading Completed successfully"
            except Exception as e:
                print(f"An Error occurred in boot > LoadDataFromDB  > loading_connector:>>>\n{e}")

        try:
            items = self.database.get_all_video_data()
            self.threadController['load data from db'] = LoadDataFromDatabaseThread(items)
            self.threadController['load data from db'].start()
            self.threadController['load data from db'].any_signal.connect(loading_connector)
        except Exception as e:
            print(f"An Error occurred in boot > LoadDataFromDB :>>>\n{e}")

    def load_images(self):
        pass


class LoadEngines():
    def __init__(self, myself):
        self.my_self = myself
        self.database = myself.database
        self.threadController = myself.threadController
        self.flipper = False

    def load_internet_checker_engine(self):
        self.flipper = True
        backupStyle_button = self.my_self.buttonInternetConnection.styleSheet()
        backupStyle_label = self.my_self.label_12.styleSheet()
        onSytle = "background-color: red; color: white;"
        offStyle = "background-color: white; color: red;"

        def internet_checker_connector(data):
            try:
                # print(data)
                self.my_self.is_internet = data['is_internet']

                # internet connection monitoring
                if data['is_internet'] is False:
                    self.my_self.label_12.setText("Internet Connection Issue")
                    if self.flipper is False:
                        # self.my_self.buttonInternetConnection.setVisible(False)
                        self.my_self.buttonInternetConnection.setStyleSheet(onSytle)
                        self.my_self.label_12.setStyleSheet(onSytle)
                        self.flipper = True
                    else:
                        # self.my_self.buttonInternetConnection.setVisible(True)
                        self.my_self.buttonInternetConnection.setStyleSheet(offStyle)
                        self.my_self.label_12.setStyleSheet(offStyle)
                        self.flipper = False
                else:
                    self.my_self.label_12.setText("Internet Connection Ok")
                    self.my_self.buttonInternetConnection.setVisible(True)
                    self.my_self.buttonInternetConnection.setStyleSheet(backupStyle_button)
                    self.my_self.label_12.setStyleSheet(backupStyle_label)
            except Exception as e:
                print(f"An Error occurred in boot > LoadEngines > load internet checker engine > internet checker connector:>>>\n{e}")

        try:
            self.threadController['internet checker'] = IsInternetThread()
            self.threadController['internet checker'].start()
            self.threadController['internet checker'].any_signal.connect(internet_checker_connector)
        except Exception as e:
            print(f"An Error occurred in boot > LoadEngines > load internet checker engine :>>>\n{e}")

    def load_statistics_getter_engine(self):

        def get_statistics_connector(data):
            try:
                # print(data)
                self.my_self.statistics_data = data
                self.my_self.textAll.setText(str(data['total_number']))
                self.my_self.textCompleted.setText(str(data['completed_number']))
                self.my_self.textInProgress.setText(str(data['downloading_number']))
                self.my_self.textWaiting.setText(str(data['waiting_number']))
                self.my_self.textStopped.setText(str(data['stopped_number']))
            except Exception as e:
                print(f"An Error occurred in boot > LoadEngines > statistics getter engine > get statistics connector :>>>\n{e}")

        try:
            self.threadController['get statistics'] = GetStatisticsThread()
            self.threadController['get statistics'].start()
            self.threadController['get statistics'].any_signal.connect(get_statistics_connector)
        except Exception as e:
            print(f"An Error occurred in boot > LoadEngines > statistics getter engine :>>>\n{e}")

    def load_downloader_engine(self):
        my_self = self.my_self

        def downloader_engine_connector(data):
            # print(data)
            # self.database.set_status()
            pass

        try:
            self.threadController['download_engine'] = DownloaderEngineThread(my_self)
            self.threadController['download_engine'].start()
            self.threadController['download_engine'].any_signal.connect(downloader_engine_connector)
        except Exception as e:
            print(f"An error occurred in MainWindow > download_engine_thread. : \n {e}")

        # 1. check if there is a waiting downnload

        # 2. check if maximum allowed download has not been exceeded

        # 3. pick the next waiting download

        # 4. start the download for the next waiting download

        # 5. go to the begining again to check if there is still waiting download.
        pass


