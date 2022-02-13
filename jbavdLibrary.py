import sqlite3
import os
import signal
import yt_dlp as youtube_dl
import re
import math
import subprocess
import threading
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QIcon
import time
import pyperclip

addDownloadEmergencyStop = False

# import stylesheet
from ui import  my_item_window_interface
import requests
import random
import pyperclip as clipboard
# from videoDownloader import Splash


class StyleSheet():
    def __init__(self):
        super(StyleSheet, self).__init__()

        # for item window styling
        self.central_widget = """
    
        QFrame{
    
        border: none;
        }
    
        #centralwidget:hover{
    
        }
        QMenu:hover{
        color:yellow;
        }
    
        QLabel{
        color: rgb(0, 255, 127);
        }
    
        #frame_select QCheckBox{
        background-color: yellow;
        color: black;
        }
    
    
    
        #frame_main{
        margin:1px;
        padding-top:5px;
        padding-left:5px;
        padding-right:5px;
        /*
        border-top: 5px solid qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));
        */
        border-bottom: 5px solid qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));
    
        border-left: 10px solid qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));
        }
    
        #frame_main QFrame{
        background-color: transparent;
        }
    
        #frame_main:hover {
        background-color: rgb(15,15,15);
        border-top: 5px solid qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), stop:0.52 rgba(0, 0, 0, 0), stop:0.565 rgba(82, 121, 76, 33), stop:0.65 rgba(159, 235, 148, 64), stop:0.721925 rgba(255, 238, 150, 129), stop:0.77 rgba(255, 128, 128, 204), stop:0.89 rgba(191, 128, 255, 64), stop:1 rgba(0, 0, 0, 0));;
        border-bottom: 5px solid qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), stop:0.52 rgba(0, 0, 0, 0), stop:0.565 rgba(82, 121, 76, 33), stop:0.65 rgba(159, 235, 148, 64), stop:0.721925 rgba(255, 238, 150, 129), stop:0.77 rgba(255, 128, 128, 204), stop:0.89 rgba(191, 128, 255, 64), stop:1 rgba(0, 0, 0, 0));;
        border-left: 5px solid qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), stop:0.52 rgba(0, 0, 0, 0), stop:0.565 rgba(82, 121, 76, 33), stop:0.65 rgba(159, 235, 148, 64), stop:0.721925 rgba(255, 238, 150, 129), stop:0.77 rgba(255, 128, 128, 204), stop:0.89 rgba(191, 128, 255, 64), stop:1 rgba(0, 0, 0, 0));;
        border-right: 5px solid qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), stop:0.52 rgba(0, 0, 0, 0), stop:0.565 rgba(82, 121, 76, 33), stop:0.65 rgba(159, 235, 148, 64), stop:0.721925 rgba(255, 238, 150, 129), stop:0.77 rgba(255, 128, 128, 204), stop:0.89 rgba(191, 128, 255, 64), stop:1 rgba(0, 0, 0, 0));;
        border-radius: 10px;
        padding-bottom: 5px;
        }
    
    
        #frame_top{
    
        }
    
        #textTitle{
        margin-left:30%;
        font:9pt;
        font-weight: bold;
        color:white;
        }
    
        #textTitle:hover{
        margin-left:30%;
        font:14pt;
        font-weight: normal;
        font-style: italic;
        color:yellow;
        }
    
        #frame_status{
    
        }
    
        #textStatus{
        font:10pt;
        }
    
        #frame_progress_bar{
        margin-left:20%;
        margin-right:20%;
        margin-bottom:5px;
        }
    
        #frame_statistics{
            margin-right:30%;
            margin-left:30%;
            margin-bottom:5px;   
            border-radius:7px;
            background:rgb(10, 10, 10);
        }
    
        #textSize, #textDownloaded, #textSpeed, #textETA{
            color:yellow;
            background-color:rgb(30,30,30);
            border:2px solid;
            border-radius:5px;
            margin-right:15px;
            font:8pt;
            font-style: italic;
        }
    
        #labelSize,#labelDownloaded,#labelSpeed, #labelETA{
            background-color:rgb(30,30,30);
            font:8pt;
            font-weight:bold;
        }
    
    
    
        #frame_image{
            margin-right:5px;  
            margin-bottom:5px;
        }
    
    
        #frame_image:hover{
            width:200px;
            height: 200px;
        }
    
    
    
        #frame_image QLabel{
        font:7pt;
        border-radius:40px;
        background: rgb(121, 121, 121);
        color: white;
        }
    
        #MainWindow{
        color: rgb(0, 255, 127);
        background-color: rgb(60, 60, 60);
        }
    
        """

        # for Qmenu styling
        self.menu_style = """
    
        QMenu{
        color: rgb(0, 255, 127);
        background-color: rgb(10, 10, 10);
        border-left: 2px solid qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));
        border-right: 2px solid qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));
        border-top: 2px solid qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));
        border-bottom: 2px solid qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));
        margin-left:2px;
        padding-left:10px;
        font:9pt;
    
        }
    
    
        QMenu::item::selected{
        color: white;
        background-color: blue;
        font:9pt;
        /*font-style: italic;*/
        padding-left:13px;
        }
    
        QMenu::separator{
        background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));
    
        }
    
    
        """

        # for main window styling
        self.main_window_style = """
    
        QFrame{
            border:none;
        }

        #centralwidget QLabel{
            color: rgb(0, 255, 127);
        }
        
        #left_frame{
        background-color: rgb(50, 50, 50);
        padding:10px;
        border-left:3px solid rgb(255, 255, 127);
        border-right:3px solid rgb(255, 255, 127);
        border-top:3px solid rgb(255, 255, 127);
        border-bottom:3px solid rgb(255, 255, 127);
        border-radius:70px;
        margin-top: 30%;
        margin-bottom: 30%;
        }
    
        #frame_filter QPushButton,#frame_action QPushButton, #buttonAddNew{
        border: 2px solid  rgb(255,255, 255);
        border-radius:14px;
        height:30px;
        margin: 3px;
        padding:3px;
        background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.55 rgba(86, 54, 22, 255), stop:1 rgba(0, 0, 0, 255));
        font: 12pt "MS Shell Dlg";
        color:rgb(255, 255, 255);
        cursor:"Pointing Hand";
        }
        
        #frame_settings_title, #frame_new_download_title{
         border-left: 3px solid white;
        border-bottom: 3px solid white;
        border-right: 3px solid white;
        border-radius:15px;
        margin-top:-10px;
        margin-bottom:20px;
        padding-top:10px;
        padding-left:40px;
        padding-right:40px;
        padding-bottom:10px;
        background-color: rgb(55,55,55);
              
        }
        
        /*
        #frame_settings_title, #frame_new_download_title{
        padding:5px;
        margin-bottom:15px;
        margin-top:5px;
        margin-right:15px;
        border-bottom: 3px solid rgb(255, 255, 255);
        border-top: 3px solid rgb(255, 255, 255);
        background:transparent;
        border-radius:10px;        
        }
        */
    
        #frame_leftTop{
        background-color: rgb(30, 30, 30);
        margin-top:25px;
        border: 1px solid white;
        border-radius:20px;
        margin-left: 5px;
        margin-right:5px;
        width: Auto;
        }
        #frame_leftTop:hover{
        border: 3px solid  blue;
        }
    
        #frame_filter QPushButton:hover,#frame_action QPushButton:hover, #buttonAddNew:hover{
        border: 3px solid  blue;
        border-radius:14px;
        height:30px;
        margin: 3px;
        padding:3px;
        background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.55 rgba(86, 54, 22, 255), stop:1 rgba(0, 0, 0, 255));
        font: 12pt "MS Shell Dlg";
        color:blue;
        cursor:"Pointing Hand";
        }
    
    
        #header_frame{
        background-color: rgb(20, 20, 20);
        padding:5px;
        border-bottom:5px solid qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));
    
        }
    
    
        #frame_11 QPushButton{
        border-radius: 14px;
        border:2px solid rgb(255, 255, 127);
        margin:3px;
        padding:1px;
        }
    
        #frame_11 QPushButton:hover{
        border-radius: 12px;
        border:2px solid rgb(60, 60, 60);
        margin:3px;
        padding:1px;
        background-color: blue;
    
        }
        
                
        #frame_message_container{        
        border-bottom:5px solid qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));
        border-top:5px solid qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));
        padding: 5px;
        }
        
        #frame_message_container QLabel{     
        background-color: black;
        color: yellow;
        font: 10pt;
        padding: 3px;
        }  
      
        #frame_indicator{       
        border-bottom:5px solid qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));
        }
        
        #frame_indicator QFrame{   
       margin-left:10px;
       }
        
       #frame_indicator QFrame QLabel{   
       margin-left:5px;
       color:gray;
       }
       
       #frame_error QPushButton{
       color: orange;
       }
        """


