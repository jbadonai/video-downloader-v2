import os
import signal
import time

from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsDropShadowEffect, QSizeGrip, QWidget, QMenu, QMessageBox
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve, QProcess, QEvent
from PyQt5.QtGui import QColor, QIcon
import subprocess

# import common
from ui import my_interface_, my_item_window_interface_
import boot
import pyperclip as clipboard

from win10toast import ToastNotifier
import pyautogui
import psutil
import shutil
from datetime import datetime, date
import sys


class JbaMenuClass():

    def __init__(self, myparent=None):
        self.my_parent = myparent  # reference to the main window. instance of the main window
        self.selected_data = None

        # creation of menu item, icon and functions for context menu on the main window.
        self.main_menu_list = {

            'Backup Database': {'name': '',
                                'text': 'Backup Database',
                                'icon': ':/white icons/White icon/archive.svg',
                                'function_name': 'backup()'},

            'Restore Database': {'name': '',
                                 'text': 'Restore Database',
                                 'icon': ':/white icons/White icon/corner-left-down.svg',
                                 'function_name': 'restore_database()'},

            'separator1': {'name': '',
                           'text': 'separator',
                           'icon': '',
                           'function_name': ''},

            'Reset Database': {'name': '',
                               'text': 'Reset Database',
                               'icon': ':/white icons/White icon/refresh-ccw.svg',
                               'function_name': 'reset_database()'},

            'separator2': {'name': '',
                           'text': 'separator',
                           'icon': '',
                           'function_name': ''},

            'Multiple Select On/Off': {'name': '',
                                       'text': 'Multiple Select On/Off',
                                       'icon': ':/white icons/White icon/edit.svg',
                                       'function_name': 'select_multiple()'},

            'separator3': {'name': '',
                           'text': 'separator',
                           'icon': '',
                           'function_name': ''},

            'Select All Items': {'name': '',
                                 'text': 'Select All Items',
                                 'icon': ':/white icons/White icon/layers.svg',
                                 'function_name': 'select_all()'},

            'Deselect all Items': {'name': '',
                                   'text': 'Deselect all Items',
                                   'icon': ':/white icons/White icon/x-square.svg',
                                   'function_name': 'deselect_all()'},

            'separator4': {'name': '',
                           'text': 'separator',
                           'icon': '',
                           'function_name': ''},

            'Delete Selected Items': {'name': '',
                                      'text': 'Delete Selected Items',
                                      'icon': ':/white icons/White icon/trash.svg',
                                      'function_name': 'delete_selected()'},

            'separator5': {'name': '',
                           'text': 'separator',
                           'icon': '',
                           'function_name': ''},

            'Show/Hide Images': {'name': '',
                                 'text': 'Show/Hide Images',
                                 'icon': ':/white icons/White icon/eye-off.svg',
                                 'function_name': 'show_hide_image()'},

        }

    def get_menu(self):
        try:
            if self.my_parent is not None:
                if self.my_parent.database.get_status(self.my_parent.videoURL) == 'completed':
                    key = "Restart"
                    value = "{'name': '','text': 'Restart', 'icon': ':/white icons/White icon/play.svg','function_name': 'restart()'}"
                    selected_data = (key, value)
                    return selected_data
                else:
                    key = "Start"
                    value = "{'name': '','text': 'Start', 'icon': ':/white icons/White icon/play.svg','function_name': 'restart()'}"
                    selected_data = (key, value)
                    return selected_data
            else:
                key = "Start"
                value = "{'name': '','text': 'Start', 'icon': ':/white icons/White icon/play.svg','function_name': 'restart()'}"
                selected_data = (key, value)
                return selected_data
        except Exception as e:
            print(f"an error occurred in jbaMenuclass > get_menu(): \n>>>>{e}")

    def auto_menu(self):

        self.selected_data =  self.get_menu()

        item_menu_list = {

            'Copy URL': {'name': '',
                         'text': 'Copy URL',
                         'icon': ':/white icons/White icon/copy.svg',
                         'function_name': 'copy_url()'},

            'Copy playlist URL': {'name': '',
                                  'text': 'Copy playlist URL',
                                  'icon': ':/white icons/White icon/copy.svg',
                                  'function_name': 'copy_playlist_url()'},

            'separator1': {'name': '',
                           'text': 'separator',
                           'icon': '',
                           'function_name': ''},

            f'{self.selected_data[0]}': f'{self.selected_data[1]}' ,

            'Stop': {'name': '',
                     'text': 'Stop',
                     'icon': ':/white icons/White icon/stop-circle.svg',
                     'function_name': 'stop_download()'},

            'separator2': {'name': '',
                           'text': 'separator',
                           'icon': '',
                           'function_name': ''},

            'Open in Explorer': {'name': '',
                                 'text': 'Open in Explorer',
                                 'icon': ':/white icons/White icon/folder.svg',
                                 'function_name': 'open_in_explorer()'},

            'separator3': {'name': '',
                           'text': 'separator',
                           'icon': '',
                           'function_name': ''},

            'Delete': {'name': '',
                       'text': 'Delete',
                       'icon': ':/white icons/White icon/trash-2.svg',
                       'function_name': 'delete_selected()'}
        }

        return item_menu_list

    def backup(self):
        try:
            shutil.copy(os.path.join(os.getcwd(), "jbacfg"), os.path.join(os.getcwd(), f"backup\\jbacfg"))
            print('backed up succesfully')
            QMessageBox.information(self.my_parent, "Backup Successful!", "Database was backed up successfully.")

        except Exception as e:
            print(f"An Error Occurred in jbaMenu >JbaMenuClass>backup: \n>>{e}")

    def restore_database(self):
        print('restoring database....')

    def reset_database(self):
        print('reseting database...')

    def select_multiple(self):
        print('selecting multiple...')

    def select_all(self):
        print('selecting all....')

    def deselect_all(self):
        print('deselecting all...')

    def delete_selected(self):
        print("deleting selected items....")

    def show_hide_image(self):
        print('hiding or showing images...')

    # item window menu function starts here
    def copy_url(self):
        clipboard.copy(self.my_parent.videoURL)
        QMessageBox.information(self.my_parent, 'URL copied', 'ULR copied to the clipboard')

    def copy_playlist_url(self):
        clipboard.copy(self.my_parent.playlistURL)
        QMessageBox.information(self.my_parent, 'URL copied', 'Playlist ULR copied to the clipboard')
        # print('copying playlist url...')

    def restart(self):
        if self.my_parent.myself.is_there_waiting_download is False:
            downloading_number = self.my_parent.database.get_downloading_number()  # retrieve downloading number from the database
            max_download_allowed = int(self.my_parent.database.get_settings('max_download'))
            if downloading_number < max_download_allowed:
                self.my_parent.database.set_status(self.my_parent.videoURL, 'downloading')
            else:
                self.my_parent.database.set_status(self.my_parent.videoURL, 'waiting')
        else:
            self.my_parent.database.set_status(self.my_parent.videoURL, 'waiting')

    def stop_download(self):
        if self.my_parent.database.get_status(self.my_parent.videoURL) != 'completed':
            self.my_parent.database.set_status(self.my_parent.videoURL, 'stopped')

    def open_in_explorer(self):
        try:
            path = os.path.normpath(f"{self.my_parent.myself.default_download_location}\\")
            print(path)
            # os.popen(self.downloadLocation)
            # subprocess.Popen(f'explorer {self.downloadLocation}')
            subprocess.Popen(rf'explorer /select,"{path}\\"')
        except Exception as e:
            print(e)

    def delete_selected(self):
        try:
            index = self.my_parent.get_index()
            ans = QMessageBox.question(self.my_parent, "Delete?", f"Delete '{self.my_parent.title}'", QMessageBox.Yes | QMessageBox.No)
            if ans == QMessageBox.Yes:
                self.my_parent.database.set_status(self.my_parent.videoURL, "deleted")
                self.my_parent.delete_index(index)
                pass
        except Exception as e:
            print(f"An error occurred in jbaMenuClass > delete_selected: {e}")


