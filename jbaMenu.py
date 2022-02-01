import os
import signal
import time

from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsDropShadowEffect, QSizeGrip, QWidget, QMenu, QMessageBox
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve, QProcess, QEvent
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


class JbaMenuClass():

    def __init__(self, myparent=None):
        self.my_parent = myparent   # reference to the main window. instance of the main window

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