class GeneralFunctions():
    def __init__(self):
        super(GeneralFunctions, self).__init__()

    def dict_to_list(self, dictionary):
        '''
        converts dictionary to list
        :param dictionary:
        :return:
        '''

        try:
            new_list = []
            for item in dictionary:
                new_list.append(dictionary[item])

            return new_list
        except Exception as e:
            print(f"An error occurred in common> general functions > dict to list")

    def database_list_to_dictionary(self, dbList):
        d = {}
        d['download_video']= dbList[1]
        d['download_all']= dbList[2]
        d['format']= dbList[3]
        d['url']= dbList[4]
        d['title']=self.screen_title(dbList[5])
        d['is_playlist']= dbList[6]
        d['playlist_index']= dbList[7]
        d['playlist_title']= dbList[8]
        d['playlist_url']= dbList[9]
        d['thumbnail']= dbList[10]
        d['status']= dbList[11]
        d['download_location']= dbList[12]

        return d

    def screen_title(self, title):
        """
        This function removes illegal characters from text passed into it.
        it was intended to remove illegal characters from video title which can cause error while saving
        """

        final = ""  # holds the final result
        for c in title:  # loop through every character in the text supplied
            # check if current character is accepted
            if c.isalnum() or c.isalpha() or c.isspace() or c.isnumeric() or c.isdigit() or c.isidentifier():
                final = final + c  # add the accepted character to the final result

        print('[][]][][][][][][][][][][][][][][][]][')
        print(f'original title = : {title}')
        print(f'Screened title = : {final}')
        print('[][]][][][][][][][][][][][][][][][]][')
        return final  # return the final result

    def purify_raw_data_from_database_dict(self, d: dict):
        """
        This makes sure that all data types are correct by converting expected data to their data types.
        expected data from dictionary

        takes in dictionary as the argument and return a dictionary
        """
        try:
            download_video = bool(d['download_video'])
            download_all = bool(d['download_all'])
            video_format = d['format']
            url = d['url']
            title = self.screen_title(d['title'])
            is_playlist = bool(d['is_playlist'])
            playlist_index = d['playlist_index']
            playlist_title = d['playlist_title']
            playlist_url = d['playlist_url']
            thumbnail = d['thumbnail']
            status = d['status']
            download_location = d['download_location']

            my_data = {'download_video': download_video,
                       'download_all': download_all,
                       'format': video_format,
                       'title': title,
                       'url': url,
                       'is_playlist': is_playlist,
                       'playlist_index': playlist_index,
                       'playlist_title': playlist_title,
                       'playlist_url': playlist_url,
                       'thumbnail': thumbnail,
                       'status': status,
                       'download_location': download_location
                       }
            return my_data
        except Exception as e:
            print(f"An error occurred in  PURIFY RAW DATA FROM DATABASE : {e}")

    def purify_raw_data_from_database_list(self, d):
        """
        This makes sure that all data types are correct by converting expected data to their data types
        expected data list from database directly.
        """
        try:
            download_video = bool(d[1])
            download_all = bool(d[2])
            video_format = d[3]
            url = d[4]
            title = self.screen_title(d[5])
            is_playlist = bool(d[6])
            playlist_index = d[7]
            playlist_title = d[8]
            playlist_url = d[9]
            thumbnail = d[10]
            status = d[11]
            download_location = d[12]

            my_data = {'download_video': download_video,
                       'download_all': download_all,
                       'format': video_format,
                       'title': title,
                       'url': url,
                       'is_playlist': is_playlist,
                       'playlist_index': playlist_index,
                       'playlist_title': playlist_title,
                       'playlist_url': playlist_url,
                       'thumbnail': thumbnail,
                       'status': status,
                       'download_location': download_location
                       }
            return my_data
        except Exception as e:
            print(f"An error occurred in  PURIFY RAW DATA FROM DATABASE : {e}")

    def convert_size(self, size_bytes):
        ''' This function converts size in bytes to respective value in KB, MB, GB...'''
        if size_bytes == 0:
            return "0B"
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return "%s %s" % (s, size_name[i])

    def IsInternet(self):
        try:
            ''' This function checks for internet availability'''
            result = subprocess.getoutput("ping www.google.com -n 1")

            if result.lower().__contains__('timed out'):
                return False
            elif result.lower().__contains__('general failure'):
                return False
            elif result.lower().__contains__('could not find host'):
                return False
            elif result.__contains__('TTL='):
                return True
            else:
                return False
        except Exception as e:
            return f"An error occurred: [{e}][{result}]"

    def is_url_valid(self, url):
        pattern = "^(?:http(s)?://)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$"
        if re.search(pattern, url):
            if str(url).lower().__contains__('www') or str(url).lower().__contains__('http'):
                return True
        else:
            return False

    def run_function(self, functionName, join: bool = False, *args):
        t = threading.Thread(target=functionName, args=args)
        t.daemon = True
        t.start()
        if join:
            t.join()

    def extract_playlist_video_download_data_list(self, rawdata):
        download_data_list = []

        for d in rawdata['entries']:
            try:
                title = d['title']
                url = d['webpage_url']
                playlist_index = d['playlist_index']
                playlist_title = d['playlist_title']
                thumbnail = d['thumbnail']
                isPlaylist = True
                data = (title, url, isPlaylist, playlist_index, playlist_title, thumbnail)
                # print(f"DATA >>>>> {data}")
                download_data_list.append(data)
            except Exception as e:
                print(f'an error occurred in extract playlist video download: {e}')
                # print(title, '>', url)
                # print(download_data_list)
                # input("have you seen the error above")
                # time.sleep(0.5)
                continue

        # print(download_data_list)
        return download_data_list

    def extract_single_video_download_data_list(self, rawdata):
        download_data_list = []
        d = rawdata
        title = d['title']
        url = d['webpage_url']
        playlist_index = None
        playlist_title = None
        thumbnail = d['thumbnail']
        isPlaylist = False

        data = (title, url, isPlaylist, playlist_index, playlist_title, thumbnail)
        download_data_list.append(data)

        return download_data_list

    def convert_size(self, size_bytes):
        ''' This function converts size in bytes to respective value in KB, MB, GB...'''
        if size_bytes == 0:
            return "0B"
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return "%s %s" % (s, size_name[i])


