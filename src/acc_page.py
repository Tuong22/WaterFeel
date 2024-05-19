import unicodedata
import re
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QShortcut
from PyQt5.QtGui import QKeySequence
from database import Database

class Ui_AccPageWindow(QtWidgets.QMainWindow):
    """
    Giao diện người dùng cho trang thông tin tài khoản (Account Page).

    Class này thiết lập và quản lý giao diện hiển thị thông tin bài hát,
    bao gồm các thành phần như:

        - Thông tin bài hát (tên, hình ảnh poster,...)
        - Các nút điều khiển (play, pause, stop,...)

    Attributes:
        None (Tất cả các thành phần giao diện được khởi tạo trong phương thức `setupUi`)

    Methods:
        setupUi(self, AccPageWindow): Thiết lập giao diện người dùng.
        retranslateUi(self, AccPageWindow): Dịch lại nội dung văn bản trên giao diện.
    """
    def setupUi(self, AccPageWindow):
        """
        Khởi tạo và thiết lập các thành phần giao diện cho trang thông tin tài khoản.

        Args:
                MainWindow (QtWidgets.QMainWindow): Cửa sổ chính chứa trang thông tin tài khoản.
        """
        AccPageWindow.setObjectName("AccPageWindow")
        AccPageWindow.resize(1944, 1227)
        AccPageWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        AccPageWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(AccPageWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QFrame(self.centralwidget)
        self.header.setMaximumSize(QtCore.QSize(16777215, 100))
        self.header.setStyleSheet("")
        self.header.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")
        self.headerLayout = QtWidgets.QHBoxLayout(self.header)
        self.headerLayout.setContentsMargins(10, 10, 10, 10)
        self.headerLayout.setSpacing(10)
        self.headerLayout.setObjectName("headerLayout")
        self.frame_logo = QtWidgets.QFrame(self.header)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_logo.sizePolicy().hasHeightForWidth())
        self.frame_logo.setSizePolicy(sizePolicy)
        self.frame_logo.setMaximumSize(QtCore.QSize(100, 100))
        self.frame_logo.setStyleSheet("")
        self.frame_logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_logo.setObjectName("frame_logo")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_logo)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.logo = QtWidgets.QLabel(self.frame_logo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMaximumSize(QtCore.QSize(80, 80))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("pic\logo\Logo-light_mode.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.horizontalLayout_8.addWidget(self.logo)
        self.headerLayout.addWidget(self.frame_logo)
        self.search_track = QtWidgets.QFrame(self.header)
        self.search_track.setStyleSheet("")
        self.search_track.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.search_track.setFrameShadow(QtWidgets.QFrame.Raised)
        self.search_track.setObjectName("search_track")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.search_track)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.name_logo = QtWidgets.QFrame(self.search_track)
        self.name_logo.setMaximumSize(QtCore.QSize(180, 16777215))
        self.name_logo.setStyleSheet("")
        self.name_logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.name_logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.name_logo.setObjectName("name_logo")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.name_logo)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.watefeel = QtWidgets.QPushButton(self.name_logo)
        self.watefeel.setStyleSheet("color: rgb(0, 0, 0);\n"
"border:none;\n"
"font: 75 20pt \"Playfair Display\";")
        self.watefeel.setObjectName("watefeel")
        self.horizontalLayout_3.addWidget(self.watefeel)
        self.horizontalLayout.addWidget(self.name_logo)
        self.frame_7 = QtWidgets.QFrame(self.search_track)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout.addWidget(self.frame_7)
        self.searches_place = QtWidgets.QFrame(self.search_track)
        self.searches_place.setMaximumSize(QtCore.QSize(950, 200))
        self.searches_place.setStyleSheet("")
        self.searches_place.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.searches_place.setFrameShadow(QtWidgets.QFrame.Raised)
        self.searches_place.setObjectName("searches_place")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.searches_place)
        self.horizontalLayout_2.setContentsMargins(0, 5, 0, 5)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.searches_place)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(900, 16777215))
        self.lineEdit_2.setStyleSheet("background-color: rgb(214, 214, 214);\n"
"border-radius: 20px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setPlaceholderText("Enter tracks")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.horizontalLayout.addWidget(self.searches_place)
        self.frame_8 = QtWidgets.QFrame(self.search_track)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(40)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame_2 = QtWidgets.QFrame(self.frame_8)
        self.frame_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_9.addWidget(self.frame_2)
        self.mode = QtWidgets.QPushButton(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mode.sizePolicy().hasHeightForWidth())
        self.mode.setSizePolicy(sizePolicy)
        self.mode.setMaximumSize(QtCore.QSize(150, 16777215))
        self.mode.setStyleSheet("background-color: rgb(238, 238, 238); border:none;")
        self.mode.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("pic\lightdarkmode\light-mode-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mode.setIcon(icon)
        self.mode.setIconSize(QtCore.QSize(110, 100))
        self.mode.setObjectName("mode")
        self.horizontalLayout_9.addWidget(self.mode)
        self.horizontalLayout.addWidget(self.frame_8)
        self.headerLayout.addWidget(self.search_track)
        self.accounts_option = QtWidgets.QFrame(self.header)
        self.accounts_option.setMaximumSize(QtCore.QSize(200, 100))
        self.accounts_option.setStyleSheet("")
        self.accounts_option.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.accounts_option.setFrameShadow(QtWidgets.QFrame.Raised)
        self.accounts_option.setObjectName("accounts_option")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.accounts_option)
        self.horizontalLayout_4.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.comboBox = QtWidgets.QComboBox(self.accounts_option)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMaximumSize(QtCore.QSize(16777215, 60))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 9pt \"Playfair Display\";\n"
"border: 2px solid black;")
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setEditable(False)
        self.horizontalLayout_4.addWidget(self.comboBox)
        self.headerLayout.addWidget(self.accounts_option)
        self.verticalLayout.addWidget(self.header)
        self.content = QtWidgets.QFrame(self.centralwidget)
        self.content.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.content.setStyleSheet("border:none;")
        self.content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.contentLayout = QtWidgets.QHBoxLayout(self.content)
        self.contentLayout.setContentsMargins(10, 0, 10, 0)
        self.contentLayout.setSpacing(5)
        self.contentLayout.setObjectName("contentLayout")
        self.search_playlist = QtWidgets.QFrame(self.content)
        self.search_playlist.setMaximumSize(QtCore.QSize(300, 16777215))
        self.search_playlist.setStyleSheet("border: 2px solid black;\nborder-radius: 15px;\nbackground-color: rgb(255, 255, 255);")
        self.search_playlist.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.search_playlist.setFrameShadow(QtWidgets.QFrame.Raised)
        self.search_playlist.setObjectName("search_playlist")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.search_playlist)
        self.verticalLayout_2.setContentsMargins(0, 10, 0, 0)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.search_playlists = QtWidgets.QFrame(self.search_playlist)
        self.search_playlists.setMaximumSize(QtCore.QSize(16777215, 50))
        self.search_playlists.setStyleSheet("border:none;")
        self.search_playlists.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.search_playlists.setFrameShadow(QtWidgets.QFrame.Raised)
        self.search_playlists.setObjectName("search_playlists")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.search_playlists)
        self.horizontalLayout_7.setContentsMargins(10, 15, 10, 5)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lineEdit = QtWidgets.QLineEdit(self.search_playlists)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setStyleSheet("border: 2px solid black;\n"
"border-radius: 10px;\nbackground-color: rgb(214, 214, 214);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("Enter Playlists")
        self.horizontalLayout_7.addWidget(self.lineEdit)
        self.verticalLayout_2.addWidget(self.search_playlists)
        self.playlists = QtWidgets.QFrame(self.search_playlist)
        self.playlists.setStyleSheet("border: none;")
        self.playlists.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.playlists.setFrameShadow(QtWidgets.QFrame.Raised)
        self.playlists.setObjectName("playlists")
        self.gridLayout = QtWidgets.QGridLayout(self.playlists)
        self.gridLayout.setContentsMargins(0, 4, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea_artist = QtWidgets.QScrollArea(self.playlists)
        self.scrollArea_artist.setStyleSheet("")
        self.scrollArea_artist.setWidgetResizable(True)
        self.scrollArea_artist.setObjectName("scrollArea_artist")
        self.scrollAreaPlaylistContents = QtWidgets.QWidget()
        self.scrollAreaPlaylistContents.setGeometry(QtCore.QRect(0, 0, 298, 941))
        self.scrollAreaPlaylistContents.setObjectName("scrollAreaPlaylistContents")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaPlaylistContents)
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        db = Database()
        _translate = QtCore.QCoreApplication.translate
        
# show playlists
        playlist = db.query("SELECT * FROM playlist")
        for i in range (len(playlist)):
                self.playlist = QtWidgets.QFrame(self.scrollAreaPlaylistContents)
                self.playlist.setMaximumSize(QtCore.QSize(16777215, 80))
                self.playlist.setStyleSheet("border: 2px solid black;\n"
"border-radius: 20px;")
                self.playlist.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.playlist.setFrameShadow(QtWidgets.QFrame.Raised)
                self.playlist.setObjectName("playlist")
                self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.playlist)
                self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_10.setSpacing(0)
                self.horizontalLayout_10.setObjectName("horizontalLayout_10")
                self.artist_img = QtWidgets.QFrame(self.playlist)
                self.artist_img.setMaximumSize(QtCore.QSize(90, 16777215))
                self.artist_img.setStyleSheet("border:none;")
                self.artist_img.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.artist_img.setFrameShadow(QtWidgets.QFrame.Raised)
                self.artist_img.setObjectName("artist_img")
                self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.artist_img)
                self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_17.setSpacing(0)
                self.horizontalLayout_17.setObjectName("horizontalLayout_17")
                self.playlist_btn = QtWidgets.QPushButton(self.artist_img)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.playlist_btn.sizePolicy().hasHeightForWidth())
                self.playlist_btn.setSizePolicy(sizePolicy)
                self.playlist_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
                self.playlist_btn.setStyleSheet("")
                self.playlist_btn.setText("")
                icon1 = QtGui.QIcon()
                playlist_img_url = "pic\playlist_img\\" + str(i+1) + ".jpg"
                icon1.addPixmap(QtGui.QPixmap(playlist_img_url), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.playlist_btn.setIcon(icon1)
                self.playlist_btn.setIconSize(QtCore.QSize(60, 60))
                self.playlist_btn.setObjectName("playlist_1_btn")
                self.horizontalLayout_17.addWidget(self.playlist_btn)
                self.horizontalLayout_10.addWidget(self.artist_img)
                self.artist_name = QtWidgets.QFrame(self.playlist)
                self.artist_name.setStyleSheet("border:none;")
                self.artist_name.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.artist_name.setFrameShadow(QtWidgets.QFrame.Raised)
                self.artist_name.setObjectName("artist_name_1")
                self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.artist_name)
                self.horizontalLayout_16.setContentsMargins(20, 0, 0, 0)
                self.horizontalLayout_16.setSpacing(0)
                self.horizontalLayout_16.setObjectName("horizontalLayout_16")
                self.playlist_name = QtWidgets.QLabel(self.artist_name)
                self.playlist_name.setStyleSheet("font: 75 bold 12pt \"Playfair Display\"; \n"
"border:none;")
                self.playlist_name.setObjectName("playlist_name_1")
                self.horizontalLayout_16.addWidget(self.playlist_name)
                self.horizontalLayout_10.addWidget(self.artist_name)
                self.verticalLayout_6.addWidget(self.playlist)
                self.playlist_name.setText(_translate("AccPageWindow", playlist[i]['title']))

        self.emp_frame_6 = QtWidgets.QFrame(self.scrollAreaPlaylistContents)
        self.emp_frame_6.setStyleSheet("border:none;")
        self.emp_frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.emp_frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.emp_frame_6.setObjectName("emp_frame_6")
        self.verticalLayout_6.addWidget(self.emp_frame_6)
        self.scrollArea_artist.setWidget(self.scrollAreaPlaylistContents)
#Playlists_show_details

