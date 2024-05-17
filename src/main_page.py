import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from sign_inup import Ui_SignInUpWindow

class Ui_MainPageWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1944, 1204)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QFrame(self.centralwidget)
        self.header.setMaximumSize(QtCore.QSize(16777215, 100))
        self.header.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_logo = QtWidgets.QFrame(self.header)
        self.frame_logo.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frame_logo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_logo.setObjectName("frame_logo")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_logo)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.logo = QtWidgets.QLabel(self.frame_logo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMaximumSize(QtCore.QSize(100, 100))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("pic\logo\Logo-light_mode.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.horizontalLayout_2.addWidget(self.logo)
        self.horizontalLayout.addWidget(self.frame_logo)
        self.frame_2 = QtWidgets.QFrame(self.header)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout.addWidget(self.frame_2)
        self.options = QtWidgets.QFrame(self.header)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.options.sizePolicy().hasHeightForWidth())
        self.options.setSizePolicy(sizePolicy)
        self.options.setMaximumSize(QtCore.QSize(200, 16777215))
        self.options.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.options.setFrameShadow(QtWidgets.QFrame.Raised)
        self.options.setObjectName("options")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.options)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_signinup = QtWidgets.QPushButton(self.options)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_signinup.sizePolicy().hasHeightForWidth())
        self.frame_signinup.setSizePolicy(sizePolicy)
        self.frame_signinup.setMaximumSize(QtCore.QSize(130, 50))
        self.frame_signinup.setStyleSheet("#frame_signinup {\n"
"    font: 75 10pt \"Playfair Display\";\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 2px solid black;\n"
"    border-radius: 20px;\n"
"}\n"
"#frame_signinup:hover {\n"
"    font: 75 10pt \"Playfair Display\";\n"
"    background-color: rgb(12, 18, 106);\n"
"    color:white;\n"
"    border: 2px solid black;\n"
"    border-radius: 20px;\n"
"\n"
"}\n"
"")
        self.frame_signinup.setObjectName("frame_signinup")
        self.horizontalLayout_3.addWidget(self.frame_signinup)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        
        self.horizontalLayout.addWidget(self.options)
        self.verticalLayout.addWidget(self.header)
        self.content = QtWidgets.QFrame(self.centralwidget)
        self.content.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.image = QtWidgets.QLabel(self.content)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image.sizePolicy().hasHeightForWidth())
        self.image.setSizePolicy(sizePolicy)
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap("pic\\background\Bgd.png"))
        self.image.setScaledContents(True)
        self.image.setObjectName("image")
        self.horizontalLayout_4.addWidget(self.image)
        self.verticalLayout.addWidget(self.content)
        MainWindow.setCentralWidget(self.centralwidget)
        self.frame_signinup.clicked.connect(self.signinup)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def signinup(self):
        self.OtherWindow = QtWidgets.QMainWindow()
        self.ui = Ui_SignInUpWindow()
        self.ui.setupUi(self.OtherWindow)
        self.OtherWindow.show()
        MainWindow.hide()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.frame_signinup.setText(_translate("MainWindow", "Sign in/Sign up"))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainPageWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