class VideoDatabase():
    def __init__(self):
        super(VideoDatabase, self).__init__()
        self.dbname = 'jbacfg'

    def set_db_filename(self, filename):
        self.dbname = filename

    def create_video_database(self):
        ''' create video table in the database '''
        try:
            print('createing video data database...')
            connection = sqlite3.connect(self.dbname)
            cursor = connection.cursor()
            command = '''
            CREATE TABLE IF NOT EXISTS VideoData
            (
            id integer primary key AUTOINCREMENT,
            download_video BOOL,
            download_all BOOL,
            format TEXT,
            url TEXT,
            title TEXT,
            is_playlist BOOL,
            playlist_index TEXT NULL,
            playlist_title TEXT NULL,
            playlist_url TEXT NULL,
            thumbnail TEXT,
            status TEXT,
            download_location TEXT        
            )
            '''
            cursor.execute(command)
            connection.commit()
            connection.close()
        except Exception as e:
            print(f"An error occurred in database module ': {e}")

    def create_settings_database(self):
        ''' creates settings table in the database '''
        try:
            print("Creating settings database...")
            connection = sqlite3.connect(self.dbname)
            cursor = connection.cursor()
            command = '''
            CREATE TABLE IF NOT EXISTS Settings
            (
            id integer primary key AUTOINCREMENT,
            key TEXT,
            value TEXT      
            )
            '''
            cursor.execute(command)
            connection.commit()
            connection.close()
        except Exception as e:
            print(f"An error occurred in database module 'CREATE SETTINGS DATABASE' : {e}")

    def insert_into_video_database(self, data):
        ''' save input data into the video database '''

        downloadVideo = data['download_video']
        downloadAll = data['download_all']
        format = data['format']
        url = data['url']
        title = data['title']
        isPlaylist = data['is_playlist']
        playlistIndex = data['playlist_index']
        playlistTitle = data['playlist_title']
        playlistURL = data['playlist_url']
        thumbnail = data['thumbnail']
        status = data['status']
        downloadLocation = data['download_location']

        try:
            connection = sqlite3.connect(self.dbname)
            cursor = connection.cursor()

            cursor.execute('INSERT INTO VideoData '
                           '(download_video, download_all, format, url, title, is_playlist, playlist_index, playlist_title, playlist_url, thumbnail, status, download_location) '
                           'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                           (downloadVideo, downloadAll, format, url, title, isPlaylist, playlistIndex, playlistTitle,
                            playlistURL, thumbnail, status, downloadLocation))
            connection.commit()

        except Exception as e:
            print(f"An error occurred in database module 'INSERT INTO VIDEO DATABASE' : {e}")

    def setup_create_settings(self, key, value):
        ''' set up required columns in the settings table '''
        try:
            connection = sqlite3.connect(self.dbname)
            cursor = connection.cursor()
            cursor.execute("insert into Settings (key, value) values (?, ?)", (key, value))
            connection.commit()
            connection.close()
        except Exception as e:
            print(f"An error occurred in database module 'SETUP CREATE SETTINGS': {e}")

    def update_setting(self, key, value):
        ''' update the value of a setting using the key'''
        try:

            connection = sqlite3.connect(self.dbname)
            cursor = connection.cursor()
            cursor.execute("update Settings set value = ? where key = ?", (value, key))
            connection.commit()
            connection.close()
        except Exception as e:
            print(f"An error occurred in database module 'UPDATE SETTING': {e}")

    def get_settings(self, key):
        ''' Reterieve a particular settings from the database using the key '''
        try:
            connection = sqlite3.connect(self.dbname)
            cursor = connection.cursor()
            cursor.execute("select value from Settings where key = ?", (key,))
            ans = cursor.fetchall()
            return ans[0][0]
        except Exception as e:
            print(f"An error occurred in the database module 'GET SETTING' [{key}]:{e}")

    def is_setting_key_in_database(self, key):
        ''' check if a particular key exist in the settings table'''
        try:
            connection = sqlite3.connect(self.dbname)
            cursor = connection.cursor()
            cursor.execute("select value from Settings where key = ?", (key,))
            ans = cursor.fetchall()
            if len(ans) == 0:
                return False
            else:
                return True

        except Exception as e:
            print(f"An error occurred in database moodule 'IS SETTING KEY IN DATABASE' : {e}")

    def get_all_video_data(self):
        ''' get all the video data in the database '''
        try:
            connection = sqlite3.connect(self.dbname)
            cursor = connection.cursor()

            cursor.execute('select * from VideoData')
            data = cursor.fetchall()
            return data
        except Exception as e:
            print(f"An error occurred in database module ' GET ALL VIDEO DATA' : [e")

    def get_waiting_number(self):
        ''' get all data in database with status of waiting '''
        try:
            connection = sqlite3.connect(self.dbname)
            cursor = connection.cursor()

            cursor.execute('select * from VideoData where status = "waiting"')
            data = cursor.fetchall()
            return len(data)
        except Exception as e:
            print(f"An error occurred in database module 'GET WAITING NUMBER': {e}")

    def get_completed_number(self):
        '''get all data in database with status of completed'''
        try:
            connection = sqlite3.connect(self.dbname)
            cursor = connection.cursor()

            cursor.execute('select * from VideoData where status = "completed"')
            data = cursor.fetchall()
            return len(data)
        except Exception as e:
            print(f"An error occurred in database module 'GET COMPLETED NUMBER': {e}")

    def get_stopped_number(self):
        ''' get all data in database with status of stopped'''
        try:
            connection = sqlite3.connect(self.dbname)
            cursor = connection.cursor()

            cursor.execute('select * from VideoData where status = "stopped"')
            data = cursor.fetchall()
            return len(data)
        except Exception as e:
            print(f"An error occurred in database module 'GET STOPPED NUMBER': {e}")

    def get_downloading_number(self):
        ''' Get all data in database with status of downloading'''
        try:
            connection = sqlite3.connect(self.dbname)
            cursor = connection.cursor()

            cursor.execute('select * from VideoData where status = "downloading"')
            data = cursor.fetchall()
            return len(data)
        except Exception as e:
            print(f"An error occurred in database module 'GET DOWNLOADING NUMBER': {e}")

    def get_total_number(self):
        ''' This get the total number of data already stored in the database '''
        try:
            connection = sqlite3.connect(self.dbname)
            cursor = connection.cursor()

            cursor.execute('select * from VideoData where status != ? ',('deleted',))
            data = cursor.fetchall()
            return len(data)
        except Exception as e:
            print(f"An error occurred in database module 'GET TOTAL NUMBER': {e}")

    def get_next_waiting_data(self):
        ''' This loop through the database and get the next item that has a status of waiting'''
        try:
            connection = sqlite3.connect(self.dbname)
            cursor = connection.cursor()

            cursor.execute('select * from VideoData where status = "waiting"')
            data = cursor.fetchall()
            return data[0]
        except Exception as e:
            print(f"An error occurred in database module 'GET NEXT WAITING DATA' :{e}")

    def get_status(self, url):
        ''' gets status of the specified url '''
        # try:
        connection = sqlite3.connect(self.dbname)
        cursor = connection.cursor()

        cursor.execute('select status from VideoData where url = ? ', (url,))
        data = cursor.fetchall()

        return data[0][0]
        # except Exception as e:
        #     print(f"An error occurred in database module ' GET STATUS' : {e}")
        #     return 'e'

    def get_status_by_playlist_url(self, playlist_url):
        ''' gets status of the specified url '''
        try:
            connection = sqlite3.connect(self.dbname)
            cursor = connection.cursor()

            cursor.execute('select status from VideoData where playlist_url = ? ', (playlist_url,))
            data = cursor.fetchall()

            return data[0][0]
        except Exception as e:
            print(f"An error occurred in database module ' GET STATUS' : {e}")

    def is_url_exists_in_database(self, url):
        '''
        checks if url (which is key identifier in vidoe database) exists to avoid duplicate
        '''
        try:
            connection = sqlite3.connect(self.dbname)
            cursor = connection.cursor()

            cursor.execute("select * from VideoData where url =?", (url,))
            data = cursor.fetchall()
            if len(data) == 0:
                return False
            else:
                return True
        except Exception as e:
            print(f"An error occurred in database module 'IS URL EXISTS IN DATABASE': {e}")

    def is_playlist_url_exists_in_database(self, url):
        '''
        checks if url (which is key identifier in vidoe database) exists to avoid duplicate
        '''
        try:
            connection = sqlite3.connect(self.dbname)
            cursor = connection.cursor()

            cursor.execute("select * from VideoData where playlist_url =?", (url,))
            data = cursor.fetchall()
            if len(data) == 0:
                return False
            else:
                return True
        except Exception as e:
            print(f"An error occurred in database module 'IS URL EXISTS IN DATABASE': {e}")

    def set_status(self, url, status):
        '''
        set status for provided key (url)
        '''

        try:
            connection = sqlite3.connect(self.dbname)
            cursor = connection.cursor()

            cursor.execute("update VideoData set status = ? where url = ?", (status, url))
            connection.commit()
            connection.close()
        except Exception as e:
            print(f"An error occurred in database module 'SET STATUS': ")

    def set_status_using_playlist_url(self, playlist_url, status):
        '''
        set status for provided key (url)
        '''

        try:
            connection = sqlite3.connect(self.dbname)
            cursor = connection.cursor()

            cursor.execute("update VideoData set status = ? where url = ?", (status, playlist_url))
            connection.commit()
            connection.close()
        except Exception as e:
            print(f"An error occurred in database module 'SET STATUS': ")

    def reset_all_status_to(self, status):
        '''
        loop through all the download stores in the database and set all their status to new status provided
        '''

        try:
            connection = sqlite3.connect(self.dbname)
            cursor = connection.cursor()
            cursor.execute("select * from VideoData")
            all = cursor.fetchall()
            for data in all:
                cursor.execute("update VideoData set status = ? where url = ? ", (status, data[4]))
                connection.commit()
            connection.close()
        except Exception as e:
            print(f"An error occurred in database module 'RESET ALL STATUS TO': {e}")

    def initialize_database(self):
        '''
        creates required tables for video and settings in the database
        checks for required settings key entry and create one if not available
        '''
        try:
            print("Initializing and checking the database...")
            # crates video table if it does not exists
            self.create_video_database()
            # crates settings table if it dow not exist.
            self.create_settings_database()

            # check for keys in setting stable and create one if it does not exist.
            if self.is_setting_key_in_database("max_download") is False:
                self.setup_create_settings("max_download", 2)

            if self.is_setting_key_in_database("max_retries") is False:
                self.setup_create_settings("max_retries", 5)

            if self.is_setting_key_in_database("default_download_location") is False:
                self.setup_create_settings("default_download_location", os.path.join(os.getcwd(), "download"))

        except Exception as e:
            print(f"An error occurred in database module 'INITIALIZE DATABASE': {e}")


class ErrorFlag():
    def __init__(self):
        super(ErrorFlag, self).__init__()
        self.error_detected = False
        self.error_details = None
        self.error_Location = None


class EmergencyError(Exception):
    pass


class InternetError(Exception):
    pass


class UnsupportedURLError(Exception):
    pass


class PrivateVideoError(Exception):
    pass


class SampleThread(QtCore.QThread):

    any_signal = QtCore.pyqtSignal(dict)

    def __init__(self, parent=None):
        super(SampleThread, self).__init__(parent)
        self.is_running = False


    def stop(self):
        ''' stops the thread '''
        try:
            self.is_running = False
            self.terminate()
        except Exception as e:
            print(f"An Error occurred in Common > Get statistics Thread > Stop: \n >>>{e}")

    def run(self):
        ''' kick start the whole thread and return updated value'''
        self.is_running = True

        try:
            while True:

                pass

        except Exception as e:
            self.is_running = False


class IsInternetThread(QtCore.QThread):

    any_signal = QtCore.pyqtSignal(dict)

    def __init__(self,myself, parent=None):
        super(IsInternetThread, self).__init__(parent)
        self.is_running = False
        self.is_internet = False
        self.general_functions = GeneralFunctions()
        self.data ={}
        self.myself = myself

    def stop(self):
        ''' stops the thread '''
        try:
            print('terminating Internet thread...')
            self.is_running = False
            self.terminate()
        except Exception as e:
            print(f"An Error occurred in Common > Get statistics Thread > Stop: \n >>>{e}")

    def run(self):
        ''' kick start the whole thread and return updated value'''
        self.is_running = True
        try:
            while True:
                print(f"internet connection thread is waiting for parent to be ready...")
                if self.myself.isReady is True:
                    break
                time.sleep(1)

            while True:
                if self.myself.isReady  is True:
                    if self.is_running is False:
                        break
                    self.is_internet = self.general_functions.IsInternet()
                    self.data['is_internet'] = self.is_internet
                    self.any_signal.emit(self.data)
                    time.sleep(0.5)
                    pass

            print(f'[XX] Internet thread stopped.')
        except Exception as e:
            self.is_running = False