#Options_apps
        #show tracks_all
        self.scrollAreaAllTrack = QtWidgets.QWidget()
        self.scrollAreaAllTrack.setGeometry(QtCore.QRect(0, 0, 1632, 928))
        self.scrollAreaAllTrack.setStyleSheet("")
        self.scrollAreaAllTrack.setObjectName("scrollAreaTrackContents_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.scrollAreaAllTrack)
        self.verticalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.track_lists_types = QtWidgets.QFrame(self.content)
        self.track_lists_types.setStyleSheet("border:2px solid black;\nborder-radius:15px;\nbackground-color: rgb(255, 255, 255);")
        self.track_lists_types.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.track_lists_types.setFrameShadow(QtWidgets.QFrame.Raised)
        self.track_lists_types.setObjectName("track_lists_types")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.track_lists_types)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(14)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.contentLayout.addWidget(self.search_playlist)
        self.contentLayout.addWidget(self.track_lists_types)
        self.verticalLayout.addWidget(self.content)
        self.options = QtWidgets.QFrame(self.track_lists_types)
        self.tracks = QtWidgets.QGroupBox(self.track_lists_types)
        self.tracks.setStyleSheet("border:none;")
        self.tracks.setObjectName("tracks")
        self.verticalLayout_3.addWidget(self.options)
        self.verticalLayout_3.addWidget(self.tracks)
        self.scrollArea_AllTrack = QtWidgets.QScrollArea(self.tracks)
        self.scrollArea_AllTrack.setGeometry(3, 0, 1600, 911)
        self.scrollArea_AllTrack.setStyleSheet("border:none;")
        self.scrollArea_AllTrack.setWidgetResizable(True)
        self.scrollArea_AllTrack.setObjectName("scrollArea_tracks")
        self.scrollArea_AllTrack.setWidget(self.scrollAreaAllTrack)
        
        self.buttons = []
        artist = db.query("SELECT * FROM track")
        for i in range (len(artist)):
                self.frame_track = QtWidgets.QFrame(self.scrollAreaAllTrack)
                self.frame_track.setMaximumSize(QtCore.QSize(16777215, 80))
                self.frame_track.setStyleSheet("border: 2px solid black;\nborder-radius: 10px;")
                self.frame_track.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_track.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_track.setObjectName("frame_track")
                self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.frame_track)
                self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_22.setSpacing(0)
                self.horizontalLayout_22.setObjectName("horizontalLayout_22")
                self.play_pause_track_all = QtWidgets.QGroupBox(self.frame_track)
                self.play_pause_track_all.setMaximumSize(QtCore.QSize(50, 16777215))
                self.play_pause_track_all.setStyleSheet("border:none;")
                self.play_pause_track_all.setObjectName("play_pause_track_all")

                self.playtrack = QtWidgets.QPushButton(self.play_pause_track_all)
                self.playtrack.setGeometry(QtCore.QRect(0, 10, 51, 41))
                self.playtrack.setStyleSheet("border:none;")
                self.playtrack.setText("")
                icon4 = QtGui.QIcon()
                icon4.addPixmap(QtGui.QPixmap("pic\musicplayertab\playTrack.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.playtrack.setIcon(icon4)
                self.playtrack.setObjectName("playtrack")
                self.pausetrack = QtWidgets.QPushButton(self.play_pause_track_all)
                self.pausetrack.setGeometry(QtCore.QRect(0, 10, 51, 41))
                self.pausetrack.setStyleSheet("border:none;")
                self.pausetrack.setText("")

                self.pausetrack.hide()

                self.buttons.append(self.playtrack)
                self.buttons.append(self.pausetrack)
                self.playtrack.clicked.connect(self.play)
                self.pausetrack.clicked.connect(self.pause)
                icon5 = QtGui.QIcon()
                icon5.addPixmap(QtGui.QPixmap("pic\musicplayertab\pauseTrack.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.pausetrack.setIcon(icon5)
                self.pausetrack.setObjectName("pausetrack")
                self.horizontalLayout_22.addWidget(self.play_pause_track_all)
                self.frame_img = QtWidgets.QFrame(self.frame_track)
                self.frame_img.setMaximumSize(QtCore.QSize(100, 16777215))
                self.frame_img.setStyleSheet("border:none;")
                self.frame_img.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_img.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_img.setObjectName("frame_img")
                self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.frame_img)
                self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_23.setSpacing(0)
                self.horizontalLayout_23.setObjectName("horizontalLayout_23")
                self.label = QtWidgets.QLabel(self.frame_img)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
                self.label.setSizePolicy(sizePolicy)
                self.label.setMaximumSize(QtCore.QSize(60, 60))
                self.label.setText("")
                track_img_url = "pic\\track_img\\" + str(i+1) + ".jpg"
                self.label.setPixmap(QtGui.QPixmap(track_img_url))
                self.label.setScaledContents(True)
                self.label.setObjectName("label")
                self.horizontalLayout_23.addWidget(self.label)
                self.horizontalLayout_22.addWidget(self.frame_img)
                self.frame_trackname = QtWidgets.QFrame(self.frame_track)
                self.frame_trackname.setStyleSheet("border:none;")
                self.frame_trackname.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_trackname.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_trackname.setObjectName("frame_trackname_1")
                self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.frame_trackname)
                self.horizontalLayout_24.setContentsMargins(20, 0, 0, 0)
                self.horizontalLayout_24.setSpacing(0)
                self.horizontalLayout_24.setObjectName("horizontalLayout_24")
                self.track_nameplace = QtWidgets.QLabel(self.frame_trackname)
                self.track_nameplace.setStyleSheet("font: 75 bold 12pt \"Playfair Display\"; \n"
"border:none;")
                self.track_nameplace.setObjectName("track_nameplace")
                self.horizontalLayout_24.addWidget(self.track_nameplace)
                self.horizontalLayout_22.addWidget(self.frame_trackname)
                self.frame_durationtrack = QtWidgets.QFrame(self.frame_track)
                self.frame_durationtrack.setMaximumSize(QtCore.QSize(100, 16777215))
                self.frame_durationtrack.setStyleSheet("border:none;")
                self.frame_durationtrack.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_durationtrack.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_durationtrack.setObjectName("frame_durationtrack")
                self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.frame_durationtrack)
                self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout_25.setSpacing(0)
                self.horizontalLayout_25.setObjectName("horizontalLayout_25")
                self.duration_track = QtWidgets.QLabel(self.frame_durationtrack)
                self.duration_track.setStyleSheet("font: 75 12pt \"Arial\"; \n"
"border:none;")
                self.duration_track.setObjectName("duration_track")
                self.horizontalLayout_25.addWidget(self.duration_track)
                self.horizontalLayout_22.addWidget(self.frame_durationtrack)
                self.verticalLayout_7.addWidget(self.frame_track)
                self.track_nameplace.setText(_translate("AccPageWindow", artist[i]['track_name']))
                self.duration_track.setText(_translate("AccPageWindow", str(artist[i]['duration'])))
        self.emp_frame_9 = QtWidgets.QFrame(self.scrollAreaAllTrack)
        self.emp_frame_9.setStyleSheet("border:none;")
        self.emp_frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.emp_frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.emp_frame_9.setObjectName("emp_frame_9")
        self.verticalLayout_7.addWidget(self.emp_frame_9)

        #Recommend tracks
        self.scrollAreaRecommendTrack = QtWidgets.QWidget()
        self.scrollAreaRecommendTrack.setGeometry(QtCore.QRect(0, 0, 1632, 928))
        self.scrollAreaRecommendTrack.setStyleSheet("")
        self.scrollAreaRecommendTrack.setObjectName("scrollAreaRecommendTrack")
        self.verticalLayout_recomTrack = QtWidgets.QVBoxLayout(self.scrollAreaRecommendTrack)
        self.verticalLayout_recomTrack.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout_recomTrack.setSpacing(5)
        self.verticalLayout_recomTrack.setObjectName("verticalLayout_recomTrack")
        
        self.recom_buttons = []
        recommend = db.query("SELECT * FROM track")
        self.scrollArea_RecommendTrack = QtWidgets.QScrollArea(self.tracks)
        self.scrollArea_RecommendTrack.setStyleSheet("border:none;")
        self.scrollArea_RecommendTrack.setGeometry(3, 0, 1600, 911)
        self.scrollArea_RecommendTrack.setWidgetResizable(True)
        self.scrollArea_RecommendTrack.setObjectName("scrollArea_tracks")
        self.scrollArea_RecommendTrack.setWidget(self.scrollAreaRecommendTrack)
        for i in range (len(recommend)//2):
                self.frame_recomTrack = QtWidgets.QFrame(self.scrollAreaRecommendTrack)
                self.frame_recomTrack.setMaximumSize(QtCore.QSize(16777215, 80))
                self.frame_recomTrack.setStyleSheet("border: 2px solid black;\nborder-radius: 10px;")
                self.frame_recomTrack.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_recomTrack.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_recomTrack.setObjectName("frame_recomTrack")
                self.horizontalrecomTrackLayout = QtWidgets.QHBoxLayout(self.frame_recomTrack)
                self.horizontalrecomTrackLayout.setContentsMargins(0, 0, 0, 0)
                self.horizontalrecomTrackLayout.setSpacing(0)
                self.horizontalrecomTrackLayout.setObjectName("horizontalrecomTrackLayout")
                self.recomplay_pause_track_all = QtWidgets.QGroupBox(self.frame_recomTrack)
                self.recomplay_pause_track_all.setMaximumSize(QtCore.QSize(50, 16777215))
                self.recomplay_pause_track_all.setStyleSheet("border:none;")
                self.recomplay_pause_track_all.setObjectName("recomplay_pause_track_all")

                self.playtrack = QtWidgets.QPushButton(self.recomplay_pause_track_all)
                self.playtrack.setGeometry(QtCore.QRect(0, 10, 51, 41))
                self.playtrack.setStyleSheet("border:none;")
                self.playtrack.setText("")
                icon4 = QtGui.QIcon()
                icon4.addPixmap(QtGui.QPixmap("pic\musicplayertab\playTrack.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.playtrack.setIcon(icon4)
                self.playtrack.setObjectName("playtrack")
                self.pausetrack = QtWidgets.QPushButton(self.recomplay_pause_track_all)
                self.pausetrack.setGeometry(QtCore.QRect(0, 10, 51, 41))
                self.pausetrack.setStyleSheet("border:none;")
                self.pausetrack.setText("")

                self.pausetrack.hide()

                self.recom_buttons.append(self.playtrack)
                self.recom_buttons.append(self.pausetrack)
                self.playtrack.clicked.connect(self.recom_play)
                self.pausetrack.clicked.connect(self.recom_pause)
                icon5 = QtGui.QIcon()
                icon5.addPixmap(QtGui.QPixmap("pic\musicplayertab\pauseTrack.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.pausetrack.setIcon(icon5)
                self.pausetrack.setObjectName("pausetrack")
                self.horizontalrecomTrackLayout.addWidget(self.recomplay_pause_track_all)
                self.frame_recomImg = QtWidgets.QFrame(self.frame_recomTrack)
                self.frame_recomImg.setMaximumSize(QtCore.QSize(100, 16777215))
                self.frame_recomImg.setStyleSheet("border:none;")
                self.frame_recomImg.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_recomImg.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_recomImg.setObjectName("frame_recomImg")
                self.recom_label = QtWidgets.QLabel(self.frame_recomImg)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.recom_label.sizePolicy().hasHeightForWidth())
                self.recom_label.setSizePolicy(sizePolicy)
                self.recom_label.setMaximumSize(QtCore.QSize(60, 60))
                self.recom_label.setText("")
                track_img_url = "pic\\track_img\\" + str(i+1) + ".jpg"
                self.recom_label.setPixmap(QtGui.QPixmap(track_img_url))
                self.recom_label.setScaledContents(True)
                self.recom_label.setObjectName("recom_label")

                self.horizontalrecomLabelLayout = QtWidgets.QHBoxLayout(self.frame_recomImg)
                self.horizontalrecomLabelLayout.setContentsMargins(0, 0, 0, 0)
                self.horizontalrecomLabelLayout.setSpacing(0)
                self.horizontalrecomLabelLayout.setObjectName("horizontalLayout_23")
                self.horizontalrecomLabelLayout.addWidget(self.recom_label)
                self.horizontalrecomTrackLayout.addWidget(self.frame_recomImg)

                self.frame_recomTrackname = QtWidgets.QFrame(self.frame_recomTrack)
                self.frame_recomTrackname.setStyleSheet("border:none;")
                self.frame_recomTrackname.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_recomTrackname.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_recomTrackname.setObjectName("frame_recomtrackname")
                self.horizontalrecomTrackLayout_3 = QtWidgets.QHBoxLayout(self.frame_recomTrackname)
                self.horizontalrecomTrackLayout_3.setContentsMargins(20, 0, 0, 0)
                self.horizontalrecomTrackLayout_3.setSpacing(0)
                self.horizontalrecomTrackLayout_3.setObjectName("horizontalrecomTrackLayout_3")
                self.recomtrack_nameplace = QtWidgets.QLabel(self.frame_recomTrackname)
                self.recomtrack_nameplace.setStyleSheet("font: 75 bold 12pt \"Playfair Display\"; \n"
"border:none;")
                self.recomtrack_nameplace.setObjectName("recomtrack_nameplace")
                self.horizontalrecomTrackLayout_3.addWidget(self.recomtrack_nameplace)
                self.horizontalrecomTrackLayout.addWidget(self.frame_recomTrackname)
                self.frame_recomdurationtrack = QtWidgets.QFrame(self.frame_recomTrack)
                self.frame_recomdurationtrack.setMaximumSize(QtCore.QSize(100, 16777215))
                self.frame_recomdurationtrack.setStyleSheet("border:none;")
                self.frame_recomdurationtrack.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_recomdurationtrack.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_recomdurationtrack.setObjectName("frame_recomdurationtrack")
                self.horizontalrecomTrackLayout_4 = QtWidgets.QHBoxLayout(self.frame_recomdurationtrack)
                self.horizontalrecomTrackLayout_4.setContentsMargins(0, 0, 0, 0)
                self.horizontalrecomTrackLayout_4.setSpacing(0)
                self.horizontalrecomTrackLayout_4.setObjectName("horizontalrecomTrackLayout_4")
                self.recomduration_track = QtWidgets.QLabel(self.frame_recomdurationtrack)
                self.recomduration_track.setStyleSheet("font: 75 12pt \"Arial\"; \n"
"border:none;")
                self.recomduration_track.setObjectName("recomduration_track")
                self.horizontalrecomTrackLayout_4.addWidget(self.recomduration_track)
                self.horizontalrecomTrackLayout.addWidget(self.frame_recomdurationtrack)
                self.verticalLayout_recomTrack.addWidget(self.frame_recomTrack)
                self.recomtrack_nameplace.setText(_translate("AccPageWindow", artist[i]['track_name']))
                self.recomduration_track.setText(_translate("AccPageWindow", str(artist[i]['duration'])))
        self.emp_frame_recom = QtWidgets.QFrame(self.scrollAreaRecommendTrack)
        self.emp_frame_recom.setStyleSheet("border:none;")
        self.emp_frame_recom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.emp_frame_recom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.emp_frame_recom.setObjectName("emp_frame_recom")
        self.verticalLayout_recomTrack.addWidget(self.emp_frame_recom)
        
        #Top Liked Track
        self.scrollAreaTopLikeTrack = QtWidgets.QWidget()
        self.scrollAreaTopLikeTrack.setGeometry(QtCore.QRect(0, 0, 1632, 928))
        self.scrollAreaTopLikeTrack.setStyleSheet("")
        self.scrollAreaTopLikeTrack.setObjectName("scrollAreaTopLikeTrack")
        self.verticalLayout_TopLikeTrack = QtWidgets.QVBoxLayout(self.scrollAreaTopLikeTrack)
        self.verticalLayout_TopLikeTrack.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout_TopLikeTrack.setSpacing(5)
        self.verticalLayout_TopLikeTrack.setObjectName("verticalLayout_TopLikeTrack")
        
        self.TopLike_buttons = []
        toplike = db.query("SELECT * FROM track")
        self.scrollArea_TopLikeTrack = QtWidgets.QScrollArea(self.tracks)
        self.scrollArea_TopLikeTrack.setStyleSheet("border:none;")
        self.scrollArea_TopLikeTrack.setGeometry(3, 0, 1600, 911)
        self.scrollArea_TopLikeTrack.setWidgetResizable(True)
        self.scrollArea_TopLikeTrack.setObjectName("scrollArea_TopLiketracks")
        self.scrollArea_TopLikeTrack.setWidget(self.scrollAreaTopLikeTrack)
        for i in range (len(toplike)//2):
                self.frame_TopLikeTrack = QtWidgets.QFrame(self.scrollAreaTopLikeTrack)
                self.frame_TopLikeTrack.setMaximumSize(QtCore.QSize(16777215, 80))
                self.frame_TopLikeTrack.setStyleSheet("border: 2px solid black;\nborder-radius: 10px;")
                self.frame_TopLikeTrack.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_TopLikeTrack.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_TopLikeTrack.setObjectName("frame_TopLikeTrack")
                self.horizontalTopLikeTrackLayout = QtWidgets.QHBoxLayout(self.frame_TopLikeTrack)
                self.horizontalTopLikeTrackLayout.setContentsMargins(0, 0, 0, 0)
                self.horizontalTopLikeTrackLayout.setSpacing(0)
                self.horizontalTopLikeTrackLayout.setObjectName("horizontalrecomTrackLayout")
                self.TopLikeplay_pause_track_all = QtWidgets.QGroupBox(self.frame_TopLikeTrack)
                self.TopLikeplay_pause_track_all.setMaximumSize(QtCore.QSize(50, 16777215))
                self.TopLikeplay_pause_track_all.setStyleSheet("border:none;")
                self.TopLikeplay_pause_track_all.setObjectName("TopLikeplay_pause_track_all")

                self.playtrack = QtWidgets.QPushButton(self.TopLikeplay_pause_track_all)
                self.playtrack.setGeometry(QtCore.QRect(0, 10, 51, 41))
                self.playtrack.setStyleSheet("border:none;")
                self.playtrack.setText("")
                icon4 = QtGui.QIcon()
                icon4.addPixmap(QtGui.QPixmap("pic\musicplayertab\playTrack.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.playtrack.setIcon(icon4)
                self.playtrack.setObjectName("playtrack")
                self.pausetrack = QtWidgets.QPushButton(self.TopLikeplay_pause_track_all)
                self.pausetrack.setGeometry(QtCore.QRect(0, 10, 51, 41))
                self.pausetrack.setStyleSheet("border:none;")
                self.pausetrack.setText("")

                self.pausetrack.hide()

                self.TopLike_buttons.append(self.playtrack)
                self.TopLike_buttons.append(self.pausetrack)
                self.playtrack.clicked.connect(self.TopLike_play)
                self.pausetrack.clicked.connect(self.TopLike_pause)
                icon5 = QtGui.QIcon()
                icon5.addPixmap(QtGui.QPixmap("pic\musicplayertab\pauseTrack.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.pausetrack.setIcon(icon5)
                self.pausetrack.setObjectName("pausetrack")
                self.horizontalTopLikeTrackLayout.addWidget(self.TopLikeplay_pause_track_all)
                self.frame_TopLikeImg = QtWidgets.QFrame(self.frame_TopLikeTrack)
                self.frame_TopLikeImg.setMaximumSize(QtCore.QSize(100, 16777215))
                self.frame_TopLikeImg.setStyleSheet("border:none;")
                self.frame_TopLikeImg.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_TopLikeImg.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_TopLikeImg.setObjectName("frame_TopLikeImg")
                self.TopLike_label = QtWidgets.QLabel(self.frame_TopLikeImg)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.TopLike_label.sizePolicy().hasHeightForWidth())
                self.TopLike_label.setSizePolicy(sizePolicy)
                self.TopLike_label.setMaximumSize(QtCore.QSize(60, 60))
                self.TopLike_label.setText("")
                track_img_url = "pic\\track_img\\" + str(i+1) + ".jpg"
                self.TopLike_label.setPixmap(QtGui.QPixmap(track_img_url))
                self.TopLike_label.setScaledContents(True)
                self.TopLike_label.setObjectName("TopLike_label")

                self.horizontalTopLikeLabelLayout = QtWidgets.QHBoxLayout(self.frame_TopLikeImg)
                self.horizontalTopLikeLabelLayout.setContentsMargins(0, 0, 0, 0)
                self.horizontalTopLikeLabelLayout.setSpacing(0)
                self.horizontalTopLikeLabelLayout.setObjectName("horizontalLayout_23")
                self.horizontalTopLikeLabelLayout.addWidget(self.recom_label)
                self.horizontalTopLikeTrackLayout.addWidget(self.frame_TopLikeImg)

                self.frame_TopLikeTrackname = QtWidgets.QFrame(self.frame_TopLikeTrack)
                self.frame_TopLikeTrackname.setStyleSheet("border:none;")
                self.frame_TopLikeTrackname.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_TopLikeTrackname.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_TopLikeTrackname.setObjectName("frame_TopLikeTrackname")
                self.horizontalTopLikeTrackLayout_3 = QtWidgets.QHBoxLayout(self.frame_TopLikeTrackname)
                self.horizontalTopLikeTrackLayout_3.setContentsMargins(20, 0, 0, 0)
                self.horizontalTopLikeTrackLayout_3.setSpacing(0)
                self.horizontalTopLikeTrackLayout_3.setObjectName("horizontalTopLikeTrackLayout_3")
                self.TopLiketrack_nameplace = QtWidgets.QLabel(self.frame_TopLikeTrackname)
                self.TopLiketrack_nameplace.setStyleSheet("font: 75 bold 12pt \"Playfair Display\"; \n"
"border:none;")
                self.TopLiketrack_nameplace.setObjectName("TopLiketrack_nameplace")
                self.horizontalTopLikeTrackLayout_3.addWidget(self.TopLiketrack_nameplace)
                self.horizontalTopLikeTrackLayout.addWidget(self.frame_TopLikeTrackname)
                self.frame_TopLikedurationtrack = QtWidgets.QFrame(self.frame_TopLikeTrack)
                self.frame_TopLikedurationtrack.setMaximumSize(QtCore.QSize(100, 16777215))
                self.frame_TopLikedurationtrack.setStyleSheet("border:none;")
                self.frame_TopLikedurationtrack.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_TopLikedurationtrack.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_TopLikedurationtrack.setObjectName("frame_TopLikedurationtrack")
                self.horizontalTopLikeTrackLayout_4 = QtWidgets.QHBoxLayout(self.frame_TopLikedurationtrack)
                self.horizontalTopLikeTrackLayout_4.setContentsMargins(0, 0, 0, 0)
                self.horizontalTopLikeTrackLayout_4.setSpacing(0)
                self.horizontalTopLikeTrackLayout_4.setObjectName("horizontalTopLikeTrackLayout_4")
                self.TopLikeduration_track = QtWidgets.QLabel(self.frame_TopLikedurationtrack)
                self.TopLikeduration_track.setStyleSheet("font: 75 12pt \"Arial\"; \n"
"border:none;")
                self.TopLikeduration_track.setObjectName("TopLikeduration_track")
                self.horizontalTopLikeTrackLayout_4.addWidget(self.TopLikeduration_track)
                self.horizontalTopLikeTrackLayout.addWidget(self.frame_TopLikedurationtrack)
                self.verticalLayout_TopLikeTrack.addWidget(self.frame_TopLikeTrack)
                self.TopLiketrack_nameplace.setText(_translate("AccPageWindow", artist[i]['track_name']))
                self.TopLikeduration_track.setText(_translate("AccPageWindow", str(artist[i]['duration'])))
        self.emp_frame_TopLike = QtWidgets.QFrame(self.scrollAreaTopLikeTrack)
        self.emp_frame_TopLike.setStyleSheet("border:none;")
        self.emp_frame_TopLike.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.emp_frame_TopLike.setFrameShadow(QtWidgets.QFrame.Raised)
        self.emp_frame_TopLike.setObjectName("emp_frame_TopLike")
        self.verticalLayout_TopLikeTrack.addWidget(self.emp_frame_TopLike)        

        self.scrollArea_AllTrack.show()
        self.scrollArea_RecommendTrack.hide()
        self.scrollArea_TopLikeTrack.hide()

        self.gridLayout.addWidget(self.scrollArea_artist, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.playlists)
        self.options.setMaximumSize(QtCore.QSize(16777215, 73))
        self.options.setStyleSheet("border:none;")
        self.options.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.options.setFrameShadow(QtWidgets.QFrame.Raised)
        self.options.setObjectName("options")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.options)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_option = QtWidgets.QFrame(self.options)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_option.sizePolicy().hasHeightForWidth())
        self.frame_option.setSizePolicy(sizePolicy)
        self.frame_option.setMaximumSize(QtCore.QSize(920, 60))
        self.frame_option.setStyleSheet("border:none;")
        self.frame_option.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_option.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_option.setObjectName("frame_option")

        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_option)
        self.horizontalLayout_6.setContentsMargins(100, 8, 0, 0)
        self.horizontalLayout_6.setSpacing(30)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.all = QtWidgets.QPushButton(self.frame_option)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.all.sizePolicy().hasHeightForWidth())
        self.all.setSizePolicy(sizePolicy)
        self.all.setStyleSheet("#all {\n"
"    background-color:rgb(189, 161, 140);\n"
"    font: 75 10pt \"Tahoma\";\n"
"    border: none;\n"
"}\n"
"\n"
"#all:hover {\n"
"    background-color: rgb(80, 0, 0);\n"
"    font: 75 10pt \"Tahoma\";\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"")
        self.all.setObjectName("all")
        self.horizontalLayout_6.addWidget(self.all)
        self.recommend = QtWidgets.QPushButton(self.frame_option)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recommend.sizePolicy().hasHeightForWidth())
        self.recommend.setSizePolicy(sizePolicy)
        self.recommend.setStyleSheet("#recommend {\n"
"    background-color:rgb(189, 161, 140);\n"
"    font: 75 10pt \"Tahoma\";\n"
"    border: none;\n"
"}\n"
"\n"
"#recommend:hover {\n"
"    background-color: rgb(80, 0, 0);\n"
"    font: 75 10pt \"Tahoma\";\n"
"    color: white;\n"
"    border: none;\n"
"}")
        self.recommend.setObjectName("recommend")
        self.horizontalLayout_6.addWidget(self.recommend)
        self.my_playlist = QtWidgets.QPushButton(self.frame_option)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.my_playlist.sizePolicy().hasHeightForWidth())
        self.my_playlist.setSizePolicy(sizePolicy)
        self.my_playlist.setStyleSheet("#my_playlist {\n"
"    background-color:rgb(189, 161, 140);\n"
"    font: 75 10pt \"Tahoma\";\n"
"    border: none;\n"
"}\n"
"\n"
"#my_playlist:hover {\n"
"    	background-color: rgb(80, 0, 0);\n"
"    font: 75 10pt \"Tahoma\";\n"
"    color: white;\n"
"    border: none;\n"
"}")
        self.my_playlist.setObjectName("my_playlist")
        self.horizontalLayout_6.addWidget(self.my_playlist)
        self.album = QtWidgets.QPushButton(self.frame_option)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.album.sizePolicy().hasHeightForWidth())
        self.album.setSizePolicy(sizePolicy)
        self.album.setStyleSheet("#album {\n"
"    background-color:rgb(189, 161, 140);\n"
"    font: 75 10pt \"Tahoma\";\n"
"    border: none;\n"
"}\n"
"\n"
"#album:hover {\n"
"    background-color: rgb(80, 0, 0);\n"
"    font: 75 10pt \"Tahoma\";\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"")
        self.album.setObjectName("album")
        self.horizontalLayout_6.addWidget(self.album)
        self.toplike = QtWidgets.QPushButton(self.frame_option)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toplike.sizePolicy().hasHeightForWidth())
        self.toplike.setSizePolicy(sizePolicy)
        self.toplike.setStyleSheet("#toplike {\n"
"    background-color:rgb(189, 161, 140);\n"
"    font: 75 10pt \"Tahoma\";\n"
"    border: none;\n"
"}\n"
"\n"
"#toplike:hover {\n"
"    background-color: rgb(80, 0, 0);\n"
"    font: 75 10pt \"Tahoma\";\n"
"    color: white;\n"
"    border: none;\n"
"}\n"
"")
        self.toplike.setObjectName("toplike")
        self.horizontalLayout_6.addWidget(self.toplike)
        self.seasons = QtWidgets.QPushButton(self.frame_option)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.seasons.sizePolicy().hasHeightForWidth())
        self.seasons.setSizePolicy(sizePolicy)
        self.seasons.setStyleSheet("#seasons {\n"
"    background-color:rgb(189, 161, 140);\n"
"    font: 75 10pt \"Tahoma\";\n"
"    border: none;\n"
"}\n"
"\n"
"#seasons:hover {\n"
"   background-color: rgb(80, 0, 0);\n"
"   font: 75 10pt \"Playfair Display\";\n"
"   color: white;\n"
"   border: none;\n"
"}\n"
"")
        self.seasons.setObjectName("seasons")
        self.horizontalLayout_6.addWidget(self.seasons)
        self.horizontalLayout_5.addWidget(self.frame_option)
        self.frame_3 = QtWidgets.QFrame(self.options)
        self.frame_3.setStyleSheet("border:none;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_5.addWidget(self.frame_3)
        self.musicplayer_icon = QtWidgets.QFrame(self.centralwidget)
        self.musicplayer_icon.setMaximumSize(QtCore.QSize(16777215, 110))
        self.musicplayer_icon.setSizeIncrement(QtCore.QSize(0, 0))
        self.musicplayer_icon.setStyleSheet("")
        self.musicplayer_icon.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.musicplayer_icon.setFrameShadow(QtWidgets.QFrame.Raised)
        self.musicplayer_icon.setObjectName("musicplayer_icon")
        self.musicplayerLayout = QtWidgets.QHBoxLayout(self.musicplayer_icon)
        self.musicplayerLayout.setContentsMargins(10, 5, 10, 5)
        self.musicplayerLayout.setSpacing(5)
        self.musicplayerLayout.setObjectName("musicplayerLayout")
        self.frame = QtWidgets.QFrame(self.musicplayer_icon)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QtCore.QSize(300, 16777215))
        self.frame.setStyleSheet("border: 2px solid black;\n"
"border-radius: 10px;\nbackground-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.track_img = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.track_img.sizePolicy().hasHeightForWidth())
        self.track_img.setSizePolicy(sizePolicy)
        self.track_img.setMaximumSize(QtCore.QSize(80, 80))
        self.track_img.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.track_img.setText("")
        self.track_img.setScaledContents(True)
        self.track_img.setObjectName("track_img")
        self.horizontalLayout_11.addWidget(self.track_img)
        self.track_name = QtWidgets.QLabel(self.frame)
        self.track_name.setStyleSheet("border:none;\n"
"color: black;\n"
"font: 75 10pt \"Playfair Display\";")
        self.track_name.setObjectName("track_name")
        self.horizontalLayout_11.addWidget(self.track_name)
        self.musicplayerLayout.addWidget(self.frame)
        self.frame_musicplayerbtn = QtWidgets.QFrame(self.musicplayer_icon)
        self.frame_musicplayerbtn.setStyleSheet("#frame_musicplayerbtn {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 2px solid black;\n"
"    border-radius: 10px;\n"
"}\n"
"    ")
        self.frame_musicplayerbtn.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_musicplayerbtn.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_musicplayerbtn.setObjectName("frame_musicplayerbtn")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_musicplayerbtn)
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.musicplayer_btn = QtWidgets.QFrame(self.frame_musicplayerbtn)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.musicplayer_btn.sizePolicy().hasHeightForWidth())
        self.musicplayer_btn.setSizePolicy(sizePolicy)
        self.musicplayer_btn.setMaximumSize(QtCore.QSize(16777215, 60))
        self.musicplayer_btn.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.musicplayer_btn.setFrameShadow(QtWidgets.QFrame.Raised)
        self.musicplayer_btn.setObjectName("musicplayer_btn")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.musicplayer_btn)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.frame_4 = QtWidgets.QFrame(self.musicplayer_btn)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.frame_volume = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_volume.sizePolicy().hasHeightForWidth())
        self.frame_volume.setSizePolicy(sizePolicy)
        self.frame_volume.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_volume.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_volume.setObjectName("frame_volume")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_volume)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.volume_text = QtWidgets.QLabel(self.frame_volume)
        self.volume_text.setStyleSheet("font: 75 8pt \"Playfair Display\";")
        self.volume_text.setObjectName("volume_text")
        self.verticalLayout_8.addWidget(self.volume_text)
        self.horizontalLayout_26.addWidget(self.frame_volume)
        self.volume_slider = QtWidgets.QSlider(self.frame_4)
        self.volume_slider.setRange(0, 100)  # Thiết lập phạm vi âm lượng từ 0 đến 100
        self.volume_slider.setValue(50)  # Thiết lập âm lượng ban đầu là 50
        # Kết nối QSlider với hàm điều chỉnh âm lượng
        self.volume_slider.valueChanged.connect(self.change_volume)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.volume_slider.sizePolicy().hasHeightForWidth())
        self.volume_slider.setSizePolicy(sizePolicy)
        self.volume_slider.setOrientation(QtCore.Qt.Horizontal)
        self.volume_slider.setObjectName("volume_slider")
        self.horizontalLayout_26.addWidget(self.volume_slider)
        self.emp_frame_7 = QtWidgets.QFrame(self.frame_4)
        self.emp_frame_7.setMaximumSize(QtCore.QSize(510, 16777215))
        self.emp_frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.emp_frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.emp_frame_7.setObjectName("emp_frame_7")
        self.horizontalLayout_26.addWidget(self.emp_frame_7)
        self.horizontalLayout_13.addWidget(self.frame_4)
        self.player_btn_2 = QtWidgets.QFrame(self.musicplayer_btn)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.player_btn_2.sizePolicy().hasHeightForWidth())
        self.player_btn_2.setSizePolicy(sizePolicy)
        self.player_btn_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.player_btn_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.player_btn_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.player_btn_2.setObjectName("player_btn_2")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.player_btn_2)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.previous_2 = QtWidgets.QPushButton(self.player_btn_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previous_2.sizePolicy().hasHeightForWidth())
        self.previous_2.setSizePolicy(sizePolicy)
        self.previous_2.setStyleSheet("border: none;")
        self.previous_2.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("pic\musicplayertab\\backTrack.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previous_2.setIcon(icon6)
        self.previous_2.setObjectName("previous_2")
        self.horizontalLayout_12.addWidget(self.previous_2)
        self.play_pause_track = QtWidgets.QGroupBox(self.player_btn_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.play_pause_track.sizePolicy().hasHeightForWidth())
        self.play_pause_track.setSizePolicy(sizePolicy)
        self.play_pause_track.setMaximumSize(QtCore.QSize(30, 30))
        self.play_pause_track.setObjectName("play_pause_track")
        self.playtrack_2 = QtWidgets.QPushButton(self.play_pause_track)
        self.playtrack_2.setGeometry(QtCore.QRect(0, 0, 31, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.playtrack_2.sizePolicy().hasHeightForWidth())
        self.playtrack_2.setSizePolicy(sizePolicy)
        self.playtrack_2.setStyleSheet("border: 2px solid grey;\n"
"border-radius: 5px;")
        self.playtrack_2.setText("")
        self.playtrack_2.setIcon(icon4)
        self.playtrack_2.setObjectName("playtrack_2")
        self.pausetrack_2 = QtWidgets.QPushButton(self.play_pause_track)
        self.pausetrack_2.setGeometry(QtCore.QRect(0, 0, 31, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pausetrack_2.sizePolicy().hasHeightForWidth())
        self.pausetrack_2.setSizePolicy(sizePolicy)
        self.pausetrack_2.setStyleSheet("border: 2px solid grey;\n"
"border-radius: 5px;")
        self.pausetrack_2.setText("")
        self.pausetrack_2.setIcon(icon5)
        self.pausetrack_2.setObjectName("pausetrack_2")
        self.horizontalLayout_12.addWidget(self.play_pause_track)

        self.pausetrack_2.hide()
        self.next_2 = QtWidgets.QPushButton(self.player_btn_2)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.next_2.sizePolicy().hasHeightForWidth())
        self.next_2.setSizePolicy(sizePolicy)
        self.next_2.setStyleSheet("border: none;")
        self.next_2.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("pic\musicplayertab\\nextTrack.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next_2.setIcon(icon7)
        self.next_2.setObjectName("next_2")
        self.horizontalLayout_12.addWidget(self.next_2)
        self.liketrack = QtWidgets.QPushButton(self.player_btn_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.liketrack.sizePolicy().hasHeightForWidth())
        self.liketrack.setSizePolicy(sizePolicy)
        self.liketrack.setStyleSheet("border:none;")
        self.liketrack.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("pic\musicplayertab\like_track.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.liketrack.setIcon(icon8)
        self.liketrack.setObjectName("pushButton")
        self.horizontalLayout_12.addWidget(self.liketrack)
        self.horizontalLayout_13.addWidget(self.player_btn_2)
        self.frame_5 = QtWidgets.QFrame(self.musicplayer_btn)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_13.addWidget(self.frame_5)
        self.verticalLayout_4.addWidget(self.musicplayer_btn)
        self.timeline = QtWidgets.QFrame(self.frame_musicplayerbtn)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeline.sizePolicy().hasHeightForWidth())
        self.timeline.setSizePolicy(sizePolicy)
        self.timeline.setMaximumSize(QtCore.QSize(16777215, 40))
        self.timeline.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.timeline.setFrameShadow(QtWidgets.QFrame.Raised)
        self.timeline.setObjectName("timeline")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.timeline)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalSlider = QtWidgets.QSlider(self.timeline)
        self.horizontalSlider.sliderMoved[int].connect(self.set_position)
        self.player = QMediaPlayer(self)
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile("sound\\music_track\\1.mp3")))
        self.player.positionChanged.connect(self.position_changed)
        self.player.durationChanged.connect(self.duration_changed)

        self.playtrack_2.clicked.connect(self.play_app)
        self.pausetrack_2.clicked.connect(self.pause_app)
        self.next_2.clicked.connect(self.next_app)
        self.previous_2.clicked.connect(self.previous_app)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy)
        self.horizontalSlider.setMaximumSize(QtCore.QSize(16777214, 25))
        self.horizontalSlider.setSizeIncrement(QtCore.QSize(2, 0))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout_5.addWidget(self.horizontalSlider)
        self.verticalLayout_4.addWidget(self.timeline)
        self.musicplayerLayout.addWidget(self.frame_musicplayerbtn)
        self.verticalLayout.addWidget(self.musicplayer_icon)
        AccPageWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(AccPageWindow)
        QtCore.QMetaObject.connectSlotsByName(AccPageWindow)

        self.lineEdit.returnPressed.connect(self.onPressed)
        self.lineEdit_2.returnPressed.connect(self.onPressed_2)
        self.all.clicked.connect(self.show_all)
        self.recommend.clicked.connect(self.show_recommend)
        self.toplike.clicked.connect(self.show_toplike)
        self.LDmode = 0
        self.mode.clicked.connect(self.change_mode)
        db.connection.close()
        #length of the tracks
        self.length = self.scrollAreaAllTrack.findChildren(QtWidgets.QFrame, name= "frame_track")

    def onPressed(self):
        """
        Xử lý sự kiện khi nút (có thể là nút tìm kiếm) được nhấn.

        Thực hiện các bước sau:
    
                1. Lấy văn bản từ trường nhập liệu (`self.lineEdit`).
                2. Tiền xử lý văn bản (`self.preprocess()`).
                3. In ra thông báo cho biết văn bản đang được tìm kiếm.

        Lưu ý:
                - Phương thức này giả định rằng `self.lineEdit` là một thành phần giao diện (ví dụ: QLineEdit) đã được khai báo và kết nối.
                - Phương thức `self.preprocess()` được gọi để tiền xử lý văn bản trước khi tìm kiếm (ví dụ: loại bỏ khoảng trắng thừa, chuyển đổi chữ hoa/thường, ...). Bạn cần tự định nghĩa phương thức này.
        """
        self.text = self.lineEdit.text()
        self.preprocess()
        print(f'Searching for: {self.text}')
        
    def onPressed_2(self):
        """
        Thực hiện tìm kiếm bài hát và hiển thị kết quả.

        Phương thức này thực hiện các bước sau:
    
        1. Tiền xử lý văn bản tìm kiếm:
                - Chuyển đổi văn bản tìm kiếm thành chữ thường.
                - Loại bỏ dấu tiếng Việt.
                - Loại bỏ khoảng trắng và các ký tự đặc biệt.
        2. Truy vấn cơ sở dữ liệu:
                - Lấy thông tin tất cả các bài hát từ cơ sở dữ liệu.
        3. Tìm kiếm bài hát:
                - So sánh văn bản tìm kiếm đã tiền xử lý với tên của từng bài hát trong cơ sở dữ liệu (cũng đã tiền xử lý).
                - Nếu tìm thấy, lưu chỉ số của bài hát (`self.search_index`) và tạo một khung hiển thị thông tin bài hát (`self.frame_searchTrack`).
                - Khung hiển thị bao gồm:
                        - Nút play/pause (ẩn nút pause ban đầu)
                        - Ảnh bìa bài hát
                        - Tên bài hát
                        - Thời lượng bài hát
                - Thêm khung hiển thị vào khu vực cuộn (`self.scrollAreaSearchTrack`).
        4. Hiển thị kết quả:
                - Nếu tìm thấy bài hát, hiển thị khu vực cuộn chứa kết quả tìm kiếm và ẩn các khu vực cuộn khác.
                - Nếu không tìm thấy bài hát, hiển thị một khung trống có thông báo "Không có bài hát mà bạn tìm kiếm".

        Lưu ý:
                - Phương thức này giả định rằng `self.lineEdit_2` là thành phần nhập liệu chứa văn bản tìm kiếm.
                - `self.scrollAreaSearchTrack`, `self.scrollArea_TopLikeTrack`, `self.scrollArea_RecommendTrack`, `self.scrollArea_AllTrack` là các thành phần giao diện hiển thị các danh sách bài hát khác nhau.
                - `self.search_buttons`, `self.track_img`, `self.track_name`, `self.search_index` là các thuộc tính của đối tượng để quản lý trạng thái và giao diện của kết quả tìm kiếm.
                - Các nút play/pause được kết nối với các phương thức `search_play` và `search_pause` (cần được định nghĩa trước đó).

        Raises:
                pymysql.Error: Nếu có lỗi xảy ra trong quá trình truy vấn cơ sở dữ liệu.
        """
        _translate = QtCore.QCoreApplication.translate
        def preprocess(text):
    # Chuyển đổi sang chữ thường
                text = text.lower()
    # Loại bỏ dấu
                text = unicodedata.normalize('NFD', text)
                text = text.encode('ascii', 'ignore')
                text = text.decode("utf-8")
    # Loại bỏ khoảng trắng
                text = re.sub(r'\s+', '', text)
    # Loại bỏ ký tự đặc biệt
                text = re.sub(r'\W+', '', text)
                return text
        text = self.lineEdit_2.text()
        #Tìm kiếm và hiển thị bài hát theo tên vừa tìm kiếm
        db = Database()
        self.search_buttons = []
        track_res = db.query("SELECT * FROM track")

        #Search_frame
        self.scrollAreaSearchTrack = QtWidgets.QWidget()
        self.scrollAreaSearchTrack.setGeometry(QtCore.QRect(0, 0, 1632, 928))
        self.scrollAreaSearchTrack.setStyleSheet("")
        self.scrollAreaSearchTrack.setObjectName("scrollAreaSearchTrack")
        self.verticalLayout_searchTrack = QtWidgets.QVBoxLayout(self.scrollAreaSearchTrack)
        self.verticalLayout_searchTrack.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout_searchTrack.setSpacing(5)
        self.verticalLayout_searchTrack.setObjectName("verticalLayout_searchTrack")
        
        self.scrollArea_SearchTrack = QtWidgets.QScrollArea(self.tracks)
        self.scrollArea_SearchTrack.setStyleSheet("border:none;")
        self.scrollArea_SearchTrack.setGeometry(3, 0, 1600, 911)
        self.scrollArea_SearchTrack.setWidgetResizable(True)
        self.scrollArea_SearchTrack.setObjectName("scrollArea_Searchtracks")
        self.scrollArea_SearchTrack.setWidget(self.scrollAreaSearchTrack)

        for i in range(len(track_res)):
             ele = track_res[i]['track_name']
             if preprocess(text) == preprocess(ele):
                self.search_index = i + 1
                self.frame_searchTrack = QtWidgets.QFrame(self.scrollAreaSearchTrack)
                self.frame_searchTrack.setMaximumSize(QtCore.QSize(16777215, 80))
                self.frame_searchTrack.setStyleSheet("border: 2px solid black;\nborder-radius: 10px;")
                self.frame_searchTrack.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_searchTrack.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_searchTrack.setObjectName("frame_searchTrack")
                self.horizontalsearchTrackLayout = QtWidgets.QHBoxLayout(self.frame_searchTrack)
                self.horizontalsearchTrackLayout.setContentsMargins(0, 0, 0, 0)
                self.horizontalsearchTrackLayout.setSpacing(0)
                self.horizontalsearchTrackLayout.setObjectName("horizontalsearchTrackLayout")
                self.searchplay_pause_track_all = QtWidgets.QGroupBox(self.frame_searchTrack)
                self.searchplay_pause_track_all.setMaximumSize(QtCore.QSize(50, 16777215))
                self.searchplay_pause_track_all.setStyleSheet("border:none;")
                self.searchplay_pause_track_all.setObjectName("searchplay_pause_track_all")

                self.playtrack_2 = QtWidgets.QPushButton(self.searchplay_pause_track_all)
                self.playtrack_2.setGeometry(QtCore.QRect(0, 10, 51, 41))
                self.playtrack_2.setStyleSheet("border:none;")
                self.playtrack_2.setText("")
                icon4 = QtGui.QIcon()
                icon4.addPixmap(QtGui.QPixmap("pic\musicplayertab\playTrack.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.playtrack_2.setIcon(icon4)
                self.playtrack_2.setObjectName("playtrack")
                self.pausetrack_2 = QtWidgets.QPushButton(self.searchplay_pause_track_all)
                self.pausetrack_2.setGeometry(QtCore.QRect(0, 10, 51, 41))
                self.pausetrack_2.setStyleSheet("border:none;")
                self.pausetrack_2.setText("")
                self.pausetrack_2.hide()
                self.search_buttons.append(self.playtrack)
                self.search_buttons.append(self.pausetrack)
                self.playtrack_2.clicked.connect(self.search_play)
                self.pausetrack_2.clicked.connect(self.search_pause)
                icon5 = QtGui.QIcon()
                icon5.addPixmap(QtGui.QPixmap("pic\musicplayertab\pauseTrack.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.pausetrack_2.setIcon(icon5)
                self.pausetrack_2.setObjectName("pausetrack")
                self.horizontalsearchTrackLayout.addWidget(self.searchplay_pause_track_all)
                self.frame_searchImg = QtWidgets.QFrame(self.frame_searchTrack)
                self.frame_searchImg.setMaximumSize(QtCore.QSize(100, 16777215))
                self.frame_searchImg.setStyleSheet("border:none;")
                self.frame_searchImg.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_searchImg.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_searchImg.setObjectName("frame_searchImg")
                self.search_label = QtWidgets.QLabel(self.frame_searchImg)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.search_label.sizePolicy().hasHeightForWidth())
                self.search_label.setSizePolicy(sizePolicy)
                self.search_label.setMaximumSize(QtCore.QSize(60, 60))
                self.search_label.setText("")
                track_img_url = "pic\\track_img\\" + str(i+1) + ".jpg"
                self.search_label.setPixmap(QtGui.QPixmap(track_img_url))
                self.search_label.setScaledContents(True)
                self.search_label.setObjectName("search_label")

                self.horizontalsearchLabelLayout = QtWidgets.QHBoxLayout(self.frame_searchImg)
                self.horizontalsearchLabelLayout.setContentsMargins(0, 0, 0, 0)
                self.horizontalsearchLabelLayout.setSpacing(0)
                self.horizontalsearchLabelLayout.setObjectName("horizontalLayout_23")
                self.horizontalsearchLabelLayout.addWidget(self.recom_label)
                self.horizontalsearchTrackLayout.addWidget(self.frame_searchImg)

                self.frame_searchTrackname = QtWidgets.QFrame(self.frame_searchTrack)
                self.frame_searchTrackname.setStyleSheet("border:none;")
                self.frame_searchTrackname.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_searchTrackname.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_searchTrackname.setObjectName("frame_recomtrackname")
                self.horizontalsearchTrackLayout_3 = QtWidgets.QHBoxLayout(self.frame_searchTrackname)
                self.horizontalsearchTrackLayout_3.setContentsMargins(20, 0, 0, 0)
                self.horizontalsearchTrackLayout_3.setSpacing(0)
                self.horizontalsearchTrackLayout_3.setObjectName("horizontalsearchTrackLayout_3")
                self.searchtrack_nameplace = QtWidgets.QLabel(self.frame_searchTrackname)
                self.searchtrack_nameplace.setStyleSheet("font: 75 bold 12pt \"Playfair Display\"; \n"
"border:none;")
                self.searchtrack_nameplace.setObjectName("searchtrack_nameplace")
                self.horizontalsearchTrackLayout_3.addWidget(self.searchtrack_nameplace)
                self.horizontalsearchTrackLayout.addWidget(self.frame_searchTrackname)
                self.frame_searchdurationtrack = QtWidgets.QFrame(self.frame_searchTrack)
                self.frame_searchdurationtrack.setMaximumSize(QtCore.QSize(100, 16777215))
                self.frame_searchdurationtrack.setStyleSheet("border:none;")
                self.frame_searchdurationtrack.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_searchdurationtrack.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_searchdurationtrack.setObjectName("frame_searchdurationtrack")
                self.horizontalsearchTrackLayout_4 = QtWidgets.QHBoxLayout(self.frame_searchdurationtrack)
                self.horizontalsearchTrackLayout_4.setContentsMargins(0, 0, 0, 0)
                self.horizontalsearchTrackLayout_4.setSpacing(0)
                self.horizontalsearchTrackLayout_4.setObjectName("horizontalsearchTrackLayout_4")
                self.searchduration_track = QtWidgets.QLabel(self.frame_searchdurationtrack)
                self.searchduration_track.setStyleSheet("font: 75 12pt \"Arial\"; \n"
"border:none;")
                self.searchduration_track.setObjectName("recomduration_track")
                self.horizontalsearchTrackLayout_4.addWidget(self.searchduration_track)
                self.horizontalsearchTrackLayout.addWidget(self.frame_searchdurationtrack)
                self.verticalLayout_searchTrack.addWidget(self.frame_searchTrack)
                self.searchtrack_nameplace.setText(_translate("AccPageWindow", track_res[i]['track_name']))
                self.searchduration_track.setText(_translate("AccPageWindow", str(track_res[i]['duration'])))
                self.emp_frame_search = QtWidgets.QFrame(self.scrollAreaSearchTrack)
                self.emp_frame_search.setStyleSheet("border:none;")
                self.emp_frame_search.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.emp_frame_search.setFrameShadow(QtWidgets.QFrame.Raised)
                self.emp_frame_search.setObjectName("emp_frame_search")
                self.verticalLayout_searchTrack.addWidget(self.emp_frame_search)

                self.scrollArea_SearchTrack.show()
                self.scrollArea_TopLikeTrack.hide()
                self.scrollArea_RecommendTrack.hide()
                self.scrollArea_AllTrack.hide()
                return
        #tạo 1 frame_track với track_title = "Không có bài hát mà bạn tìm kiếm"
        self.emp_frame_search = QtWidgets.QFrame(self.scrollAreaSearchTrack)
        self.emp_frame_search.setStyleSheet("border:none;")
        self.emp_frame_search.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.emp_frame_search.setFrameShadow(QtWidgets.QFrame.Raised)
        self.emp_frame_search.setObjectName("emp_frame_search")
        self.verticalLayout_searchTrack.addWidget(self.emp_frame_search)

        self.scrollArea_SearchTrack.show()
        self.scrollArea_TopLikeTrack.hide()
        self.scrollArea_RecommendTrack.hide()
        self.scrollArea_AllTrack.hide()
        db.connection.close()

    def play(self):
        """
        Bắt đầu hoặc tiếp tục phát một bài hát.

        Phương thức này thực hiện các bước sau:
    
                1. Xác định nút được nhấn: Lấy thông tin về nút ("Play" hoặc "Pause") đã kích hoạt phương thức.
                2. Ẩn nút hiện tại và hiển thị nút tiếp theo (nếu có):
                        - Nếu nhấn "Play", ẩn nút "Play" và hiển thị nút "Pause".
                        - Nếu nhấn "Pause", ẩn nút "Pause" và hiển thị nút "Play".
                3. Xác định chỉ số của bài hát: Tính toán chỉ số bài hát tương ứng với nút được nhấn dựa trên vị trí của nút trong danh sách `self.buttons`.
                4. Truy vấn cơ sở dữ liệu: Lấy thông tin bài hát (tên, hình ảnh) từ cơ sở dữ liệu dựa trên chỉ số bài hát.
                5. Cập nhật giao diện người dùng:
                        - Thay đổi hình ảnh bài hát hiển thị (`self.track_img`).
                        - Thay đổi tên bài hát hiển thị (`self.track_name`).
                        - Hiển thị/ẩn các nút "Play/Pause" ở các vị trí phù hợp trên giao diện.
                6. Tải và phát bài hát: Sử dụng trình phát media (`self.player`) để tải và phát bài hát từ tệp tin.

        Lưu ý:
                - Phương thức này giả định rằng `self.buttons` là một danh sách chứa các nút "Play/Pause" trên giao diện.
                - `self.next_button_index` được sử dụng để theo dõi chỉ số của nút tiếp theo sẽ được hiển thị.
                - `self.index_track` là chỉ số của bài hát hiện tại.

        Raises:
                pymysql.Error: Nếu có lỗi xảy ra trong quá trình truy vấn cơ sở dữ liệu.
        """

        db = Database()
        button = self.sender()
        button.hide()
        self.next_button_index = (self.buttons.index(button) + 1) % len(self.buttons)
        self.index_track = int((self.next_button_index+1)/2)
        info_track = db.query(f"SELECT * FROM track WHERE track_id={self.index_track}")
        self.track_img.setPixmap(QtGui.QPixmap(f"pic\\track_img\\{self.index_track}.jpg"))
        self.track_name.setText(info_track[0]['track_name'])
        self.buttons[self.next_button_index].show()
        self.playtrack_2.hide()
        self.pausetrack_2.show()
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(f"sound\\music_track\\{self.index_track}.mp3")))
        self.player.play()
        self.playtrack.show()
        self.pausetrack.hide()
        db.connection.close()

    def recom_play(self):
        """
        Bắt đầu hoặc tiếp tục phát một bài hát được đề xuất.

                Phương thức này tương tự như `play`, nhưng nó xử lý các nút "Play/Pause"
                        trong danh sách các bài hát được đề xuất (`self.recom_buttons`).

        Các bước thực hiện:

                1. Xác định nút được nhấn: Lấy thông tin về nút ("Play" hoặc "Pause") đã kích hoạt phương thức.
                2. Ẩn nút hiện tại và hiển thị nút tiếp theo (nếu có) trong danh sách `self.recom_buttons`:
                        - Nếu nhấn "Play", ẩn nút "Play" và hiển thị nút "Pause".
                        - Nếu nhấn "Pause", ẩn nút "Pause" và hiển thị nút "Play".
                3. Xác định chỉ số của bài hát: Tính toán chỉ số bài hát tương ứng với nút được nhấn dựa trên vị trí của nút trong danh sách `self.recom_buttons`.
                4. Truy vấn cơ sở dữ liệu: Lấy thông tin bài hát (tên, hình ảnh) từ cơ sở dữ liệu dựa trên chỉ số bài hát.
                5. Cập nhật giao diện người dùng:
                        - Thay đổi hình ảnh bài hát hiển thị (`self.track_img`).
                        - Thay đổi tên bài hát hiển thị (`self.track_name`).
                        - Hiển thị/ẩn các nút "Play/Pause" ở các vị trí phù hợp trong danh sách `self.recom_buttons`.
                        - Đảm bảo nút "Play" chính được hiển thị và nút "Pause" chính được ẩn. (Giả sử bạn có các nút play/pause chính ở nơi khác trên giao diện) 
                6. Tải và phát bài hát: Sử dụng trình phát media (`self.player`) để tải và phát bài hát từ tệp tin.

        Lưu ý:
                - Phương thức này giả định rằng `self.recom_buttons` là một danh sách chứa các nút "Play/Pause" cho các bài hát được đề xuất.
                - `self.next_button_index` được sử dụng để theo dõi chỉ số của nút tiếp theo sẽ được hiển thị trong danh sách `self.recom_buttons`.
                - `self.index_track` là chỉ số của bài hát hiện tại (được tính toán từ `self.next_button_index`).

        Raises:
                pymysql.Error: Nếu có lỗi xảy ra trong quá trình truy vấn cơ sở dữ liệu.
                IndexError: Nếu `self.recom_buttons` không có phần tử nào hoặc `info_track` rỗng (không có kết quả truy vấn).
        """
        db = Database()
        button = self.sender()
        button.hide()
        self.next_button_index = (self.recom_buttons.index(button) + 1) % len(self.recom_buttons)
        self.index_track = int((self.next_button_index+1)/2)
        info_track = db.query(f"SELECT * FROM track WHERE track_id={self.index_track}")
        self.track_img.setPixmap(QtGui.QPixmap(f"pic\\track_img\\{self.index_track}.jpg"))
        self.track_name.setText(info_track[0]['track_name'])
        self.recom_buttons[self.next_button_index].show()
        self.playtrack_2.hide()
        self.pausetrack_2.show()
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(f"sound\\music_track\\{self.index_track}.mp3")))
        self.player.play()
        db.connection.close()

    def search_play(self):
        """
        Bắt đầu phát bài hát từ kết quả tìm kiếm.

        Phương thức này thực hiện các bước sau:
    
                1. Truy vấn cơ sở dữ liệu: Lấy thông tin bài hát (tên, hình ảnh) từ cơ sở dữ liệu dựa trên `self.search_index` (giả định đây là chỉ số của bài hát trong kết quả tìm kiếm).
                2. Cập nhật giao diện người dùng:
                        - Thay đổi hình ảnh bài hát hiển thị (`self.track_img`).
                        - Thay đổi tên bài hát hiển thị (`self.track_name`).
                        - Ẩn nút "Play" chính và hiển thị nút "Pause" chính (giả định có các nút này trên giao diện).
                        - Ẩn nút "Play" phụ và hiển thị nút "Pause" phụ (giả định có các nút này trên giao diện).
                3. Tải và phát bài hát: Sử dụng trình phát media (`self.player`) để tải và phát bài hát từ tệp tin.

        Lưu ý:
                - Phương thức này giả định rằng `self.search_index` là chỉ số hợp lệ của bài hát trong kết quả tìm kiếm.
                - `self.track_img`, `self.track_name`, `self.player` là các thuộc tính của đối tượng (giả định đã được khai báo trước đó).
                - `playtrack`, `pausetrack`, `playtrack_2`, `pausetrack_2` là các nút điều khiển phát nhạc (giả định đã được khai báo trước đó).

        Raises:
                pymysql.Error: Nếu có lỗi xảy ra trong quá trình truy vấn cơ sở dữ liệu.
                IndexError: Nếu `info_track` rỗng (không có kết quả truy vấn).
        """
        db = Database()
        info_track = db.query(f"SELECT * FROM track WHERE track_id={self.search_index}")
        self.track_img.setPixmap(QtGui.QPixmap(f"pic\\track_img\\{self.search_index}.jpg"))
        self.track_name.setText(info_track[0]['track_name'])
        self.playtrack_2.hide()
        self.pausetrack_2.show()
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(f"sound\\music_track\\{self.search_index}.mp3")))
        self.player.play()
        self.playtrack.hide()
        self.pausetrack.show()
        db.connection.close()

    def TopLike_play(self):
        """
        Bắt đầu hoặc tiếp tục phát một bài hát từ danh sách bài hát được yêu thích nhiều nhất (TopLike).

        Phương thức này tương tự như `play` và `recom_play`, nhưng xử lý các nút "Play/Pause"
                trong danh sách các bài hát được yêu thích nhiều nhất (`self.TopLike_buttons`).

        Các bước thực hiện:

                1. Xác định nút được nhấn: Lấy thông tin về nút ("Play" hoặc "Pause") đã kích hoạt phương thức.
                2. Ẩn nút hiện tại và hiển thị nút tiếp theo (nếu có) trong danh sách `self.TopLike_buttons`:
                        - Nếu nhấn "Play", ẩn nút "Play" và hiển thị nút "Pause".
                        - Nếu nhấn "Pause", ẩn nút "Pause" và hiển thị nút "Play".
                3. Xác định chỉ số của bài hát: Tính toán chỉ số bài hát tương ứng với nút được nhấn dựa trên vị trí của nút trong danh sách `self.TopLike_buttons`.
                4. Truy vấn cơ sở dữ liệu: Lấy thông tin bài hát (tên, hình ảnh) từ cơ sở dữ liệu dựa trên chỉ số bài hát.
                5. Cập nhật giao diện người dùng:
                        - Thay đổi hình ảnh bài hát hiển thị (`self.track_img`).
                        - Thay đổi tên bài hát hiển thị (`self.track_name`).
                        - Hiển thị/ẩn các nút "Play/Pause" ở các vị trí phù hợp trong danh sách `self.TopLike_buttons`.
                        - Ẩn nút "Play" chính và hiển thị nút "Pause" chính (giả định có các nút này trên giao diện).
                6. Tải và phát bài hát: Sử dụng trình phát media (`self.player`) để tải và phát bài hát từ tệp tin.

        Lưu ý:
                - Phương thức này giả định rằng `self.TopLike_buttons` là một danh sách chứa các nút "Play/Pause" cho các bài hát được yêu thích nhiều nhất.
                - `self.next_button_index` được sử dụng để theo dõi chỉ số của nút tiếp theo sẽ được hiển thị trong danh sách `self.TopLike_buttons`.
                - `self.index_track` là chỉ số của bài hát hiện tại (được tính toán từ `self.next_button_index`).

        Raises:
                pymysql.Error: Nếu có lỗi xảy ra trong quá trình truy vấn cơ sở dữ liệu.
                IndexError: Nếu `self.TopLike_buttons` không có phần tử nào hoặc `info_track` rỗng (không có kết quả truy vấn).
        """
        db = Database()
        button = self.sender()
        button.hide()
        self.next_button_index = (self.TopLike_buttons.index(button) + 1) % len(self.TopLike_buttons)
        self.index_track = int((self.next_button_index+1)/2)
        info_track = db.query(f"SELECT * FROM track WHERE track_id={self.index_track}")
        self.track_img.setPixmap(QtGui.QPixmap(f"pic\\track_img\\{self.index_track}.jpg"))
        self.track_name.setText(info_track[0]['track_name'])
        self.TopLike_buttons[self.next_button_index].show()
        self.playtrack_2.hide()
        self.pausetrack_2.show()
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(f"sound\\music_track\\{self.index_track}.mp3")))
        self.player.play()
        db.connection.close()

    def recom_pause(self):
        """
        Tạm dừng phát bài hát trong danh sách đề xuất.

        Phương thức này xử lý việc tạm dừng phát nhạc khi nhấn nút "Pause" 
                trong danh sách các bài hát được đề xuất (`self.recom_buttons`).

        Các bước thực hiện:

                1. Xác định nút "Pause" được nhấn.
                2. Ẩn nút "Pause" đã nhấn và hiển thị nút "Play" tương ứng trong danh sách `self.recom_buttons`.
                3. Hiển thị nút "Play" chính và ẩn nút "Pause" chính (giả định có các nút này trên giao diện).
                4. Tạm dừng trình phát media (`self.player`).

        Lưu ý:
                - Phương thức này giả định rằng `self.recom_buttons` là một danh sách chứa các nút "Play/Pause" cho các bài hát được đề xuất.
                - `self.next_button_index` được sử dụng để theo dõi chỉ số của nút tiếp theo (trong trường hợp này là nút "Play") sẽ được hiển thị.

        Raises:
                IndexError: Nếu `self.recom_buttons` không có phần tử nào.
        """
        button = self.sender()
        button.hide()
        self.next_button_index = (self.recom_buttons.index(button) - 1) % len(self.recom_buttons)
        self.recom_buttons[self.next_button_index].show()
        self.playtrack_2.show()
        self.pausetrack_2.hide()
        self.player.pause()

    def TopLike_pause(self):
        """
        Tạm dừng phát bài hát trong danh sách "TopLike" (các bài hát được yêu thích nhiều nhất).

        Phương thức này xử lý việc tạm dừng phát nhạc khi nhấn nút "Pause" trong danh sách
                các bài hát được yêu thích nhiều nhất (`self.TopLike_buttons`).

        Các bước thực hiện:

                1. Xác định nút "Pause" được nhấn.
                2. Ẩn nút "Pause" đã nhấn và hiển thị nút "Play" tương ứng trong danh sách `self.TopLike_buttons`.
                3. Hiển thị nút "Play" chính và ẩn nút "Pause" chính (giả định có các nút này trên giao diện).
                4. Tạm dừng trình phát media (`self.player`).

        Lưu ý:
                - Phương thức này giả định rằng `self.TopLike_buttons` là một danh sách chứa các nút "Play/Pause" cho các bài hát được yêu thích nhiều nhất.
                - `self.next_button_index` được sử dụng để theo dõi chỉ số của nút tiếp theo (trong trường hợp này là nút "Play") sẽ được hiển thị.

        Raises:
                IndexError: Nếu `self.TopLike_buttons` không có phần tử nào.
        """
        button = self.sender()
        button.hide()
        self.next_button_index = (self.TopLike_buttons.index(button) - 1) % len(self.TopLike_buttons)
        self.TopLike_buttons[self.next_button_index].show()
        self.playtrack_2.show()
        self.pausetrack_2.hide()
        self.player.pause()

    def pause(self):
        """
        Tạm dừng phát nhạc hiện tại.

        Phương thức này xử lý việc tạm dừng phát nhạc khi nhấn nút "Pause". 
        Các bước thực hiện:

                1. Xác định nút "Pause" được nhấn.
                2. Ẩn nút "Pause" đã nhấn và hiển thị nút "Play" tương ứng trong danh sách `self.buttons`.
                3. Hiển thị nút "Play" chính và ẩn nút "Pause" chính (giả định có các nút này trên giao diện).
                4. Hiển thị nút "Play" phụ và ẩn nút "Pause" phụ (giả định có các nút này trên giao diện).
                5. Tạm dừng trình phát media (`self.player`).

        Lưu ý:
                - Phương thức này giả định rằng `self.buttons` là một danh sách chứa các nút "Play/Pause" cho các bài hát chính.
                - `self.next_button_index` được sử dụng để theo dõi chỉ số của nút tiếp theo (trong trường hợp này là nút "Play") sẽ được hiển thị.

        Raises:
                IndexError: Nếu `self.buttons` không có phần tử nào.
        """
        button = self.sender()
        button.hide()
        self.next_button_index = (self.buttons.index(button) - 1) % len(self.buttons)
        self.buttons[self.next_button_index].show()
        self.playtrack_2.show()
        self.pausetrack_2.hide()
        self.playtrack.show()
        self.pausetrack.hide()
        self.player.pause()

    def search_pause(self):
        """
        Tạm dừng phát bài hát từ kết quả tìm kiếm.

        Phương thức này xử lý việc tạm dừng phát nhạc khi nhấn nút "Pause" sau khi đã phát
                một bài hát từ kết quả tìm kiếm.

        Các bước thực hiện:

                1. Hiển thị nút "Play" chính và ẩn nút "Pause" chính (giả định có các nút này trên giao diện).
                2. Hiển thị nút "Play" phụ và ẩn nút "Pause" phụ (giả định có các nút này trên giao diện).
                3. Tạm dừng trình phát media (`self.player`).

        Lưu ý:
                - Phương thức này không thay đổi trạng thái của các nút "Play/Pause" trong danh sách kết quả tìm kiếm.
                - `self.player`, `self.playtrack`, `self.pausetrack`, `self.playtrack_2` và `self.pausetrack_2` là các thuộc tính của đối tượng, giả định đã được khai báo trước đó.
        """
        self.playtrack_2.show()
        self.pausetrack_2.hide()
        self.playtrack.show()
        self.pausetrack.hide()
        self.player.pause()

    def play_app(self):
        """
        Tiếp tục phát nhạc hoặc bắt đầu phát từ đầu nếu chưa phát.

        Phương thức này thực hiện các bước sau:
        
                1. Ẩn nút "Play" chính và nút "Play" phụ (giả định có các nút này trên giao diện).
                2. Hiển thị nút "Pause" chính và nút "Pause" phụ (giả định có các nút này trên giao diện).
                3. Tiếp tục phát nhạc từ vị trí hiện tại bằng trình phát media (`self.player`).
                Nếu nhạc chưa được phát, phương thức sẽ bắt đầu phát từ đầu.

        Lưu ý:
                - `self.player`, `self.playtrack`, `self.pausetrack`, `self.playtrack_2` và `self.pausetrack_2` là các thuộc tính của đối tượng, giả định đã được khai báo trước đó.
        """
        self.pausetrack_2.show()
        self.playtrack_2.hide()
        self.playtrack.hide()
        self.pausetrack.show()
        self.player.play()

    def pause_app(self):
        """
        Tạm dừng phát nhạc hiện tại.

        Phương thức này xử lý việc tạm dừng phát nhạc.

        Các bước thực hiện:

                1. Hiển thị nút "Play" chính và nút "Play" phụ (giả định có các nút này trên giao diện).
                2. Ẩn nút "Pause" chính và nút "Pause" phụ (giả định có các nút này trên giao diện).
                3. Tạm dừng trình phát media (`self.player`).

        Lưu ý:
                - `self.player`, `self.playtrack`, `self.pausetrack`, `self.playtrack_2` và `self.pausetrack_2` là các thuộc tính của đối tượng, giả định đã được khai báo trước đó.
        """        
        self.playtrack_2.show()
        self.pausetrack_2.hide()
        self.playtrack.show()
        self.pausetrack.hide()
        self.player.pause()

    def next_app(self):
        """
        Phát bài hát tiếp theo trong danh sách nhạc.

        Phương thức thực hiện các bước sau:
    
                1. Tăng chỉ số bài hát hiện tại (`self.index_track`) lên 1.
                2. Truy vấn cơ sở dữ liệu để lấy thông tin của bài hát tiếp theo (tên, hình ảnh).
                3. Cập nhật giao diện người dùng (hình ảnh, tên bài hát) để hiển thị thông tin bài hát mới.
                4. Tải và phát bài hát mới bằng trình phát media (`self.player`).

        Xử lý lỗi:
                Nếu không tìm thấy bài hát tiếp theo (ví dụ: đang ở bài hát cuối cùng), phương thức sẽ phát bài hát đầu tiên trong danh sách (giả định bài hát có `track_id` là 1).

        aises:
                pymysql.Error: Nếu có lỗi xảy ra trong quá trình truy vấn cơ sở dữ liệu.
        """
        try:
                db = Database()
                self.index_track = self.index_track + 1
                info_track = db.query(f"SELECT * FROM track WHERE track_id={self.index_track}")
                self.track_img.setPixmap(QtGui.QPixmap(f"pic\\track_img\\{self.index_track}.jpg"))
                self.track_name.setText(info_track[0]['track_name'])
                self.player.setMedia(QMediaContent(QUrl.fromLocalFile(f"sound\\music_track\\{self.index_track}.mp3")))
                self.player.play()
                db.connection.close()
        except Exception as e:
                db = Database()
                info_track = db.query(f"SELECT * FROM track WHERE track_id=1")
                self.track_img.setPixmap(QtGui.QPixmap(f"pic\\track_img\\1.jpg"))
                self.track_name.setText(info_track[0]['track_name'])
                self.player.setMedia(QMediaContent(QUrl.fromLocalFile(f"sound\\music_track\\1.mp3")))
                self.player.play()
                db.connection.close()

    def previous_app(self):
        """
        Phát bài hát trước đó trong danh sách nhạc.

        Phương thức thực hiện các bước sau:

                1. Giảm chỉ số bài hát hiện tại (`self.index_track`) xuống 1.
                2. Truy vấn cơ sở dữ liệu để lấy thông tin của bài hát trước đó (tên, hình ảnh).
                3. Cập nhật giao diện người dùng (hình ảnh, tên bài hát) để hiển thị thông tin bài hát mới.
                4. Tải và phát bài hát mới bằng trình phát media (`self.player`).

        Xử lý lỗi:
                Nếu không tìm thấy bài hát trước đó (ví dụ: đang ở bài hát đầu tiên), phương thức sẽ phát bài hát cuối cùng trong danh sách (giả định bài hát có `track_id` là 100).

        Raises:
                pymysql.Error: Nếu có lỗi xảy ra trong quá trình truy vấn cơ sở dữ liệu.
        """
        try:
                db = Database()
                self.index_track = self.index_track - 1
                info_track = db.query(f"SELECT * FROM track WHERE track_id={self.index_track}")
                self.track_img.setPixmap(QtGui.QPixmap(f"pic\\track_img\\{self.index_track}.jpg"))
                self.track_name.setText(info_track[0]['track_name'])
                self.player.setMedia(QMediaContent(QUrl.fromLocalFile(f"sound\\music_track\\{self.index_track}.mp3")))
                self.player.play()
                db.connection.close()
        except Exception as e:
                db = Database()
                info_track = db.query(f"SELECT * FROM track WHERE track_id=100")
                self.track_img.setPixmap(QtGui.QPixmap(f"pic\\track_img\\100.jpg"))
                self.track_name.setText(info_track[0]['track_name'])
                self.player.setMedia(QMediaContent(QUrl.fromLocalFile(f"sound\\music_track\\100.mp3")))
                self.player.play()
                db.connection.close()

    def change_volume(self, value):
        """
                Thay đổi âm lượng của trình phát media.

        Args:
                value (int): Giá trị âm lượng mới (0-100).
        """
        self.player.setVolume(value)

    def position_changed(self, position):
        """
                Cập nhật thanh trượt (horizontalSlider) khi vị trí phát media thay đổi.

        Args:
                position (int): Vị trí mới của media (tính bằng mili giây).
        """
        self.horizontalSlider.setValue(position)

    def duration_changed(self, duration):
        """
                Cập nhật phạm vi của thanh trượt khi độ dài của media thay đổi.

        Args:
                duration (int): Tổng độ dài của media (tính bằng mili giây).
        """
        self.horizontalSlider.setRange(0, duration)

    def set_position(self, position):
        """
                Đặt vị trí phát của media.

        Args:
                position (int): Vị trí mới của media (tính bằng mili giây).
        """
        self.player.setPosition(position)

    def show_all(self):
        """
        Hiển thị danh sách tất cả bài hát.

        hương thức này ẩn các danh sách bài hát khác (nếu có) và hiển thị danh sách tất cả bài hát (`self.scrollArea_AllTrack`).

        Lưu ý:
                - Phương thức này giả định rằng `self.scrollArea_AllTrack`, `self.scrollArea_RecommendTrack`,
                        `self.scrollArea_TopLikeTrack`, và có thể có `self.scrollArea_SearchTrack` đã được khai báo và thiết lập trước đó.
        """
        self.scrollArea_AllTrack.show()
        self.scrollArea_RecommendTrack.hide()
        self.scrollArea_TopLikeTrack.hide()
        if hasattr(self, "scrollArea_SearchTrack"):
                self.scrollArea_SearchTrack.hide()

    def show_recommend(self):
        """
        Hiển thị danh sách các bài hát gợi ý.

        Phương thức này ẩn các danh sách bài hát khác (nếu có) và hiển thị danh sách bài hát gợi ý (`self.scrollArea_RecommendTrack`).

        Lưu ý:
                - Phương thức này giả định rằng `self.scrollArea_RecommendTrack`, `self.scrollArea_AllTrack`,
                        `self.scrollArea_TopLikeTrack`, và có thể có `self.scrollArea_SearchTrack` đã được khai báo và thiết lập trước đó.
        """
        self.scrollArea_RecommendTrack.show()
        self.scrollArea_AllTrack.hide()
        self.scrollArea_TopLikeTrack.hide()
        if hasattr(self, "scrollArea_SearchTrack"):
                self.scrollArea_SearchTrack.hide()

    def show_toplike(self):
        """
        Hiển thị danh sách các bài hát được yêu thích nhiều nhất (TopLike).

        Phương thức này ẩn các danh sách bài hát khác (nếu có) và hiển thị danh sách bài hát TopLike (`self.scrollArea_TopLikeTrack`).

        Lưu ý:
                - Phương thức này giả định rằng `self.scrollArea_TopLikeTrack`, `self.scrollArea_RecommendTrack`,
                        `self.scrollArea_AllTrack`, và có thể có `self.scrollArea_SearchTrack` đã được khai báo và thiết lập trước đó.
        """
        self.scrollArea_TopLikeTrack.show()
        self.scrollArea_RecommendTrack.hide()
        self.scrollArea_AllTrack.hide()
        if hasattr(self, "scrollArea_SearchTrack"):
                self.scrollArea_SearchTrack.hide()
 

    def retranslateUi(self, AccPageWindow):
        """
        Dịch lại nội dung văn bản trên giao diện người dùng (nếu cần).

        Args:
                AccPageWindow (QtWidgets.QMainWindow): Cửa sổ chính chứa trang thông tin tài khoản.
        """
        _translate = QtCore.QCoreApplication.translate
        AccPageWindow.setWindowTitle(_translate("AccPageWindow", "AccPageWindow"))
        self.watefeel.setText(_translate("AccPageWindow", "WaterFeel"))
        self.comboBox.setItemText(0, _translate("AccPageWindow", "Account"))
        self.comboBox.setItemText(1, _translate("AccPageWindow", "Help"))
        self.comboBox.setItemText(2, _translate("AccPageWindow", "Sign out"))               
        self.all.setText(_translate("AccPageWindow", "All"))
        self.recommend.setText(_translate("AccPageWindow", "Recommend"))
        self.my_playlist.setText(_translate("AccPageWindow", "My Playlist"))
        self.album.setText(_translate("AccPageWindow", "Album"))
        self.toplike.setText(_translate("AccPageWindow", "Top Liked"))
        self.seasons.setText(_translate("AccPageWindow", "Seasons"))
        self.track_name.setText(_translate("AccPageWindow", ""))
        self.volume_text.setText(_translate("AccPageWindow", "Volume"))

    def change_mode(self):
        """
        Phương thức chuyển đổi trạng thái Light/Dark Mode cho acc_page.py
        """
        if (self.LDmode == 0):
                self.LDmode = 1
                self.content.setStyleSheet("background-color: rgb(0, 0, 0)")
                self.header.setStyleSheet("background-color: rgb(0, 0, 0)")
                self.watefeel.setStyleSheet("color: white;\nfont: 75 20pt \"Playfair Display\"")
                self.mode.setStyleSheet("background-color: rgb(255, 255, 255);\nborder: 2px solid white;\nborder-radius: 25px;")
                self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);\nborder: 2px solid white;\nborder-radius: 20px;")
                self.search_playlist.setStyleSheet("background-color: rgb(214, 214, 214);\nborder: 2px solid white;\nborder-radius: 10px;")
                self.track_lists_types.setStyleSheet("background-color: rgb(214, 214, 214);\nborder: 2px solid white;\nborder-radius: 10px;")
                self.mode.setIcon(QtGui.QIcon("pic\lightdarkmode\dark-mode-icon.png"))
                self.musicplayer_icon.setStyleSheet("background-color: rgb(0, 0, 0)")
                self.frame.setStyleSheet("border: 2px solid white;\nborder-radius: 10px;")
                self.frame_musicplayerbtn.setStyleSheet("border: 2px solid white;\nborder-radius: 10px;")
                self.musicplayer_btn.setStyleSheet("border:none;")
                self.timeline.setStyleSheet("border:none;")
                self.volume_text.setStyleSheet("color: white")
                self.track_name.setStyleSheet("color: white;\nfont: 75 10pt \"Playfair Display\";\nborder:none;")
                self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255)")
                self.track_img.setStyleSheet("border:2px solid white;\nborder-radius: 10px;")
                self.player_btn_2.setStyleSheet("background-color: rgb(255, 255, 255);\nborder:2px solid white;\nborder-radius: 20px;")
        else:
                self.LDmode = 0
                self.content.setStyleSheet("background-color: rgb(255, 255, 255)")
                self.header.setStyleSheet("background-color: rgb(255, 255, 255)")
                self.watefeel.setStyleSheet("font: 75 20pt \"Playfair Display\";\nborder:none;")
                self.mode.setStyleSheet("border: none;")
                self.lineEdit_2.setStyleSheet("background-color: rgb(214, 214, 214);\nborder: 2px solid black;\nborder-radius: 20px;")
                self.search_playlist.setStyleSheet("background-color: rgb(255, 255, 255);\nborder: 2px solid black;\nborder-radius: 10px;")
                self.track_lists_types.setStyleSheet("background-color: rgb(255, 255, 255);\nborder: 2px solid black;\nborder-radius: 10px;")
                self.mode.setIcon(QtGui.QIcon("pic\lightdarkmode\dark-mode-icon.png"))
                self.musicplayer_icon.setStyleSheet("background-color: rgb(255, 255, 255)")
                self.frame.setStyleSheet("border: 2px solid black;\nborder-radius: 10px;")
                self.frame_musicplayerbtn.setStyleSheet("border: 2px solid black;\nborder-radius: 10px;")
                self.musicplayer_btn.setStyleSheet("border:none;")
                self.timeline.setStyleSheet("border:none;")
                self.track_name.setStyleSheet("color: black;\nfont: 75 10pt \"Playfair Display\";\nborder:none;")
                self.track_img.setStyleSheet("border:2px solid black;\nborder-radius: 10px;")
                self.lineEdit.setStyleSheet("background-color: rgb(214, 214, 214);\nborder: 2px solid black;\nborder-radius: 10px;")
                self.player_btn_2.setStyleSheet("background-color: rgb(255, 255, 255);\nborder:2px solid black;\nborder-radius: 20px;")
                self.track_name.setStyleSheet("color: black;\nfont: 75 10pt \"Playfair Display\";\nborder:none;")
                self.mode.setIcon(QtGui.QIcon("pic\lightdarkmode\light-mode-icon.png"))


if __name__ == "__main__":

        import sys
        from acc_page import Ui_AccPageWindow
        app = QtWidgets.QApplication(sys.argv)
        AccPageWindow = QtWidgets.QMainWindow()
        ui = Ui_AccPageWindow()
        ui.setupUi(AccPageWindow)
        AccPageWindow.show()
        sys.exit(app.exec_())