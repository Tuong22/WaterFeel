from PyQt5 import QtCore, QtGui, QtWidgets
from database import Database
from acc_page import Ui_AccPageWindow
from PyQt5.QtCore import QTimer

class Ui_SignInUpWindow(object):
    def setupUi(self, SignWindow):
        """
        Thiết lập giao diện người dùng chính.

        Args:
                SignWindow (QMainWindow): Đối tượng cửa sổ đăng nhập/đăng ký cần thiết lập giao diện.
        """
        SignWindow.setObjectName("SignWindow")
        SignWindow.resize(1944, 962)

        self.frame_sign_in = QtWidgets.QWidget(SignWindow)
        self.frame_sign_in.setObjectName("frame_sign_in")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_sign_in)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QFrame(self.frame_sign_in)
        self.header.setMaximumSize(QtCore.QSize(16777215, 100))
        self.header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_logo = QtWidgets.QFrame(self.header)
        self.frame_logo.setMaximumSize(QtCore.QSize(105, 16777215))
        self.frame_logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_logo.setObjectName("frame_logo")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_logo)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.logo = QtWidgets.QLabel(self.frame_logo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("pic\logo\Logo-light_mode.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.verticalLayout_8.addWidget(self.logo)
        self.horizontalLayout.addWidget(self.frame_logo)
        self.btn_places = QtWidgets.QFrame(self.header)
        self.btn_places.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.btn_places.setFrameShadow(QtWidgets.QFrame.Raised)
        self.btn_places.setObjectName("btn_places")
        self.horizontalLayout.addWidget(self.btn_places)
        self.frame_options = QtWidgets.QFrame(self.header)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_options.sizePolicy().hasHeightForWidth())
        self.frame_options.setSizePolicy(sizePolicy)
        self.frame_options.setMaximumSize(QtCore.QSize(220, 16777215))
        self.frame_options.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_options.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_options.setObjectName("frame_options")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_options)
        self.horizontalLayout_5.setContentsMargins(0, 0, 15, 5)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.groupBox = QtWidgets.QGroupBox(self.frame_options)
        self.groupBox.setStyleSheet("border:none;")
        self.groupBox.setObjectName("groupBox")
        self.btnsignup = QtWidgets.QPushButton(self.groupBox)
        self.btnsignup.setGeometry(QtCore.QRect(20, 20, 80, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnsignup.sizePolicy().hasHeightForWidth())
        self.btnsignup.setSizePolicy(sizePolicy)
        self.btnsignup.setMaximumSize(QtCore.QSize(80, 50))
        self.btnsignup.setStyleSheet("border: 2px solid black;\n"
"font: 75 10pt \"Playfair Display\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.btnsignup.setObjectName("btnsignup")
        self.btnsignin = QtWidgets.QPushButton(self.groupBox)
        self.btnsignin.setGeometry(QtCore.QRect(20, 20, 80, 50))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnsignin.sizePolicy().hasHeightForWidth())
        self.btnsignin.setSizePolicy(sizePolicy)
        self.btnsignin.setMaximumSize(QtCore.QSize(80, 50))
        self.btnsignin.setStyleSheet("border: 2px solid black;\n"
"font: 75 10pt \"Playfair Display\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.btnsignin.setObjectName("btnsignin")
        self.horizontalLayout_5.addWidget(self.groupBox)
        self.help = QtWidgets.QPushButton(self.frame_options)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.help.sizePolicy().hasHeightForWidth())
        self.help.setSizePolicy(sizePolicy)
        self.help.setMaximumSize(QtCore.QSize(80, 50))
        self.help.setStyleSheet("border: 2px solid black;\n"
"font: 75 10pt \"Playfair Display\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 15px;")
        self.help.setObjectName("help")
        self.horizontalLayout_5.addWidget(self.help)
        self.horizontalLayout.addWidget(self.frame_options)
        self.verticalLayout.addWidget(self.header)
        self.content = QtWidgets.QGroupBox(self.frame_sign_in)
        self.content.setObjectName("content")
        self.frame_signup = QtWidgets.QFrame(self.content)
        self.frame_signup.setGeometry(QtCore.QRect(0, 0, 1951, 861))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_signup.sizePolicy().hasHeightForWidth())
        self.frame_signup.setSizePolicy(sizePolicy)
        self.frame_signup.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_signup.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_signup.setObjectName("frame_signup")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_signup)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.emp_frame_3 = QtWidgets.QFrame(self.frame_signup)
        self.emp_frame_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.emp_frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.emp_frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.emp_frame_3.setObjectName("emp_frame_3")
        self.horizontalLayout_2.addWidget(self.emp_frame_3)
        self.frame_signinform = QtWidgets.QFrame(self.frame_signup)
        self.frame_signinform.setMaximumSize(QtCore.QSize(450, 16777215))
        self.frame_signinform.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_signinform.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_signinform.setObjectName("frame_signinform")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_signinform)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.emp_frame_4 = QtWidgets.QFrame(self.frame_signinform)
        self.emp_frame_4.setMaximumSize(QtCore.QSize(16777215, 100))
        self.emp_frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.emp_frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.emp_frame_4.setObjectName("emp_frame_4")
        self.verticalLayout_2.addWidget(self.emp_frame_4)
        self.frame_form_place = QtWidgets.QFrame(self.frame_signinform)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_form_place.sizePolicy().hasHeightForWidth())
        self.frame_form_place.setSizePolicy(sizePolicy)
        self.frame_form_place.setMaximumSize(QtCore.QSize(16777215, 550))
        self.frame_form_place.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius: 20px;")
        self.frame_form_place.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_form_place.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_form_place.setObjectName("frame_form_place")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_form_place)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_title = QtWidgets.QFrame(self.frame_form_place)
        self.frame_title.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_title.setStyleSheet("border:none;")
        self.frame_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title.setObjectName("frame_title")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_title)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.emp_frame_9 = QtWidgets.QFrame(self.frame_title)
        self.emp_frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.emp_frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.emp_frame_9.setObjectName("emp_frame_9")
        self.horizontalLayout_4.addWidget(self.emp_frame_9)
        self.title = QtWidgets.QFrame(self.frame_title)
        self.title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title.setObjectName("title")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.title)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.signin = QtWidgets.QLabel(self.title)
        self.signin.setStyleSheet("font: 75 22pt \"Playfair Display\";")
        self.signin.setAlignment(QtCore.Qt.AlignCenter)
        self.signin.setObjectName("signin")
        self.verticalLayout_4.addWidget(self.signin)
        self.horizontalLayout_4.addWidget(self.title)
        self.emp_frame_6 = QtWidgets.QFrame(self.frame_title)
        self.emp_frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.emp_frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.emp_frame_6.setObjectName("emp_frame_6")
        self.horizontalLayout_4.addWidget(self.emp_frame_6)
        self.verticalLayout_3.addWidget(self.frame_title)
        self.frame_name = QtWidgets.QFrame(self.frame_form_place)
        self.frame_name.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_name.setStyleSheet("border:none;")
        self.frame_name.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_name.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_name.setObjectName("frame_name")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_name)
        self.verticalLayout_5.setContentsMargins(30, 10, 30, 0)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.nameinput_text = QtWidgets.QLabel(self.frame_name)
        self.nameinput_text.setStyleSheet("font: 75 10pt \"Arial\";")
        self.nameinput_text.setObjectName("nameinput_text")
        self.verticalLayout_5.addWidget(self.nameinput_text)
        self.nameinput_place = QtWidgets.QPlainTextEdit(self.frame_name)
        self.nameinput_place.setStyleSheet("border: 2px solid black;\n"
"border-radius:7px;")
        self.nameinput_place.setObjectName("nameinput_place")
        self.verticalLayout_5.addWidget(self.nameinput_place)
        self.verticalLayout_3.addWidget(self.frame_name)
        self.frame_email_3 = QtWidgets.QFrame(self.frame_form_place)
        self.frame_email_3.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_email_3.setStyleSheet("border:none;")
        self.frame_email_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_email_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_email_3.setObjectName("frame_email_3")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_email_3)
        self.verticalLayout_17.setContentsMargins(30, 10, 30, 0)
        self.verticalLayout_17.setSpacing(10)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.email_text_3 = QtWidgets.QLabel(self.frame_email_3)
        self.email_text_3.setStyleSheet("font: 75 10pt \"Arial\";")
        self.email_text_3.setObjectName("email_text_3")
        self.verticalLayout_17.addWidget(self.email_text_3)
        self.emailinput_place_3 = QtWidgets.QPlainTextEdit(self.frame_email_3)
        self.emailinput_place_3.setStyleSheet("border: 2px solid black;\n"
"border-radius:7px;")
        self.emailinput_place_3.setObjectName("emailinput_place_3")
        self.verticalLayout_17.addWidget(self.emailinput_place_3)
        self.verticalLayout_3.addWidget(self.frame_email_3)
        self.frame_password = QtWidgets.QFrame(self.frame_form_place)
        self.frame_password.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_password.setStyleSheet("border:none;")
        self.frame_password.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_password.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_password.setObjectName("frame_password")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_password)
        self.verticalLayout_6.setContentsMargins(30, 10, 30, 0)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.password_text = QtWidgets.QLabel(self.frame_password)
        self.password_text.setStyleSheet("font: 75 10pt \"Arial\";")
        self.password_text.setObjectName("password_text")
        self.verticalLayout_6.addWidget(self.password_text)
        self.passwordinput_place = QtWidgets.QLineEdit(self.frame_password)
        self.passwordinput_place.setStyleSheet("border: 2px solid black;\n"
"border-radius:7px;")
        self.passwordinput_place.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordinput_place.setObjectName("passwordinput_place")
        self.verticalLayout_6.addWidget(self.passwordinput_place)
        self.verticalLayout_3.addWidget(self.frame_password)
        self.frame_forgot_passwd = QtWidgets.QFrame(self.frame_form_place)
        self.frame_forgot_passwd.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_forgot_passwd.setStyleSheet("border:none;")
        self.frame_forgot_passwd.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_forgot_passwd.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_forgot_passwd.setObjectName("frame_forgot_passwd")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_forgot_passwd)
        self.horizontalLayout_3.setContentsMargins(0, 10, 30, 0)
        self.horizontalLayout_3.setSpacing(140)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.forgotpasswd_btn = QtWidgets.QPushButton(self.frame_forgot_passwd)
        self.forgotpasswd_btn.setStyleSheet("#forgotpasswd_btn {\n"
"    font: 75 10pt \"Playfair Display\";\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"#forgotpasswd_btn:hover {\n"
"    font: 75 10pt \"Playfair Display\";\n"
"    color: red;\n"
"}")
        self.forgotpasswd_btn.setObjectName("forgotpasswd_btn")
        self.horizontalLayout_3.addWidget(self.forgotpasswd_btn)
        self.signup_btn = QtWidgets.QPushButton(self.frame_forgot_passwd)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.signup_btn.sizePolicy().hasHeightForWidth())
        self.signup_btn.setSizePolicy(sizePolicy)
        self.signup_btn.setMaximumSize(QtCore.QSize(90, 30))
        self.signup_btn.setStyleSheet("#signin_btn {\n"
"    font: 75 10pt \"Playfair Display\";\n"
"    border: 2px solid black;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"#signin_btn:hover { \n"
"    font: 75 10pt \"Playfair Display\";\n"
"    border: 2px solid black;\n"
"    background-color: rgb(51, 0, 138);\n"
"    color: white;\n"
"}")
        self.signup_btn.setObjectName("signin_btn")
        self.horizontalLayout_3.addWidget(self.signup_btn)
        self.verticalLayout_3.addWidget(self.frame_forgot_passwd)
        self.verticalLayout_2.addWidget(self.frame_form_place)
        self.emp_frame_7 = QtWidgets.QFrame(self.frame_signinform)
        self.emp_frame_7.setMaximumSize(QtCore.QSize(16777215, 100))
        self.emp_frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.emp_frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.emp_frame_7.setObjectName("emp_frame_7")
        self.verticalLayout_2.addWidget(self.emp_frame_7)
        self.horizontalLayout_2.addWidget(self.frame_signinform)
        self.emp_frame_5 = QtWidgets.QFrame(self.frame_signup)
        self.emp_frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.emp_frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.emp_frame_5.setObjectName("emp_frame_5")
        self.horizontalLayout_2.addWidget(self.emp_frame_5)
        self.frame_signin = QtWidgets.QFrame(self.content)
        self.frame_signin.setGeometry(QtCore.QRect(0, 0, 1951, 871))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_signin.sizePolicy().hasHeightForWidth())
        self.frame_signin.setSizePolicy(sizePolicy)
        self.frame_signin.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_signin.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_signin.setObjectName("frame_signin")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_signin)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.emp_frame_10 = QtWidgets.QFrame(self.frame_signin)
        self.emp_frame_10.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.emp_frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.emp_frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.emp_frame_10.setObjectName("emp_frame_10")
        self.horizontalLayout_9.addWidget(self.emp_frame_10)
        self.frame_signinform_2 = QtWidgets.QFrame(self.frame_signin)
        self.frame_signinform_2.setMaximumSize(QtCore.QSize(450, 16777215))
        self.frame_signinform_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_signinform_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_signinform_2.setObjectName("frame_signinform_2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_signinform_2)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.emp_frame_12 = QtWidgets.QFrame(self.frame_signinform_2)
        self.emp_frame_12.setMaximumSize(QtCore.QSize(16777215, 150))
        self.emp_frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.emp_frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.emp_frame_12.setObjectName("emp_frame_12")
        self.verticalLayout_10.addWidget(self.emp_frame_12)
        self.frame_form_place_2 = QtWidgets.QFrame(self.frame_signinform_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_form_place_2.sizePolicy().hasHeightForWidth())
        self.frame_form_place_2.setSizePolicy(sizePolicy)
        self.frame_form_place_2.setMaximumSize(QtCore.QSize(16777215, 550))
        self.frame_form_place_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: 2px solid black;\n"
"border-radius: 20px;")
        self.frame_form_place_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_form_place_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_form_place_2.setObjectName("frame_form_place_2")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_form_place_2)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_title_2 = QtWidgets.QFrame(self.frame_form_place_2)
        self.frame_title_2.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_title_2.setStyleSheet("border:none;")
        self.frame_title_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_title_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title_2.setObjectName("frame_title_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_title_2)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.emp_frame_13 = QtWidgets.QFrame(self.frame_title_2)
        self.emp_frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.emp_frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.emp_frame_13.setObjectName("emp_frame_13")
        self.horizontalLayout_10.addWidget(self.emp_frame_13)
        self.title_2 = QtWidgets.QFrame(self.frame_title_2)
        self.title_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.title_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.title_2.setObjectName("title_2")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.title_2)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.signin_2 = QtWidgets.QLabel(self.title_2)
        self.signin_2.setStyleSheet("font: 75 22pt \"Playfair Display\";")
        self.signin_2.setAlignment(QtCore.Qt.AlignCenter)
        self.signin_2.setObjectName("signin_2")
        self.verticalLayout_12.addWidget(self.signin_2)
        self.horizontalLayout_10.addWidget(self.title_2)
        self.emp_frame_14 = QtWidgets.QFrame(self.frame_title_2)
        self.emp_frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.emp_frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.emp_frame_14.setObjectName("emp_frame_14")
        self.horizontalLayout_10.addWidget(self.emp_frame_14)
        self.verticalLayout_11.addWidget(self.frame_title_2)
        self.frame_name_2 = QtWidgets.QFrame(self.frame_form_place_2)
        self.frame_name_2.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_name_2.setStyleSheet("border:none;")
        self.frame_name_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_name_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_name_2.setObjectName("frame_name_2")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_name_2)
        self.verticalLayout_13.setContentsMargins(30, 10, 30, 0)
        self.verticalLayout_13.setSpacing(10)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.nameinput_text_2 = QtWidgets.QLabel(self.frame_name_2)
        self.nameinput_text_2.setStyleSheet("font: 75 10pt \"Arial\";")
        self.nameinput_text_2.setObjectName("nameinput_text_2")
        self.verticalLayout_13.addWidget(self.nameinput_text_2)
        self.nameinput_place_2 = QtWidgets.QPlainTextEdit(self.frame_name_2)
        self.nameinput_place_2.setStyleSheet("border: 2px solid black;\n"
"border-radius:7px;")
        self.nameinput_place_2.setObjectName("nameinput_place_2")
        self.verticalLayout_13.addWidget(self.nameinput_place_2)
        self.verticalLayout_11.addWidget(self.frame_name_2)
        self.frame_password_2 = QtWidgets.QFrame(self.frame_form_place_2)
        self.frame_password_2.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_password_2.setStyleSheet("border:none;")
        self.frame_password_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_password_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_password_2.setObjectName("frame_password_2")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_password_2)
        self.verticalLayout_14.setContentsMargins(30, 10, 30, 0)
        self.verticalLayout_14.setSpacing(10)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.password_text_2 = QtWidgets.QLabel(self.frame_password_2)
        self.password_text_2.setStyleSheet("font: 75 10pt \"Arial\";")
        self.password_text_2.setObjectName("password_text_2")
        self.verticalLayout_14.addWidget(self.password_text_2)
        self.passwordinput_place_2 = QtWidgets.QLineEdit(self.frame_password_2)
        self.passwordinput_place_2.setStyleSheet("border: 2px solid black;\n"
"border-radius:7px;")
        self.passwordinput_place_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordinput_place_2.setObjectName("passwordinput_place_2")
        self.verticalLayout_14.addWidget(self.passwordinput_place_2)
        self.verticalLayout_11.addWidget(self.frame_password_2)
        self.frame_forgot_passwd_2 = QtWidgets.QFrame(self.frame_form_place_2)
        self.frame_forgot_passwd_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_forgot_passwd_2.setStyleSheet("border:none;")
        self.frame_forgot_passwd_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_forgot_passwd_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_forgot_passwd_2.setObjectName("frame_forgot_passwd_2")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_forgot_passwd_2)
        self.horizontalLayout_11.setContentsMargins(0, 10, 30, 0)
        self.horizontalLayout_11.setSpacing(140)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.forgotpasswd_btn_2 = QtWidgets.QPushButton(self.frame_forgot_passwd_2)
        self.forgotpasswd_btn_2.setStyleSheet("#forgotpasswd_btn_2 {\n"
"    font: 75 10pt \"Playfair Display\";\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"#forgotpasswd_btn_2:hover {\n"
"    font: 75 10pt \"Playfair Display\";\n"
"    color: red;\n"
"}")
        self.forgotpasswd_btn_2.setObjectName("forgotpasswd_btn_2")
        self.horizontalLayout_11.addWidget(self.forgotpasswd_btn_2)
        self.signup_btn_2 = QtWidgets.QPushButton(self.frame_forgot_passwd_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.signup_btn_2.sizePolicy().hasHeightForWidth())
        self.signup_btn_2.setSizePolicy(sizePolicy)
        self.signup_btn_2.setMaximumSize(QtCore.QSize(90, 30))
        self.signup_btn_2.setStyleSheet("#signin_btn_2 {\n"
"    font: 75 10pt \"Playfair Display\";\n"
"    border: 2px solid black;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"#signin_btn_2:hover { \n"
"    font: 75 10pt \"Playfair Display\";\n"
"    border: 2px solid black;\n"
"    background-color: rgb(51, 0, 138);\n"
"    color: white;\n"
"}")
        self.signup_btn_2.setObjectName("signin_btn_2")
        self.horizontalLayout_11.addWidget(self.signup_btn_2)
        self.verticalLayout_11.addWidget(self.frame_forgot_passwd_2)
        self.frame_signinby_2 = QtWidgets.QFrame(self.frame_form_place_2)
        self.frame_signinby_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_signinby_2.setStyleSheet("border:none;\n"
" font: 75 8pt \"Arial\";")
        self.frame_signinby_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_signinby_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_signinby_2.setObjectName("frame_signinby_2")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_signinby_2)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.emp_frame_15 = QtWidgets.QFrame(self.frame_signinby_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.emp_frame_15.sizePolicy().hasHeightForWidth())
        self.emp_frame_15.setSizePolicy(sizePolicy)
        self.emp_frame_15.setMaximumSize(QtCore.QSize(100, 16777215))
        self.emp_frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.emp_frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.emp_frame_15.setObjectName("emp_frame_15")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.emp_frame_15)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.horizontalLayout_12.addWidget(self.emp_frame_15)
        self.frame_signinwith_2 = QtWidgets.QFrame(self.frame_signinby_2)
        self.frame_signinwith_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_signinwith_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_signinwith_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_signinwith_2.setObjectName("frame_signinwith_2")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_signinwith_2)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.frame_email_2 = QtWidgets.QFrame(self.frame_signinwith_2)
        self.frame_email_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_email_2.setStyleSheet("border: 2px solid black;\n"
"border-radius: 10px;")
        self.frame_email_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_email_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_email_2.setObjectName("frame_email_2")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_email_2)
        self.horizontalLayout_13.setContentsMargins(10, 0, 12, 0)
        self.horizontalLayout_13.setSpacing(25)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.logo_email_2 = QtWidgets.QLabel(self.frame_email_2)
        self.logo_email_2.setMaximumSize(QtCore.QSize(20, 15))
        self.logo_email_2.setStyleSheet("border: none;")
        self.logo_email_2.setText("")
        self.logo_email_2.setPixmap(QtGui.QPixmap("pic\logo\email.png"))
        self.logo_email_2.setScaledContents(True)
        self.logo_email_2.setObjectName("logo_email_2")
        self.horizontalLayout_13.addWidget(self.logo_email_2)
        self.text_email_2 = QtWidgets.QLabel(self.frame_email_2)
        self.text_email_2.setMaximumSize(QtCore.QSize(110, 16777215))
        self.text_email_2.setStyleSheet("border:none;")
        self.text_email_2.setObjectName("text_email_2")
        self.horizontalLayout_13.addWidget(self.text_email_2)
        self.verticalLayout_16.addWidget(self.frame_email_2)
        self.frame_fb_2 = QtWidgets.QFrame(self.frame_signinwith_2)
        self.frame_fb_2.setStyleSheet("border: 2px solid black;\n"
"border-radius: 10px;")
        self.frame_fb_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_fb_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_fb_2.setObjectName("frame_fb_2")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_fb_2)
        self.horizontalLayout_14.setContentsMargins(8, 0, 0, 0)
        self.horizontalLayout_14.setSpacing(10)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.logo_fb_2 = QtWidgets.QLabel(self.frame_fb_2)
        self.logo_fb_2.setMaximumSize(QtCore.QSize(25, 20))
        self.logo_fb_2.setStyleSheet("border: none;")
        self.logo_fb_2.setText("")
        self.logo_fb_2.setPixmap(QtGui.QPixmap("pic\logo\\facebook.png"))
        self.logo_fb_2.setScaledContents(True)
        self.logo_fb_2.setObjectName("logo_fb_2")
        self.horizontalLayout_14.addWidget(self.logo_fb_2)
        self.text_fb_2 = QtWidgets.QLabel(self.frame_fb_2)
        self.text_fb_2.setStyleSheet("border: none;")
        self.text_fb_2.setObjectName("text_fb_2")
        self.horizontalLayout_14.addWidget(self.text_fb_2)
        self.verticalLayout_16.addWidget(self.frame_fb_2)
        self.horizontalLayout_12.addWidget(self.frame_signinwith_2)
        self.emp_frame_16 = QtWidgets.QFrame(self.frame_signinby_2)
        self.emp_frame_16.setMaximumSize(QtCore.QSize(100, 16777215))
        self.emp_frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.emp_frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.emp_frame_16.setObjectName("emp_frame_16")
        self.horizontalLayout_12.addWidget(self.emp_frame_16)
        self.verticalLayout_11.addWidget(self.frame_signinby_2)
        self.verticalLayout_10.addWidget(self.frame_form_place_2)
        self.emp_frame_17 = QtWidgets.QFrame(self.frame_signinform_2)
        self.emp_frame_17.setMaximumSize(QtCore.QSize(16777215, 150))
        self.emp_frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.emp_frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.emp_frame_17.setObjectName("emp_frame_17")
        self.verticalLayout_10.addWidget(self.emp_frame_17)
        self.horizontalLayout_9.addWidget(self.frame_signinform_2)
        self.emp_frame_18 = QtWidgets.QFrame(self.frame_signin)
        self.emp_frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.emp_frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.emp_frame_18.setObjectName("emp_frame_18")
        self.horizontalLayout_9.addWidget(self.emp_frame_18)
        self.image = QtWidgets.QLabel(self.content)
        self.image.setEnabled(True)
        self.image.setGeometry(QtCore.QRect(0, 0, 1951, 861))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image.sizePolicy().hasHeightForWidth())
        self.image.setSizePolicy(sizePolicy)
        self.image.setMaximumSize(QtCore.QSize(1777215, 1777215))
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap("pic\\background\Background.png"))
        self.image.setScaledContents(True)
        self.image.setObjectName("image")
        self.image.raise_()
        self.frame_signup.raise_()
        self.frame_signin.raise_()
        self.frame_signin.hide()
        self.btnsignup.hide()
        self.verticalLayout.addWidget(self.content)
        # Tạo một QLabel để hiển thị thông báo lỗi
        self.label = QtWidgets.QLabel()
        self.label.setGeometry(830, 450, 500, 100)
        self.label.setStyleSheet("font: 75 12pt \"Playfair Display\";\nmargin:auto;")
        self.label.hide()  # Ẩn ban đầu
        self.btnsignin.clicked.connect(self.change_to_signin)
        self.btnsignup.clicked.connect(self.change_to_signup)
        self.signup_btn_2.clicked.connect(self.confirm_signin)
        self.signup_btn.clicked.connect(self.confirm_signup)

        SignWindow.setCentralWidget(self.frame_sign_in)

        self.retranslateUi(SignWindow)
        QtCore.QMetaObject.connectSlotsByName(SignWindow)

    def change_to_signup(self):
        """
        Chuyển đổi giao diện từ đăng nhập (Sign In) sang đăng ký (Sign Up).

        Phương thức này thực hiện các bước sau:

                1. Ẩn khung đăng nhập (`self.frame_signin`).
                2. Hiển thị khung đăng ký (`self.frame_signup`).
                3. Hiển thị nút chuyển sang đăng nhập (`self.btnsignin`).
                4. Ẩn nút chuyển sang đăng ký (`self.btnsignup`).

        Lưu ý:
                - Phương thức này giả định rằng các thành phần giao diện `self.frame_signin`, `self.frame_signup`,
                        `self.btnsignin` và `self.btnsignup` đã được khai báo và thiết lập trước đó.
        """
        self.frame_signin.hide()
        self.frame_signup.show()
        self.btnsignin.show()
        self.btnsignup.hide()

    def change_to_signin(self):
        """
        Chuyển đổi giao diện từ đăng ký (Sign Up) sang đăng nhập (Sign In).

        Phương thức này thực hiện các bước sau:

                1. Ẩn khung đăng ký (`self.frame_signup`).
                2. Hiển thị khung đăng nhập (`self.frame_signin`).
                3. Hiển thị nút chuyển sang đăng ký (`self.btnsignup`).
                4. Ẩn nút chuyển sang đăng nhập (`self.btnsignin`).

        Lưu ý:
                - Phương thức này giả định rằng các thành phần giao diện `self.frame_signup`, `self.frame_signin`,
                        `self.btnsignup` và `self.btnsignin` đã được khai báo và thiết lập trước đó.
        """
        self.frame_signup.hide()
        self.frame_signin.show()
        self.btnsignup.show()
        self.btnsignin.hide()

    def show_message(self, message):
        """
        Hiển thị thông báo lỗi.

        Args:
                message (str): Nội dung thông báo lỗi cần hiển thị.
        """
        # Hiển thị thông báo lỗi
        self.label.setText(message)
        self.label.show()

    def hide_message(self):
        """
        Ẩn thông báo lỗi
        """
        # Ẩn thông báo lỗi
        self.label.hide()

    def confirm_signin(self):
        """
        Xác nhận đăng nhập.

        Thực hiện các bước sau:

                1. Truy vấn cơ sở dữ liệu để lấy thông tin tên người dùng và mật khẩu.
                2. Lấy thông tin đăng nhập từ các trường nhập liệu.
                3. Kiểm tra xem các trường có được điền đầy đủ không.
                4. So sánh thông tin đăng nhập với dữ liệu từ cơ sở dữ liệu.
                5. Hiển thị thông báo thành công hoặc thất bại.
                6. Nếu đăng nhập thành công, chờ 2 giây và gọi phương thức `wait`.
                7. Đóng kết nối cơ sở dữ liệu.

        Raises:
                pymysql.Error: Nếu có lỗi xảy ra trong quá trình truy vấn cơ sở dữ liệu.
        """
        db = Database()
        info = db.query("SELECT cust_name, cust_password FROM customer")
        name = self.nameinput_place_2.toPlainText()
        passwd = self.passwordinput_place_2.text()
        if name == "" or passwd == "":
            self.show_message("Please fill in all the fields")
            return
        flag = 0
        for i in range (len(info)):
            lst = list(info[i].values())
            if name == lst[0] and passwd == lst[1]:
                self.show_message("Sign in Successful")
                flag = 1
                break
        if flag == 0:
            self.show_message("Your name or your password may not match!")
        else:
            QTimer.singleShot(2000, self.wait)
        db.connection.close()

    def confirm_signup(self):
        """
        Xác nhận đăng ký.

        Thực hiện các bước sau:

                1. Truy vấn cơ sở dữ liệu để lấy thông tin người dùng hiện có.
                2. Lấy thông tin đăng ký từ các trường nhập liệu.
                3. Kiểm tra xem các trường có được điền đầy đủ không.
                4. Kiểm tra xem email đã tồn tại chưa.
                5. Thêm thông tin người dùng mới vào cơ sở dữ liệu.
                6. Hiển thị thông báo thành công.
                7. Chờ 2 giây và gọi phương thức `wait`.
                8. Đóng kết nối cơ sở dữ liệu.

        Raises:
                pymysql.Error: Nếu có lỗi xảy ra trong quá trình truy vấn hoặc thêm dữ liệu vào cơ sở dữ liệu.
        """
        db = Database()
        info = db.query("SELECT * FROM customer")
        name = self.nameinput_place.toPlainText()
        email = self.emailinput_place_3.toPlainText()
        passwd = self.passwordinput_place.text()
        if name == "" or email == "" or passwd == "":
            self.show_message("Please fill in all the fields")
            return
        for i in range (len(info)):
            lst = list(info[i].values())
            if email == lst[2]:
                self.show_message("Your email may already exist!")
                return
        
        db.execute("INSERT INTO customer(cust_id, cust_name, email, cust_password) VALUES (%s, %s, %s, %s)", (len(info)+1, name, email, passwd))
        self.show_message("Sign up Successfully") 
        QTimer.singleShot(2000, self.wait)
        db.connection.close()

    def wait(self):
        """
        Chờ 2 giây trước khi chuyển đến trang thông tin tài khoản (`Ui_AccPageWindow`).

        Thực hiện các bước sau:

                1. Ẩn thông báo đăng nhập thành công (nếu có).
                2. Tạo một đối tượng cửa sổ mới (`self.OtherWindow`) thuộc lớp `QtWidgets.QMainWindow`.
                3. Tạo một đối tượng giao diện (`self.ui`) thuộc lớp `Ui_AccPageWindow`.
                4. Thiết lập giao diện cho cửa sổ mới bằng `self.ui.setupUi(self.OtherWindow)`.
                5. Hiển thị cửa sổ mới (`self.OtherWindow.show()`).
        """
        self.hide_message()
        self.OtherWindow = QtWidgets.QMainWindow()
        self.ui = Ui_AccPageWindow()
        self.ui.setupUi(self.OtherWindow)
        self.OtherWindow.show()

    def retranslateUi(self, SignWindow):
        """
        Cài đặt lại nội dung văn bản cho các thành phần giao diện.

        Args:
            SignWindow (QMainWindow): Đối tượng cửa sổ đăng nhập cần cài đặt lại nội dung.
        """
        _translate = QtCore.QCoreApplication.translate
        SignWindow.setWindowTitle(_translate("SignWindow", "SignWindow"))
        self.btnsignup.setText(_translate("SignWindow", "Sign up"))
        self.btnsignin.setText(_translate("SignWindow", "Sign in"))
        self.help.setText(_translate("SignWindow", "Help"))
        self.signin.setText(_translate("SignWindow", "Sign up"))
        self.nameinput_text.setText(_translate("SignWindow", "Enter your name:"))
        self.email_text_3.setText(_translate("SignWindow", "Enter your email:"))
        self.password_text.setText(_translate("SignWindow", "Enter your password:"))
        self.forgotpasswd_btn.setText(_translate("SignWindow", "Forgot password?"))
        self.signup_btn.setText(_translate("SignWindow", "Sign Up"))
        self.signin_2.setText(_translate("SignWindow", "Sign In"))
        self.nameinput_text_2.setText(_translate("SignWindow", "Enter your name:"))
        self.password_text_2.setText(_translate("SignWindow", "Enter your password:"))
        self.forgotpasswd_btn_2.setText(_translate("SignWindow", "Forgot password?"))
        self.signup_btn_2.setText(_translate("SignWindow", "Sign In"))
        self.text_email_2.setText(_translate("SignWindow", "Sign in with Email"))
        self.text_fb_2.setText(_translate("SignWindow", "Sign in with Facebook"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SignWindow = QtWidgets.QMainWindow()
    ui = Ui_SignInUpWindow()
    ui.setupUi(SignWindow)
    SignWindow.show()
    sys.exit(app.exec_())