class GetStatisticsThread(QtCore.QThread):
    ''' add provided items to the format list window represented by container '''
    any_signal = QtCore.pyqtSignal(dict)

    def __init__(self,myself, parent=None):
        super(GetStatisticsThread, self).__init__(parent)
        try:
            self.my_parent = myself
            self.is_running = False
            self.is_waiting_download = False
            self.is_max_download_exceeded = False
            self.db = self.my_parent.database
            self.max_download_allowed = int(self.db.get_settings('max_download'))
            self.max_retries = int(self.db.get_settings('max_retries'))
            self.default_download_location = self.db.get_settings('default_download_location')
        except Exception as e:
            print(f"An Error occurred in Common > get statistics thread > Init: \n>>>{e}")

    def stop(self):
        ''' stops the thread '''
        try:
            self.is_running = False
            self.terminate()
            print(f'[] GetStatisticsThread Stopped....')
        except Exception as e:
            print(f"An Error occurred in Common > Get statistics Thread > Stop: \n >>>{e}")

    def run(self):

        ''' kick start the whole thread and return updated value'''
        self.is_running = True
        print(f"[x] starting GetStatisticsThread...")
        try:
            while True:
                print(f"get statistics thread is waiting for parent to be ready...")
                if self.my_parent.isReady is True:
                    break
                time.sleep(3)

            while True:
                if self.is_running is False:
                    print('STOPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP')
                    break
                waiting_number = self.db.get_waiting_number()  # retrieve waiting number from the database
                completed_number = self.db.get_completed_number()  # retrieve completed number from the database
                stopped_number = self.db.get_stopped_number()  # retrieve stopped nuber from the database
                downloading_number = self.db.get_downloading_number()  # retrieve downloading number from the database
                total_number = self.db.get_total_number()  # retrieve total download number from database
                self.max_download_allowed = int(self.db.get_settings('max_download'))
                self.max_retries = int(self.db.get_settings('max_retries'))
                self.default_download_location = self.db.get_settings('default_download_location')
                if self.is_running is False:
                    print('STOPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP')
                    break
                # check and set value indicating that there are download still waiting to start downloading
                if waiting_number > 0:
                    self.is_waiting_download = True
                else:
                    self.is_waiting_download = False

                # check and set inicator showing max allowed download has been exceeded or not.
                if downloading_number < self.max_download_allowed:
                    self.is_max_download_exceeded = False
                else:
                    self.is_max_download_exceeded = True

                data = {
                    'waiting_number': waiting_number,
                    'completed_number': completed_number,
                    'stopped_number': stopped_number,
                    'downloading_number': downloading_number,
                    'total_number': total_number,
                    'is_waiting_download': self.is_waiting_download,
                    'is_max_download_exceeded': self.is_max_download_exceeded,
                    'max_download_allowed': self.max_download_allowed,
                    'max_retries': self.max_retries,
                    'default_download_location': self.default_download_location
                }
                # print(f"Emitting data : {data}")
                self.any_signal.emit(data)
                if self.is_running is False:
                    print('STOPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP')
                    break
                time.sleep(0.5)
            print(f'[XX] Getstatistics thread stopped.')
        except Exception as e:
            print(f"An error occurred in run: {e}")
            self.is_running = False


class LoadDataFromDatabaseThread(QtCore.QThread):
    ''' add provided item to the download list window '''
    any_signal = QtCore.pyqtSignal(dict)

    def __init__(self, items: list, parent=None):
        super(LoadDataFromDatabaseThread, self).__init__(parent)
        try:
            # self.index = index
            self.is_running = False
            self.item_list = items
            self.general_function = GeneralFunctions()
        except Exception as e:
            print(f"An Error occurred in  LoadDataFromDatabaseThread > Init(): \n >>>{e}")

    def stop(self):
        try:
            ''' stops the thread '''
            self.is_running = False
            self.terminate()

        except Exception as e:
            print(f"An Error occurred in Common > AddDownloadItemsThread > stop(): \n >>>{e}")

    def run(self):
        ''' kick start the whole thread and return updated value'''
        m_data = None

        try:
            # print(self.item_list)
            # input("Wait a bit.......")
            for item in self.item_list:
                if str(item[11]).lower() != 'deleted':
                    # print(f"item: {item}")
                    m_data = self.general_function.database_list_to_dictionary(item)
                    self.any_signal.emit(m_data)
                time.sleep(0.1)

            print('done loading successfully')
            m_data['data_loading_completed'] = True
            self.any_signal.emit(m_data)
        except Exception as e:
            print(f"An error occurred in run: {e}")
            self.is_running = False


