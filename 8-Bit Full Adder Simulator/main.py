from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from PyQt5.QtCore import *
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    sumA = 0
    sumB = 0
    carryInValue = 0
    total = 0
    result = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1051, 512)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 30, 60, 101))
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber.setDigitCount(1)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(70, 30, 60, 101))
        self.lcdNumber_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_2.setDigitCount(1)
        self.lcdNumber_2.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_3.setGeometry(QtCore.QRect(130, 30, 60, 101))
        self.lcdNumber_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_3.setDigitCount(1)
        self.lcdNumber_3.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_4.setGeometry(QtCore.QRect(190, 30, 60, 101))
        self.lcdNumber_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_4.setDigitCount(1)
        self.lcdNumber_4.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.lcdNumber_5 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_5.setGeometry(QtCore.QRect(250, 30, 60, 101))
        self.lcdNumber_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_5.setDigitCount(1)
        self.lcdNumber_5.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_5.setObjectName("lcdNumber_5")
        self.lcdNumber_6 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_6.setGeometry(QtCore.QRect(310, 30, 60, 101))
        self.lcdNumber_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_6.setDigitCount(1)
        self.lcdNumber_6.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_6.setObjectName("lcdNumber_6")
        self.lcdNumber_7 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_7.setGeometry(QtCore.QRect(370, 30, 60, 101))
        self.lcdNumber_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_7.setDigitCount(1)
        self.lcdNumber_7.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_7.setObjectName("lcdNumber_7")
        self.lcdNumber_8 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_8.setGeometry(QtCore.QRect(430, 30, 60, 101))
        self.lcdNumber_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_8.setDigitCount(1)
        self.lcdNumber_8.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_8.setObjectName("lcdNumber_8")
        self.lcdNumber_13 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_13.setGeometry(QtCore.QRect(800, 30, 60, 101))
        self.lcdNumber_13.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_13.setDigitCount(1)
        self.lcdNumber_13.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_13.setObjectName("lcdNumber_13")
        self.lcdNumber_9 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_9.setGeometry(QtCore.QRect(560, 30, 60, 101))
        self.lcdNumber_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_9.setDigitCount(1)
        self.lcdNumber_9.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_9.setObjectName("lcdNumber_9")
        self.lcdNumber_10 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_10.setGeometry(QtCore.QRect(620, 30, 60, 101))
        self.lcdNumber_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_10.setDigitCount(1)
        self.lcdNumber_10.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_10.setObjectName("lcdNumber_10")
        self.lcdNumber_11 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_11.setGeometry(QtCore.QRect(680, 30, 60, 101))
        self.lcdNumber_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_11.setDigitCount(1)
        self.lcdNumber_11.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_11.setObjectName("lcdNumber_11")
        self.lcdNumber_14 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_14.setGeometry(QtCore.QRect(860, 30, 60, 101))
        self.lcdNumber_14.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_14.setDigitCount(1)
        self.lcdNumber_14.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_14.setObjectName("lcdNumber_14")
        self.lcdNumber_16 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_16.setGeometry(QtCore.QRect(980, 30, 60, 101))
        self.lcdNumber_16.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_16.setDigitCount(1)
        self.lcdNumber_16.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_16.setObjectName("lcdNumber_16")
        self.lcdNumber_15 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_15.setGeometry(QtCore.QRect(920, 30, 60, 101))
        self.lcdNumber_15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_15.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_15.setDigitCount(1)
        self.lcdNumber_15.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_15.setObjectName("lcdNumber_15")
        self.lcdNumber_12 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_12.setGeometry(QtCore.QRect(740, 30, 60, 101))
        self.lcdNumber_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_12.setDigitCount(1)
        self.lcdNumber_12.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_12.setObjectName("lcdNumber_12")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(33, 135, 16, 17))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(93, 135, 16, 17))
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(153, 135, 16, 17))
        self.checkBox_3.setText("")
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(213, 135, 16, 17))
        self.checkBox_4.setText("")
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(273, 135, 16, 17))
        self.checkBox_5.setText("")
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_6.setGeometry(QtCore.QRect(333, 135, 16, 17))
        self.checkBox_6.setText("")
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_7.setGeometry(QtCore.QRect(393, 135, 16, 17))
        self.checkBox_7.setText("")
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_8.setGeometry(QtCore.QRect(453, 135, 16, 17))
        self.checkBox_8.setText("")
        self.checkBox_8.setObjectName("checkBox_8")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 30, 481, 131))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: lightblue")
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(2)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")
        self.checkBox_9 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_9.setGeometry(QtCore.QRect(583, 135, 16, 17))
        self.checkBox_9.setText("")
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_10.setGeometry(QtCore.QRect(643, 135, 16, 17))
        self.checkBox_10.setText("")
        self.checkBox_10.setObjectName("checkBox_10")
        self.checkBox_11 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_11.setGeometry(QtCore.QRect(703, 135, 16, 17))
        self.checkBox_11.setText("")
        self.checkBox_11.setObjectName("checkBox_11")
        self.checkBox_12 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_12.setGeometry(QtCore.QRect(763, 135, 16, 17))
        self.checkBox_12.setText("")
        self.checkBox_12.setObjectName("checkBox_12")
        self.checkBox_14 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_14.setGeometry(QtCore.QRect(883, 135, 16, 17))
        self.checkBox_14.setText("")
        self.checkBox_14.setObjectName("checkBox_14")
        self.checkBox_15 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_15.setGeometry(QtCore.QRect(943, 135, 16, 17))
        self.checkBox_15.setText("")
        self.checkBox_15.setObjectName("checkBox_15")
        self.checkBox_16 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_16.setGeometry(QtCore.QRect(1003, 135, 16, 17))
        self.checkBox_16.setText("")
        self.checkBox_16.setObjectName("checkBox_16")
        self.checkBox_13 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_13.setGeometry(QtCore.QRect(823, 135, 16, 17))
        self.checkBox_13.setText("")
        self.checkBox_13.setObjectName("checkBox_13")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(560, 30, 481, 131))
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setStyleSheet("background-color: lightblue")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(2)
        self.frame_2.setMidLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(200, 190, 650, 150))
        self.frame_3.setAutoFillBackground(False)
        self.frame_3.setStyleSheet("background-color: lightblue")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setLineWidth(2)
        self.frame_3.setObjectName("frame_3")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(120, 50, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(40, 5, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(590, 5, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(590, 60, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(30, 130, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setGeometry(QtCore.QRect(365, 130, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(240, 160, 20, 30))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(790, 160, 20, 30))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(910, 200, 72, 135))
        self.frame_4.setAutoFillBackground(False)
        self.frame_4.setStyleSheet("background-color: lightblue")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setLineWidth(2)
        self.frame_4.setObjectName("frame_4")
        self.lcdNumber_17 = QtWidgets.QLCDNumber(self.frame_4)
        self.lcdNumber_17.setGeometry(QtCore.QRect(7, 5, 60, 101))
        self.lcdNumber_17.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_17.setDigitCount(1)
        self.lcdNumber_17.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_17.setObjectName("lcdNumber_17")
        self.checkBox_17 = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox_17.setGeometry(QtCore.QRect(30, 110, 16, 17))
        self.checkBox_17.setText("")
        self.checkBox_17.setObjectName("checkBox_17")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(850, 260, 60, 3))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(375, 370, 411, 111))
        self.frame_5.setAutoFillBackground(False)
        self.frame_5.setStyleSheet("background-color: lightblue")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_5.setLineWidth(2)
        self.frame_5.setMidLineWidth(0)
        self.frame_5.setObjectName("frame_5")
        self.lcdNumber_18 = QtWidgets.QLCDNumber(self.frame_5)
        self.lcdNumber_18.setGeometry(QtCore.QRect(2, 2, 401, 101))
        self.lcdNumber_18.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_18.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber_18.setDigitCount(8)
        self.lcdNumber_18.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_18.setProperty("value", 99999999.0)
        self.lcdNumber_18.setObjectName("lcdNumber_18")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(570, 340, 20, 30))
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(2)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setObjectName("line_4")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(230, 370, 72, 111))
        self.frame_6.setAutoFillBackground(False)
        self.frame_6.setStyleSheet("background-color: lightblue")
        self.frame_6.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_6.setLineWidth(2)
        self.frame_6.setObjectName("frame_6")
        self.lcdNumber_28 = QtWidgets.QLCDNumber(self.frame_6)
        self.lcdNumber_28.setGeometry(QtCore.QRect(7, 5, 60, 101))
        self.lcdNumber_28.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_28.setDigitCount(1)
        self.lcdNumber_28.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_28.setObjectName("lcdNumber_28")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(255, 340, 20, 30))
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setLineWidth(2)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setObjectName("line_5")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 280, 121, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(30, 330, 121, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(30, 430, 121, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(30, 300, 121, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(30, 350, 121, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(30, 450, 121, 16))
        self.label_14.setObjectName("label_14")
        self.frame_7 = QtWidgets.QFrame(self.centralwidget)
        self.frame_7.setGeometry(QtCore.QRect(20, 270, 151, 211))
        self.frame_7.setAutoFillBackground(True)
        self.frame_7.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_7.setLineWidth(1)
        self.frame_7.setObjectName("frame_7")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(30, 380, 121, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(30, 400, 121, 16))
        self.label_16.setObjectName("label_16")
        self.frame_7.raise_()
        self.frame_4.raise_()
        self.frame.raise_()
        self.frame_2.raise_()
        self.lcdNumber.raise_()
        self.lcdNumber_2.raise_()
        self.lcdNumber_3.raise_()
        self.lcdNumber_4.raise_()
        self.lcdNumber_5.raise_()
        self.lcdNumber_6.raise_()
        self.lcdNumber_7.raise_()
        self.lcdNumber_8.raise_()
        self.lcdNumber_13.raise_()
        self.lcdNumber_9.raise_()
        self.lcdNumber_10.raise_()
        self.lcdNumber_11.raise_()
        self.lcdNumber_14.raise_()
        self.lcdNumber_16.raise_()
        self.lcdNumber_15.raise_()
        self.lcdNumber_12.raise_()
        self.checkBox.raise_()
        self.checkBox_2.raise_()
        self.checkBox_3.raise_()
        self.checkBox_4.raise_()
        self.checkBox_5.raise_()
        self.checkBox_6.raise_()
        self.checkBox_7.raise_()
        self.checkBox_8.raise_()
        self.checkBox_9.raise_()
        self.checkBox_10.raise_()
        self.checkBox_11.raise_()
        self.checkBox_12.raise_()
        self.checkBox_14.raise_()
        self.checkBox_15.raise_()
        self.checkBox_16.raise_()
        self.checkBox_13.raise_()
        self.frame_3.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.frame_5.raise_()
        self.line_4.raise_()
        self.frame_6.raise_()
        self.line_5.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1051, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # INPUT A SIGNALS

        self.checkBox.stateChanged.connect(self.lcdOneA)
        self.checkBox_2.stateChanged.connect(self.lcdTwoA)
        self.checkBox_3.stateChanged.connect(self.lcdThreeA)
        self.checkBox_4.stateChanged.connect(self.lcdFourA)
        self.checkBox_5.stateChanged.connect(self.lcdFiveA)
        self.checkBox_6.stateChanged.connect(self.lcdSixA)
        self.checkBox_7.stateChanged.connect(self.lcdSevenA)
        self.checkBox_8.stateChanged.connect(self.lcdEightA)

        # INPUT B SIGNALS

        self.checkBox_9.stateChanged.connect(self.lcdOneB)
        self.checkBox_10.stateChanged.connect(self.lcdTwoB)
        self.checkBox_11.stateChanged.connect(self.lcdThreeB)
        self.checkBox_12.stateChanged.connect(self.lcdFourB)
        self.checkBox_13.stateChanged.connect(self.lcdFiveB)
        self.checkBox_14.stateChanged.connect(self.lcdSixB)
        self.checkBox_15.stateChanged.connect(self.lcdSevenB)
        self.checkBox_16.stateChanged.connect(self.lcdEightB)

        # SUM SIGNALS

        self.timer = QTimer()
        self.timer.timeout.connect(self.fullAdderLogic)
        self.timer.start(1)

        self.checkBox_17.stateChanged.connect(self.carryIn)

    # SUM I/O

    def updateTotalLabel(self):
        stringResult = format(self.result, '08b')
        self.label_16.setText(str(self.result))
        self.lcdNumber_18.display(stringResult)
        self.label_14.setText(str(self.total))

    def fullAdderLogic(self):
        self.result = 0
        self.total = self.carryInValue + self.sumA + self.sumB
        if self.total >= 256: # OVERFLOW
            self.lcdNumber_28.display(1) # Carry out = 1
            self.result = self.total - 255
            self.updateTotalLabel()
        else:
            self.lcdNumber_28.display(0)
            self.result = self.total
            self.updateTotalLabel()

    def carryIn(self):
        if self.checkBox_17.isChecked():
            self.lcdNumber_17.display(1)
            self.carryInValue += 1
        else:
            self.lcdNumber_17.display(0)
            self.carryInValue -= 1

    # INPUT A I/O

    def updateSumALabel(self):
        self.label_12.setText(str(self.sumA))

    def lcdOneA(self):
        if self.checkBox.isChecked():
            self.lcdNumber.display(1)
            self.sumA += 128
        else:
            self.lcdNumber.display(0)
            self.sumA -= 128
        self.updateSumALabel()

    def lcdTwoA(self):
        if self.checkBox_2.isChecked():
            self.lcdNumber_2.display(1)
            self.sumA += 64
        else:
            self.lcdNumber_2.display(0)
            self.sumA -= 64
        self.updateSumALabel()

    def lcdThreeA(self):
        if self.checkBox_3.isChecked():
            self.lcdNumber_3.display(1)
            self.sumA += 32
        else:
            self.lcdNumber_3.display(0)
            self.sumA -= 32
        self.updateSumALabel()
    
    def lcdFourA(self):
        if self.checkBox_4.isChecked():
            self.lcdNumber_4.display(1)
            self.sumA += 16
        else:
            self.lcdNumber_4.display(0)
            self.sumA -= 16
        self.updateSumALabel()

    def lcdFiveA(self):
        if self.checkBox_5.isChecked():
            self.lcdNumber_5.display(1)
            self.sumA += 8
        else:
            self.lcdNumber_5.display(0)
            self.sumA -= 8
        self.updateSumALabel()

    def lcdSixA(self):
        if self.checkBox_6.isChecked():
            self.lcdNumber_6.display(1)
            self.sumA += 4
        else:
            self.lcdNumber_6.display(0)
            self.sumA -= 4
        self.updateSumALabel()

    def lcdSevenA(self):
        if self.checkBox_7.isChecked():
            self.lcdNumber_7.display(1)
            self.sumA += 2
        else:
            self.lcdNumber_7.display(0)
            self.sumA -= 2
        self.updateSumALabel()

    def lcdEightA(self):
        if self.checkBox_8.isChecked():
            self.lcdNumber_8.display(1)
            self.sumA += 1
        else:
            self.lcdNumber_8.display(0)
            self.sumA -= 1
        self.updateSumALabel()

    # INPUT B I/O

    def updateSumBLabel(self):
        self.label_13.setText(str(self.sumB))

    def lcdOneB(self):
        if self.checkBox_9.isChecked():
            self.lcdNumber_9.display(1)
            self.sumB += 128
        else:
            self.lcdNumber_9.display(0)
            self.sumB -= 128
        self.updateSumBLabel()

    def lcdTwoB(self):
        if self.checkBox_10.isChecked():
            self.lcdNumber_10.display(1)
            self.sumB += 64
        else:
            self.lcdNumber_10.display(0)
            self.sumB -= 64
        self.updateSumBLabel()

    def lcdThreeB(self):
        if self.checkBox_11.isChecked():
            self.lcdNumber_11.display(1)
            self.sumB += 32
        else:
            self.lcdNumber_11.display(0)
            self.sumB -= 32
        self.updateSumBLabel()
    
    def lcdFourB(self):
        if self.checkBox_12.isChecked():
            self.lcdNumber_12.display(1)
            self.sumB += 16
        else:
            self.lcdNumber_12.display(0)
            self.sumB -= 16
        self.updateSumBLabel()

    def lcdFiveB(self):
        if self.checkBox_13.isChecked():
            self.lcdNumber_13.display(1)
            self.sumB += 8
        else:
            self.lcdNumber_13.display(0)
            self.sumB -= 8
        self.updateSumBLabel()

    def lcdSixB(self):
        if self.checkBox_14.isChecked():
            self.lcdNumber_14.display(1)
            self.sumB += 4
        else:
            self.lcdNumber_14.display(0)
            self.sumB -= 4
        self.updateSumBLabel()

    def lcdSevenB(self):
        if self.checkBox_15.isChecked():
            self.lcdNumber_15.display(1)
            self.sumB += 2
        else:
            self.lcdNumber_15.display(0)
            self.sumB -= 2
        self.updateSumBLabel()

    def lcdEightB(self):
        if self.checkBox_16.isChecked():
            self.lcdNumber_16.display(1)
            self.sumB += 1
        else:
            self.lcdNumber_16.display(0)
            self.sumB -= 1
        self.updateSumBLabel()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "8-Bit Full Adder Simulator - Rafael Almazar"))
        self.label_3.setText(_translate("MainWindow", "8-Bit Full Adder"))
        self.label_4.setText(_translate("MainWindow", "A in"))
        self.label_5.setText(_translate("MainWindow", "B in"))
        self.label_6.setText(_translate("MainWindow", "Carry in"))
        self.label_7.setText(_translate("MainWindow", "Carry out"))
        self.label_8.setText(_translate("MainWindow", "Sum"))
        self.label_9.setText(_translate("MainWindow", "Input A Decimal Value:"))
        self.label_10.setText(_translate("MainWindow", "Input B Decimal Value:"))
        self.label_11.setText(_translate("MainWindow", "Total Sum Decimal Value:"))
        self.label_12.setText(_translate("MainWindow", "0"))
        self.label_13.setText(_translate("MainWindow", "0"))
        self.label_14.setText(_translate("MainWindow", "0"))
        self.label_15.setText(_translate("MainWindow", "Sum Decimal Value:"))
        self.label_16.setText(_translate("MainWindow", "0"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())