class AddNewDownloadThread(QtCore.QThread):
    any_signal = QtCore.pyqtSignal(dict)

    def __init__(self, db, container, parent=None):
        super(AddNewDownloadThread, self).__init__(parent)
        self.is_running = False     # checks if the thread is running
        self.url = None     # holds the url
        self.data = {}  # holds data to be emitted
        self.db = db    # holds the database object
        self.container = container  # tracks the container for object interacting with. self.
        self.urlIsValid = False     # tracks url validity

        self.playlist_detected = False
        self.completed = False
        self.message = ""
        self.status = "waiting"
        self.logger = self.MyLogger()
        self.video_data = None
        self.counter = 0
        self.timer = QtCore.QBasicTimer()
        self.raw_data = None

        self.general_functions = GeneralFunctions()

        self.stop_info_board = False
        global addDownloadEmergencyStop
        addDownloadEmergencyStop = False

        self.container.groupBox_PlaylistOption.setVisible(False)    # hides the playlist option groupbox

        #   connects buttons('get info', 'browse download location', 'cancel' and 'ok') to functions
        self.container.buttonAddNewBrowseFileLocation.clicked.connect(lambda: self.browse_folder_location())
        self.container.buttonGetInfo.clicked.connect(lambda: self.get_info())
        self.container.buttonAddNewCancel.clicked.connect(lambda: self.stop())
        # self.container.buttonAddNewOK.clicked.connect(lambda: self.ok())

        self.reset_content()

        self.canceledByUser = False

    def ok(self):
        if self.is_running is True:
            # self.container.show_download_page()
            self.functions.run_function(self.container.show_download_page)

            def speedup():
                try:
                    download_data = []
                    download_data.clear()
                    url = self.url
                    download_location = self.container.textAddNewDownloadLocation.text()
                    download_video = self.container.radioButtonDownloadVideo.isChecked()
                    download_all_playlist = self.container.radioButtonPlaylistDownloadAll.isChecked()
                    selected_format = None

                    for x in range(self.container.scrollAreaWidgetContents_VideoFormat.layout().count()):  #
                        item = self.container.scrollAreaWidgetContents_VideoFormat.layout().itemAt(x).widget()  #
                        # print(f"type:;{type(item)}")
                        if type(item) == 'PyQt5.QtWidgets.QRadioButton':
                            if item.isChecked():
                                # assign the selected format to the the variable which will overwrite the default value of None
                                selected_format = item.text()

                    # extract video video data from the raw data
                    data = None
                    if self.playlist_detected:
                        data = GeneralFunctions.extract_playlist_video_download_data_list(GeneralFunctions, self.raw_data)
                        # data = common.extract_playlist_video_download_data_list(self.raw_data)
                    else:
                        data = GeneralFunctions.extract_single_video_download_data_list(GeneralFunctions, self.raw_data)
                        # data = common.extract_single_video_download_data_list(self.raw_data)
                    if data is not None:
                        for d in data:
                            mydata = {'download_video': download_video,
                                      'download_all': download_all_playlist,
                                      'format': selected_format,
                                      'title': d[0],
                                      'url': d[1],
                                      'is_playlist': d[2],
                                      'playlist_index': d[3],
                                      'playlist_title': d[4],
                                      'playlist_url': self.container.textURL.text(),
                                      'thumbnail': d[5],
                                      'status': 'waiting',
                                      'download_location': self.container.textAddNewDownloadLocation.text()
                                      }
                            download_data.append(mydata)

                    # self.load_items_into_items_window(download_data)
                    self.functions.run_function(self.load_items_into_items_window,False, download_data)

                except Exception as e:
                    print(f"An error occurred in 'AddNewDownload' OK : \n{e}")

            self.functions.run_function(speedup)

    def load_items_into_items_window(self, all_data):
        try:
            self.data.clear()

            for data in all_data:  # get next data

                # save to database
                data = self.functions.purify_raw_data_from_database_dict(data)

                self.db.insert_into_video_database(data)
                self.data['download_data'] = data
                # push for display
                self.any_signal.emit(self.data)
                time.sleep(0.1)
            self.reset_content()
        except Exception as e:
            print(f"An error occurred in ADDNewDownload' > load items into items window")
            self.reset_content()

    def reset_content(self):
        self.container.textURL.setText("")
        self.container.textAddNewDownloadLocation.setText("")
        self.clear_format_list()
        # print(self.container.threadController)

    def clear_format_list(self):
        try:
            if self.container.scrollAreaWidgetContents_VideoFormat.layout().count() > 0:
                for x in range(self.container.scrollAreaWidgetContents_VideoFormat.layout().count()):
                    self.container.scrollAreaWidgetContents_VideoFormat.layout().itemAt(x).widget().deleteLater()
        except Exception as e:
            print(f"An error occurred in 'AddewDowloadThread'> 'clear_format_list(): \n{e}")

    def browse_folder_location(self):
        try:
            if self.is_running is True:
                print('browsing for folder location...')
                dl = QFileDialog.getExistingDirectory(self.container, "open location")
                if dl != "":
                    self.container.textAddNewDownloadLocation.setText(dl)
        except Exception as e:
            print(f"An error occurred in 'COMMON'>'ADD NEW DOWNLOAD THREAD'>'browse folder location:\n{e}")

    def get_info(self):
        if self.is_running is True:
            url = self.container.textURL.text()
            if GeneralFunctions.is_url_valid(GeneralFunctions, url) is False:
                QMessageBox.information(self.container, f"Invalid url-{id(self)}", "The URL is invalid. Please provide a valid URL")
                self.container.textURL.selectAll()
                self.data['valid_url'] = False
                self.urlIsValid = False
            else:
                self.url = self.container.textURL.text()
                self.data['url'] = self.url
                self.data['valid_url'] = True
                self.urlIsValid = True
                self.any_signal.emit(self.data)
                self.container.buttonGetInfo.setVisible(False)

    def stop(self):
        ''' stops the thread '''
        global addDownloadEmergencyStop
        try:
            self.canceledByUser = True
            self.container.busy = False
            addDownloadEmergencyStop = True
            self.is_running = False
            self.container.show_download_page()
            self.container.message = 'Add New download Canceled by User'


        except Exception as e:
            #   signal handler must be signal.SIG_IGN, signal.SIG_DFL, or a callable object
            print(f"An error occurred in 'AddNewDownnloadThread' > stop.\n{e}")

    def reset(self):
        global addDownloadEmergencyStop
        try:
            self.is_running = False  # checks if the thread is running
            self.url = None  # holds the url
            self.data = {}  # holds data to be emitted
            # self.db = db  # holds the database object
            # self.container = container  # tracks the container for object interacting with. self.
            self.urlIsValid = False  # tracks url validity

            self.playlist_detected = False
            self.completed = False
            self.message = ""
            self.status = "waiting"
            self.logger = self.MyLogger()
            self.video_data = None
            self.counter = 0
            self.timer = QtCore.QBasicTimer()
            # self.timer.start(1000, self)
            # common.run_function(self.info_board)
            self.stop_info_board = False

            self.is_running = True
            addDownloadEmergencyStop = False
        except Exception as e:
            print(f"An error occurred in 'AddNewDownloadThread' > reset :\n{e}")

    def run(self):
        ''' kick start the whole thread and return updated value'''

        self.reset()
        self.container.busy = True
        try:
            self.url = pyperclip.paste()    # get the content of the clipboard and store it in url variable
            self.data['id'] = id(self)  # get id of this instance of the thread different from other instance
            self.data['url'] = self.url  # put obtained url in data container
            self.urlIsValid = self.general_functions.is_url_valid(self.url)
            self.data['valid_url'] = self.urlIsValid

            self.data['download_location'] = self.db.get_settings('default_download_location')
            self.any_signal.emit(self.data)
            time.sleep(1)

            # do not proceed until there is a valid url
            waiting_time = 1
            bak = self.container.labelInfo.styleSheet()
            flip = False
            while True:
                if self.is_running is False:
                    raise Exception
                if self.urlIsValid is True:
                    break
                print('waiting for a valid url')
                self.data['message'] = f"[ {waiting_time}s ] Waiting for a valid URL...\n" \
                                       f"[ Hint ] Please paste a valid URL in the space provided above."
                self.any_signal.emit(self.data)

                if flip is True:
                    self.container.labelInfo.setStyleSheet('color: red;')
                    flip = False
                else:
                    self.container.labelInfo.setStyleSheet('color: white;')
                    flip = True

                waiting_time += 1
                time.sleep(1)
                self.url = self.container.textURL.text()    # get the current text in the url textbox
                if self.url != "":  # if not empty
                    self.urlIsValid = self.general_functions.is_url_valid(self.url)     # check url validity
                    if self.urlIsValid: # if url is valid
                        self.container.labelInfo.setStyleSheet(bak)
                        self.data['url'] = self.url    # put valid url in data to be emitted
                        self.data['valid_url'] = self.urlIsValid    # set boolean value for valid url
                        self.data['message'] = "Valid URL detected"
                        self.any_signal.emit(self.data)
            time.sleep(1)


            # check if the valid url exists in the database
            self.data['message'] = "Checking if URL exists in the database"
            self.any_signal.emit(self.data)
            time.sleep(1)
            url_exists = self.db.is_playlist_url_exists_in_database(self.url)


            if url_exists is False:
                # check and wait for internet connection
                self.data['message'] = "checking Internet connection..."
                self.any_signal.emit(self.data)
                time.sleep(1)
                while True:     # check internet connection and don't proceed until there is internet connection
                    if self.is_running is False:
                        raise Exception
                    try:
                        ans = self.general_functions.IsInternet()
                        if ans is True:
                            break
                    except Exception as e:
                        self.data['message'] = f"Error!. {e}"
                        self.any_signal.emit(self.data)

                    print('Internet connection issue detected. Waiting for Internet connection to be available.')
                    self.data['message'] = f'Internet issue detected. Retrying. Please wait...'
                    self.any_signal.emit(self.data)
                    time.sleep(5)

                try:
                    # check if url contains playlist and store the value in a variable
                    print('checking if url contains playlist')
                    self.data['message'] = "Checking if url contains playlist"
                    self.any_signal.emit(self.data)
                    is_playlist = self.is_playlist(self.url)
                except:
                    raise Exception
                if is_playlist == "Error":
                    raise UnsupportedURLError

                print('starting info board.')
                self.data['message'] = "starting info board"
                self.any_signal.emit(self.data)
                self.general_functions.run_function(self.info_board)  # starts the info board

                # check and wait for internet connection
                while True:
                    if self.is_running is False:
                        raise Exception
                    if self.general_functions.IsInternet() is True:
                        break
                    print('Internet connection issue detected. Waiting for Internet connection to be available.')
                    self.data['message'] = "Internet Connection Issue deteced. Retrying. Please wait..."
                    self.any_signal.emit(self.data)
                    time.sleep(5)

                print('Getting raw data')
                self.data['message'] = "Getting Raw Data. Please wait..."
                self.any_signal.emit(self.data)
                self.raw_data = self.extract_info_dict(self.url)  # get raw data

                # print("RAW DATA=============================================")
                # print(self.raw_data)

                if self.raw_data == "Error":
                # private_video_detected = False
                # if str(self.raw_data).__contains__("Error"):
                #     if str(self.raw_data).__contains__("Private"):
                #         if is_playlist is False:
                #             raise PrivateVideoError
                #         else:
                #             print("One private video skipped")
                #             private_video_detected = True
                #     else:
                    raise UnsupportedURLError

                # if private_video_detected is False:
                self.stop_info_board = True  # a trigger to stop the info board as soon as not needed again

                self.data['raw_data'] = self.raw_data
                self.data['isplaylist'] = is_playlist
                self.any_signal.emit(self.data)
                time.sleep(1)
                self.data.pop('raw_data')
                self.data.pop('isplaylist')
                # check is_playlist status
                self.data['message'] = "Checking playlist status..."
                self.any_signal.emit(self.data)
                if is_playlist:
                    # set a trigger that main or calling function will use to hide or show playlist option
                    self.playlist_detected = True
                    self.container.groupBox_PlaylistOption.setVisible(True)  # shows the playlist option groupbox
                else:
                    self.container.groupBox_PlaylistOption.setVisible(False)  # hides the playlist option groupbox
                    self.playlist_detected = False

                self.data['message'] = "Detecting available video format for your video. Please wait..."
                self.any_signal.emit(self.data)
                formats_detected = None
                if self.raw_data is not None:
                    # get video format information from the extracted data
                    if is_playlist is False:
                        formats_detected = self.get_video_formats(self.raw_data)
                    else:
                        formats_detected = self.get_playlist_video_formats(self.raw_data)

                if formats_detected is not None:
                    for data in formats_detected:
                        title = self.screenTitle(data[0])
                        size = data[1]
                        if size is not None:
                            size = self.convert_size(size)

                        # self.is_running = False
                        self.completed = True
                        self.status = f"{title} - {size}"
                        self.message = f'extracting format - {self.status}'
                        self.data = {
                            'status': self.status,
                            'message': self.message
                        }
                        self.container.show_add_new_page()
                        self.any_signal.emit(self.data)
                        time.sleep(0.01)
                    self.data['message'] = "Data Extraction Completed! click OK to add to download list."
                    self.container.show_add_new_page()
                    self.any_signal.emit(self.data)

                else:
                    print('no formats detected ')
                    self.data['message'] = "No video format detected. Please click Ok to use best format"
                    self.any_signal.emit(self.data)
                    self.container.busy = False
                self.container.busy = False
            else:
                # if url exist in the database do not proceed
                self.data['url_exists'] = True
                self.data['message'] = "url already exists in the database. Please obtain a new url to download"
                self.data['url'] = self.url
                self.any_signal.emit(self.data)
                time.sleep(1)
                self.data.pop('url_exists')
                self.container.busy = False
                pass
            if addDownloadEmergencyStop is True:
                self.data['message']= 'Add New download Canceled by User'
                self.any_signal.emit(self.data)
        except UnsupportedURLError:
            try:
                print("Unsupported URL supplied. Please check it's a video URL")
                self.data["unsupported_url"] = True
                self.data['message'] = "Unnsupported URL supplied. Please check if it's a video URL and try again."
                self.any_signal.emit(self.data)
                self.is_running = False
                time.sleep(1)
                self.data.pop('unsupported_url')
                self.container.busy = False
                self.container.buttonAddNewCancel.click()
                self.container.message = "UnsupportedURLError"

            except Exception as e:
                print(f"Error within error:{e}")
                self.container.busy = False
                if self.canceledByUser is True:
                    self.container.message = 'Add New download Canceled by User'

                # self.container.message = str(e)+ str(self.db)

        except PrivateVideoError:
            print("Private video. Sign in if you've been granted access to this video")
            self.data["unsupported_url"] = True
            self.data['message'] = "Private video. Sign in if you've been granted access to this video."
            self.any_signal.emit(self.data)
            self.is_running = False
            time.sleep(0.1)
            self.data.pop('unsupported_url')
            self.container.busy = False
            self.container.buttonAddNewCancel.click()
            time.sleep(0.5)
            self.container.message = "Error! Private video detected. Sign in if you've been granted access to this video\n" \
                                     "[hint] Sorry Video Login Option not supported in this version of video downloader. Please try another URL"

        except Exception as e:
            print(f"An error occurred in run: {e}")
            # if self.canceledByUser is True:
            #     self.container.message = 'Add New download Canceled by User'
            self.is_running = False
            self.container.busy = False
            # self.container.message = str(e) + str(self.db)

    #   --------------------------------------------------------

    def info_board(self):
        try:
            while True:
                self.data = {
                    'status': self.status,
                    'playlist_detected': self.playlist_detected,
                    'message': str(self.logger.inner_message).replace("Downloading","Extracting data for Playlist") + ". This is required once. Please Wait..."
                }

                self.any_signal.emit(self.data)
                time.sleep(1)
                if self.is_running is False or self.stop_info_board is True:
                    break

        except Exception as e:
            print(f"An error occurred in 'AddNewDownloadThread > info_board:\n {e}")

    def screenTitle(self, title):
        final = ""
        for c in title:
            if c.isalnum() or c.isalpha() or c.isspace() or c.isnumeric() or c.isdigit() or c.isidentifier():
                final = final + c

        return final

    def convert_size(self, size_bytes):
        ''' This function converts size in bytes to respective value in KB, MB, GB...'''
        if size_bytes == 0:
            return "0B"
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(size_bytes, 1024)))
        p = math.pow(1024, i)
        s = round(size_bytes / p, 2)
        return "%s %s" % (s, size_name[i])

    class MyLogger(object):
        global addDownloadEmergencyStop
        inner_message = "Please Wait..."

        def debug(self, msg):
            global addDownloadEmergencyStop
            try:
                # print(msg)

                if addDownloadEmergencyStop is True:
                    print('force stop')
                    signal.signal(signal.SIGTERM, self.debug)

                if str(msg).__contains__('[download]'):
                    self.inner_message = msg

                if str(msg).__contains__('Finished'):
                    # self.inner_message = "Done!"
                    pass

                if str(msg).lower().__contains__('already'):
                    print("already downloade.....")
                    print()

                pass
            except Exception as e:
                signal.signal(signal.SIGTERM, youtube_dl.YoutubeDL.extract_info)
                print('here:::', e)

        def warning(self, msg):
            pass

        def error(self, msg):
            pass

    def my_hook(self, d):
        try:
            print(d)
            if d['status'] == 'finished':
                self.counter += 1
                if self.counter == 1:
                    print('Done downloading, now converting ...')
                if self.counter == 2:
                    self.counter = 0
                    print("Completed!")
                    print()
        except Exception as e:
            pass

    def is_playlist(self, url: str):
        try:
            opt = {
                'extract_flat': True
            }

            with youtube_dl.YoutubeDL(opt) as ydl:
                d = ydl.extract_info(url, False)
                self.video_data = d
                if d['_type']:
                    return True
                else:
                    return False
        except Exception as e:
            if str(e).__contains__("urlopen error") or str(e).lower().__contains__('unsupported url') or str(e).lower().__contains__('not a valid URL'.lower()):
                return "Error"
            else:
                return False

    def extract_info_dict(self, url):

        try:
            ''' extract info that can be used in list_format function'''
            ydl_opts = {
                'postprocesor-args': 'loglevel quiet, -8',
                'password': 'Zu@6LFzU',
                'nopart': True,
                'quiet': True,
                'ignoreerrors':True,
                'logger': self.logger,
                'progress_hooks': [self.my_hook],
            }

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                # ydl.download([url])
                info = ydl.extract_info(url, download=False)

                return info
        except Exception as e:
            if str(e).__contains__('urlopen error'):
                print("Internet connection issue!")
                return "Error"

            if str(e).__contains__('Private video'):
                print("Internet connection issue!")
                return "Error: Private Video"

            print(f"Error in extrac_info_dict: {e}")

    def get_video_formats(self, data):
        format_list = []

        try:
            for format in data['formats']:
                try:
                    f = (format['format'], format['filesize'])
                    format_list.append(f)
                except Exception as e:
                    if str(e).__contains__('filesize'):
                        # print(format['format'], "--", "None", "--", format['ext'])
                        pass
                    else:
                        print(f"Error: {e}")
                    continue
            if len(format_list) > 0:
                return format_list
            else:
                format_list.append(("No Format detected. Click 'OK' to continue.", 0))
                return format_list
        except:
            format_list.append(("No Format detected. Click 'OK' to continue.", 0))
            return format_list

    def get_playlist_video_formats(self, data):
        format_list = []
        entries = data['entries'][0]
        formats = entries['formats']

        for format in formats:
            try:
                f = (format['format'], format['filesize'])
                format_list.append(f)
            except Exception as e:
                if str(e).__contains__('filesize'):
                    # print(format['format'], "--", "None", "--", format['ext'])
                    pass
                else:
                    print(f"Error: {e}")
                continue
        # print("Returning below...")
        # print(format_list)
        return format_list


class AddNewOkThread(QtCore.QThread):
    any_signal = QtCore.pyqtSignal(dict)

    def __init__(self, container, raw_data, is_playlist,  parent=None):
        super(AddNewOkThread, self).__init__(parent)
        self.container = container
        self.raw_data = raw_data
        self.is_playlist= is_playlist
        self.general_functions = GeneralFunctions()

    def stop(self):
        ''' stops the thread '''
        # self.is_running = False
        self.terminate()
        print("[] AddNewOkThread Stopped..")

    def run(self):
        ''' kick start the whole thread and return updated value'''

        try:
            try:
                download_data = []
                download_data.clear()
                url = self.container.textURL.text()

                download_location = self.container.textAddNewDownloadLocation.text()
                download_video = self.container.radioButtonDownloadVideo.isChecked()
                download_all_playlist = self.container.radioButtonPlaylistDownloadAll.isChecked()

                # initialize download format to none
                selected_format = None

                # scan all format radio button to detect which one was selected by user.
                for x in range(self.container.scrollAreaWidgetContents_VideoFormat.layout().count()):  #
                    item = self.container.scrollAreaWidgetContents_VideoFormat.layout().itemAt(x).widget()  #
                    try:
                        # print(item.text(), '<>', item.isChecked() ,'<>', type(item))
                        if item.isChecked() is True:
                            selected_format = item.text()
                            break
                    except Exception as e:
                        print(e)
                        continue
                # extract video video data from the raw data
                data = None

                print(f'selected format : {selected_format}')

                if self.is_playlist is True:
                    data = self.general_functions.extract_playlist_video_download_data_list( self.raw_data)
                    # data = common.extract_playlist_video_download_data_list(self.raw_data)
                else:
                    data = self.general_functions.extract_single_video_download_data_list( self.raw_data)
                    # data = common.extract_single_video_download_data_list(self.raw_data)

                if data is not None:
                    for d in data:
                        mydata = {'download_video': download_video,
                                  'download_all': download_all_playlist,
                                  'format': selected_format,
                                  'url': d[1],
                                  'title': d[0],
                                  'is_playlist': d[2],
                                  'playlist_index': d[3],
                                  'playlist_title': d[4],
                                  'playlist_url': self.container.textURL.text(),
                                  'thumbnail': d[5],
                                  'status': 'waiting',
                                  'download_location': self.container.textAddNewDownloadLocation.text()
                                  }
                        download_data.append(mydata)
                print('done')
                # self.load_items_into_items_window(download_data)
                # self.functions.run_function(self.load_items_into_items_window, False, download_data)

            except Exception as e:
                print(f"An error occurred in 'AddNewDownload' OK : \n{e}")

            for item in download_data:
                self.any_signal.emit(item)
                time.sleep(0.1)
            self.container.scrollToBottom()
            time.sleep(1)
            self.container.message  = "Ready!"

        except Exception as e:
            print(f"An error occurred in run: {e}")


class LoadItemDataThread(QtCore.QThread):
    any_signal = QtCore.pyqtSignal(dict)

    def __init__(self, data, my_self):
        super(LoadItemDataThread, self).__init__()
        try:
            # print(data)
            self.my_parent = my_self

            self.title = data['title']
            self.status = data['status']
            self.downloadVideo = bool(data['download_video'])
            self.downloadAll = bool(data['download_all'])
            self.downloadFormat = data['format']
            self.videoURL = data['url']

            self.isPlaylist = bool(data['is_playlist'])
            self.playlistIndex = data['playlist_index']
            self.playlistTitle = data['playlist_title']
            self.playlistURL = data['playlist_url']
            self.thumbnail = data['thumbnail']
            self.downloadLocation = data['download_location']

            self.emitData ={}

            self.general_functions = GeneralFunctions()
            self.imageData = None
            pass

        except Exception as e:
            print(f"An Error Occurred in jbavdLibrary > LoadItemDataThread > __init__()[]{self.title}: \n >>{e}")

    def display_content(self):

        def start():

            try:
                img_data = requests.get(self.thumbnail).content
                tempFilename = f"temp_{random.randrange(1000, 9999)}"

                # checkpoint 1
                with open(f"temp\\{tempFilename}", 'wb') as f:
                    f.write(img_data)

                try:
                    self.my_parent.labelImage.setPixmap(QPixmap(f"temp\\{tempFilename}"))
                    self.my_parent.labelImage.setScaledContents(True)
                except Exception as e:
                    self.my_parent.labelImage.setText("image Error")

            except:
                self.my_parent.labelImage.setText("No Image")

        self.general_functions.run_function(start)
        # start()

    def load_image(self):
        try:
            self.imageData = requests.get(self.thumbnail).content
        except Exception as e:
            self.my_parent.labelImage.setText("Image \n Loading \nError")
            self.imageData = 'Error'
            pass

    def stop(self):
        self.terminate()
        print("[] LoadItemDataThread Stopped.")

    def run(self):
        # print(f"[x] Starting LoadItemDataThread: {self.title}")
        try:

            self.my_parent.progressBar.setValue(0)  # reset progress bar value to 0

            # image data is in byte. need to be saved to file
            # check if directory 'temp' where image will be store does not exist then create the directory
            if os.path.exists("temp") is False:
                os.makedirs("temp")

            self.my_parent.labelImage.setText("Loading...")

            # trying to load the image from internet using a separate thread to avoid slowing down the app
            self.general_functions.run_function(self.load_image)

            # show the video title. formatting it depending of playlist or not
            if self.isPlaylist is True:
                self.my_parent.textTitle.setText(f"{self.playlistIndex}. [{self.playlistTitle}] - {self.title}")
                pass
            else:
                self.my_parent.textTitle.setText(self.title)

            self.my_parent.textStatus.setText(self.status)  # set the status of the download as received

            # wait for image to be downloaded from internet or error occures while downloading before proceeding
            while True:
                time.sleep(1)
                if self.imageData is not None:  #    if image has been downloaded or an error occurred. proceed
                    break

            if self.imageData != "Error":   # if error did not occurred. continue to process the image
                tempFilename = f"temp_{random.randrange(1000, 9999)}"   # create a temporary filename to save the image byte on the pc

                # write the image byte obtained from internet to file using the tempfilename generated above
                with open(f"temp\\{tempFilename}", 'wb') as f:
                    f.write(self.imageData)

                try:
                    # show the image saved in the image placeholder or label
                    self.my_parent.labelImage.setPixmap(QPixmap(f"temp\\{tempFilename}"))
                    self.my_parent.labelImage.setScaledContents(True)   # scale the content of the image to fit the size of the container.
                except Exception as e:
                    # if an error occurred image error placeholder on the image box.
                    self.my_parent.labelImage.setText("image Error")

                self.my_parent.dataLoadingCompleted = True  # signal parent. itemwindow that we are done here with this
                self.emitData['completed'] = True   # set emit signal (an alternative to the above)
                self.any_signal.emit(self.emitData) # emit the signal (an alternative)
                pass
        except Exception as e:
            print(f"An Error Occurred in JbavdLibrary > LoadItemDataThread > Run :\n>>{e}")


class DownloadMonitoringEngineThread(QtCore.QThread):
    ''' add provided item to the download list window '''
    any_signal = QtCore.pyqtSignal(dict)

    def __init__(self, container, parent=None):
        super(DownloadMonitoringEngineThread, self).__init__(parent)

        # self.index = index
        self.is_running = False
        self.db = VideoDatabase()
        self.downloading_number = self.db.get_downloading_number()

        self.is_waiting_download = False
        self.is_max_download_exceeded = False
        self.functions = GeneralFunctions()
        self.my_parent = container
        self.max_download_allowed = int(self.db.get_settings('max_download'))
        self.emitData ={}

    def stop(self):
        ''' stops the thread '''
        self.is_running = False
        # time.sleep(1)
        self.terminate()
        print(f"[] Downloader Engine Stopped.")

    def get_statistics(self):
        try:
            waiting_number = self.db.get_waiting_number()  # retrieve waiting number from the database
            self.downloading_number = self.db.get_downloading_number()  # retrieve downloading number from the database
            self.max_download_allowed = int(self.db.get_settings('max_download'))

            # check and set value indicating that there are download still waiting to start downloading
            if waiting_number > 0:
                self.is_waiting_download = True
            else:
                self.is_waiting_download = False

            # check and set indicator showing max allowed download has been exceeded or not.

            if self.downloading_number < self.max_download_allowed:
                self.is_max_download_exceeded = False
            else:
                self.is_max_download_exceeded = True

            return 'success'
        except Exception as e:
            print(f'An error occurred in download engine thread > get statistics: \n{e}')
            return 'error'

    def run(self):
        ''' kick start the whole thread and return updated value'''
        self.is_running = True
        # time.sleep(10)
        print('[x] Downloader Monitoring Engine Started...')
        try:
            while True:
                print(f"download monitoring thread is waiting for parent to be ready...")
                if self.my_parent.isReady is True:
                    break
                time.sleep(3)

            while True:
                if self.is_running is False:
                    break
                # print("[][] downloader engine running")
                if self.is_running is True:
                    ans = self.get_statistics()
                    if ans != 'error':
                        if self.is_waiting_download is True:  # check if there are waiting downloads
                            # print("waiting download found..........")
                            if self.is_max_download_exceeded is False:  # check if max download limit has not been exceeded

                                data = self.db.get_next_waiting_data()  # get next waiting data
                                nextWaitingData = self.functions.purify_raw_data_from_database_list(
                                    data)  # reformat the waiting data
                                self.any_signal.emit(nextWaitingData)
                                time.sleep(2) #  small delay before auto starting the next one
                                self.db.set_status(nextWaitingData['url'],
                                                   'downloading')  # change status of the next waiting to downloading

                            else:
                                # print("max download allowed exceeded. Rechecking.........")
                                try:
                                    if self.downloading_number > self.max_download_allowed:

                                        counter = 0
                                        try:

                                            if self.my_parent.scrollAreaWidgetContents.layout().count() > 0:
                                                for x in range(self.my_parent.scrollAreaWidgetContents.layout().count()):
                                                    # status = self.my_parent.scrollAreaWidgetContents.layout().itemAt(
                                                    #     x).widget().textStatus.text()
                                                    url = self.my_parent.scrollAreaWidgetContents.layout().itemAt(
                                                        x).widget().videoURL
                                                    status = self.db.get_status(url)
                                                    if status == 'list index out of range':
                                                        break

                                                    counter += 1
                                                    if counter > self.max_download_allowed:
                                                        if status == 'downloading':
                                                            self.my_parent.database.set_status(url, 'waiting')

                                        except Exception as e:
                                            print(f"An error occurred in 'clear download item': \n{e}")
                                        pass
                                except:
                                    print(f"An error occurred while sanitizing")

                                # print("there are pending downloads but no slots to start them")
                                pass

                        else:
                            # print("No waiting download")
                            try:
                                if self.downloading_number > self.max_download_allowed:

                                    counter = 0
                                    try:

                                        if self.my_parent.scrollAreaWidgetContents.layout().count() > 0:
                                            for x in range(self.my_parent.scrollAreaWidgetContents.layout().count()):
                                                # status = self.my_parent.scrollAreaWidgetContents.layout().itemAt(
                                                #     x).widget().textStatus.text()
                                                url = self.my_parent.scrollAreaWidgetContents.layout().itemAt(
                                                    x).widget().videoURL
                                                status = self.db.get_status(url)
                                                if status == 'list index out of range':
                                                    break
                                                counter += 1
                                                if counter > self.max_download_allowed:
                                                    if status == 'downloading':
                                                        self.my_parent.database.set_status(url, 'waiting')

                                    except Exception as e:
                                        print(f"An error occurred in 'clear download item': \n{e}")
                                    pass
                            except:
                                print(f"An error occurred while sanitizing")
                            pass

                    time.sleep(2)
                else:
                    break
        except Exception as e:
            print(f"An error occurred in LOAD ENGINE : {e}")


class ItemWindowDownloaderEngine(QtCore.QThread):
    any_signal = QtCore.pyqtSignal(dict)

    def __init__(self, data, my_parent):
        super(ItemWindowDownloaderEngine, self).__init__()
        try:
            # print(f"data:  {data}")
            self.is_running = False
            self.my_parent = my_parent
            self.title = data['title']
            self.status = data['status']
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
            self.downloadLocation = data['download_location']
            self.db = VideoDatabase()

            self.retries_counter = 0
            self.max_retries = int(self.my_parent.database.get_settings('max_retries'))

            self._eta = "0:00"
            self._speed = "0 kbs"
            self._downloaded = "0 kb"
            self._size = "0 kb"
            self._percent = "0 %"

            self.functions = GeneralFunctions()
            self.Logger = self.MyLogger()
            self.Logger.logger_functions = self.functions
            self.Logger.url = self.videoURL

            self.emitData = {}
            self.message = "..."
            self.errorDetected = False
            self.errorMessage = None

            self.finish_counter = 0

            self.downloadCompleted = False

        except Exception as e:
            print(f"An Error Occurred in jbavdLibrary > ItemWindowDownloaderEngine > __init__(): \n >>{e}")

    def stop(self):
        self.is_running = False
        self.terminate()
        print(f"[] ItemWindowDownloaderEngine Stopped..")

    def run(self):
        # time.sleep(0.2)
        self.is_running = True
        print(f"[x] Staring ItemWindowDownloaderEngine..{self.title}")
        self.downloadCompleted = False
        # self.downloadLocation = self.db.get_settings('default_download_location')
        self.downloadLocation = self.downloadLocation

        try:
            if self.downloadFormat is None:
                self.functions.run_function(self.download, False, self.videoURL, self.downloadLocation)
            else:
                self.functions.run_function(self.download, False, self.videoURL, self.downloadLocation, self.downloadFormat)

            while True:
                if self.is_running is False:
                    break
                self.max_retries = int(self.my_parent.database.get_settings('max_retries'))
                self.Logger.loggerEmergencyStop = self.my_parent.emergencyStop
                self.emitData['message'] = self.message
                self.emitData['logger_message'] = self.Logger.loggerMessage
                self.emitData['error'] = self.errorDetected
                self.emitData['error_message'] = self.errorMessage
                self.emitData['eta'] = self._eta
                self.emitData['downloaded'] = self._downloaded
                self.emitData['speed'] = self._speed
                self.emitData['size'] = self._size
                self.emitData['percent'] = self._percent
                self.emitData['already_downloaded'] = self.Logger.alreadyDownloaded
                self.emitData['completed'] = False
                self.emitData['emergency_stop'] = False

                if self.Logger.loggerEmergencyStop is True:
                    print("stopped by Emergency")
                    self.message = "Download Stopped by User"
                    self.emitData['emergency_stop'] = True
                    self.any_signal.emit(self.emitData)
                    # self.stop()
                    break

                elif self.Logger.alreadyDownloaded is True:
                    print("stopped by Already downloaded")
                    self.db.set_status(self.videoURL, "completed")
                    self.message = "Video already downloaded"
                    self.emitData['already_downloaded'] = True
                    self.emitData['message'] = self.message
                    # print(self.emitData)
                    self.any_signal.emit(self.emitData)
                    # self.stop()
                    break

                elif self.downloadCompleted is True:
                    print("stopped by download completed")
                    # self.db.set_status(self.videoURL, "completed")
                    self.message = "Completed"
                    self.emitData['completed'] = True
                    self.emitData['message'] = self.message
                    # print(self.emitData)
                    self.any_signal.emit(self.emitData)
                    # self.stop()
                    break
                else:
                    # print(f'emmitted datttaaaa: {self.emitData}')
                    self.any_signal.emit(self.emitData)

                time.sleep(1)

        except Exception as e:
            print(f"An Error Occurred in JbavdLibrary > ItemWindowDownloaderEngine > Start: \n >>> {e}")

    class MyLogger(object):
        loggerEmergencyStop = False
        alreadyDownloaded = False
        logger_functions = None
        url = None
        loggerMessage = "..."
        loggerCompleted = False
        fragment = False

        def debug(self, msg):
            try:
                if self.loggerEmergencyStop is True:
                    print('emergecny stop detected! in Logger [][][][][][][][][][]')
                    signal.signal(signal.SIGTERM, self.debug)
                    raise EmergencyError

                # print(">>> ", msg)
                self.loggerMessage = msg
                if str(msg).lower().__contains__('already'):
                    print(f"already downloaded.....{self.url}")
                    self.loggerMessage = "url already downloaded"

                    self.alreadyDownloaded = True
                    counter = 0
                    # signal.signal(signal.SIGTERM, self.debug)
                    # raise EmergencyError

                if str(msg).lower().__contains__('destination'):
                    print(f"initial destination file: {str(msg).split(':')[1]}")
                    print(msg)
                    if str(msg).lower().__contains__('ffmpeg'):
                        print(f"final destination file: {str(msg).split(':')[1]}")
                        print(msg)
                if str(msg).lower().__contains__('deleting original file'):
                    print(msg)
                    print(f"Audio download completed. Thanks")

                if self.fragment == False:
                    if str(msg).lower().__contains__('frag'):
                        self.fragment = True

                if str(msg).lower().__contains__('Fixing'):
                    self.loggerCompleted = True
                    print("Completed by fixing")

                pass
            except EmergencyError:
                signal.signal(signal.SIGTERM, youtube_dl.YoutubeDL.download)

                pass
            except Exception as e:
                signal.signal(signal.SIGTERM, youtube_dl.YoutubeDL.download)
                pass

        def warning(self, msg):
            pass

        def error(self, msg):
            if self.logger_functions is not None:
                if self.logger_functions.IsInternet() is False:
                    print("Internet connection issue")
                    self.loggerMessage = "Internet connection issue"
                else:
                    signal.signal(signal.SIGTERM, self.debug)
            pass

    def my_hook(self, d):
        if self.Logger.loggerEmergencyStop is True:
            print('emergecny stop detected! in my hook[][][][][][][][][][]')
            # emergency_stop = False
            # signal.signal(signal.SIGTERM, self)
            raise EmergencyError

        try:
            # print(">>>>>>>> " , d)
            # print(f"stopper: {stopper}")

            if d['status'] == 'finished':
                self.finish_counter += 1
                if self.finish_counter == 1:
                    if self.downloadVideo is True:
                        print('Done downloading, now converting ...')
                        if self.Logger.fragment is True:
                            print('completed by fragment')
                            self.finish_counter = 2
                        else:
                            self.downloadCompleted = True
                    else:
                        print("Download completed for Audio")
                        self.db.set_status(self.videoURL, 'completed')
                        # raise EmergencyError

                if self.finish_counter == 2:
                    self.finish_counter = 0
                    print("Completed!!!!!!!!!!!!!!!!!!!!!!!")
                    self.downloadCompleted = True
                    # self.download_in_progress = False
                    # self.db.set_status(self.url, 'completed')
                    # self.database.set_status(self.videoURL, 'completed')
                    self.db.set_status(self.videoURL, 'completed')
                    # raise EmergencyError
                if self.Logger.loggerCompleted is True:
                    self.finish_counter = 2

            try:
                self._eta = str(d['_eta_str'])
            except:
                self._eta = "00:00"

            try:
                self._speed = d['_speed_str']
            except:
                self._speed = "-:-"

            try:
                self._downloaded = str(self.functions.convert_size(d['downloaded_bytes']))
            except:
                self._downloaded = "-:-"

            try:
                self._size = str(self.functions.convert_size(d['total_bytes']))
            except:
                self._size = "-"

            try:
                self._percent = d['_percent_str']
            except:
                self._percent = "100%"



        except EmergencyError:
            signal.signal(signal.SIGTERM, self.my_hook)
            self.Logger.loggerEmergencyStop = False
            pass

    def download(self, url,
                 directory='downloads',
                 video_format='bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'):

        self.Logger.loggerEmergencyStop = False

        # check if the root directory exists, if not create one.
        if directory == 'downloads':
            full_download_path = os.path.join(os.getcwd(), directory)
            if os.path.exists(full_download_path) is False:
                os.makedirs(full_download_path)

        if video_format != 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best':
            video_format = str(video_format).split(" ")[0].strip()

        print(f"selected format  is ::::::::::::{video_format}")



        # set the output template depending on wether the url is playlist or not
        if self.isPlaylist:
            outtmpl = f'{directory}/{self.playlistTitle}/{self.playlistIndex}-{self.title}.%(ext)s'
        else:
            outtmpl = f'{directory}/{self.title}.%(ext)s'

        # se the looger object
        logger = self.Logger

        # check if Audio or vidoe is being downloaded and set youtube dl option accordingly
        if self.downloadVideo is True:
            # option for downloading video
            ydl_opts = {
                'outtmpl': outtmpl,
                'format': video_format,
                'password':'Zu@6LFzU',
                # 'writethumbnail': True,
                'postprocesor-args': 'loglevel quiet, -8',
                'nopart': True,
                'quiet': True,
                'logger': logger,
                'progress_hooks': [self.my_hook],
            }
        else:
            # option for downloading audio
            ydl_opts = {
                'outtmpl': outtmpl,
                'format': 'bestaudio/best',
                # 'password':'Zu@6LFzU',
                # 'writethumbnail': True,
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',

                }],
                'postprocesor-args': 'loglevel quiet, -8',
                'nopart': True,
                'quiet': True,
                'logger': logger,
                'progress_hooks': [self.my_hook],
            }

        # downloading with youtube-dl with the opiton set above.
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
                # info = ydl.extract_info(url, download=True)
        except Exception as e:
            if self.Logger.loggerEmergencyStop is False:
                if self.functions.IsInternet() is False:
                    self.retries_counter += 1
                    if self.retries_counter <= self.max_retries:
                        print("retrying download in 5s")
                        time.sleep(5)
                        print(f"retrying [{self.retries_counter}/{self.max_retries}]...")
                        self.message = f"retrying [{self.retries_counter}/{self.max_retries}]..."
                        self.download(url, directory, video_format)
                    else:
                        print(
                            f"Internet Connection issue. Download stopped after {self.max_retries} retries. Please restart downloading of '{self.title}' when connection is restored.")
                        self.message = f"Internet Connection issue. Download stopped after {self.max_retries} retries. Please restart downloading of '{self.title}' when connection is restored."
                        self.db.set_status(self.videoURL, 'stopped')
                        self.retries_counter = 0
                        print("[][][][][][][][][][][][][][][][][][][]")


class ActivityStopperThread(QtCore.QThread):
    any_signal = QtCore.pyqtSignal(dict)

    def __init__(self, myself, parent=None):
        super(ActivityStopperThread, self).__init__(parent)

        try:
            self.is_running = False
            self.my_self = myself
            self.message = ""
            self.data={}
        except Exception as e:
            print(f'Error in init: {e}')

    def stop(self):
        ''' stops the thread '''
        try:
            self.is_running = False
            self.terminate()
        except Exception as e:
            print(f"An Error occurred in Common > Get statistics Thread > Stop: \n >>>{e}")

    def run(self):
        ''' kick start the whole thread and return updated value'''
        self.is_running = True
        print("in thread....")
        try:
            # stop all download in progress:
            self.message = f"Attempting to stop all running downloads. Please wait..."
            self.data['message'] = self.message
            self.any_signal.emit(self.data)

            if self.my_self.scrollAreaWidgetContents.layout().count() > 0:
                for x in range(self.my_self.scrollAreaWidgetContents.layout().count()):

                    if self.my_self.scrollAreaWidgetContents.layout().itemAt(x).widget().textStatus.text() == 'downloading':
                        self.my_self.scrollAreaWidgetContents.layout().itemAt(x).widget().stop_downloading()
                        self.message = f"stopping {self.my_self.scrollAreaWidgetContents.layout().itemAt(x).widget().title}'..."
                        self.data['message'] = self.message
                        print(self.message)
                        self.any_signal.emit(self.data)
                        time.sleep(0.1)
            time.sleep(1)
            # stop all running thread
            total = len(self.my_self.threadController)
            for index, thread in enumerate(self.my_self.threadController):
                self.message = f"[{round(((index + 1)/total) *100)}%] Preparing to Restore. Please wait... '{thread}'..."
                print(f"[{index+1}/{total}]Stopping thread '{thread}'...")
                self.data['message'] = self.message
                self.any_signal.emit(self.data)
                self.my_self.threadController[thread].stop()
                # thread.stop()
                time.sleep(0.1)

            time.sleep(1)
            self.data['completed'] = True
            self.any_signal.emit(self.data)
        except Exception as e:
            self.is_running = False
