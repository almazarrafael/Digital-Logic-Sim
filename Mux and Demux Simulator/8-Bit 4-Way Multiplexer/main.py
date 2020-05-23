from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from PyQt5.QtCore import *
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    sumA = 0
    sumB = 0
    sumC = 0
    sumD = 0
    output = 0
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1226, 789)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.A8 = QtWidgets.QLCDNumber(self.centralwidget)
        self.A8.setGeometry(QtCore.QRect(437, 15, 60, 101))
        self.A8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.A8.setDigitCount(1)
        self.A8.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.A8.setObjectName("A8")
        self.AIn6 = QtWidgets.QCheckBox(self.centralwidget)
        self.AIn6.setGeometry(QtCore.QRect(340, 120, 16, 17))
        self.AIn6.setText("")
        self.AIn6.setObjectName("AIn6")
        self.A1 = QtWidgets.QLCDNumber(self.centralwidget)
        self.A1.setGeometry(QtCore.QRect(17, 15, 60, 101))
        self.A1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.A1.setDigitCount(1)
        self.A1.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.A1.setObjectName("A1")
        self.A2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.A2.setGeometry(QtCore.QRect(77, 15, 60, 101))
        self.A2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.A2.setDigitCount(1)
        self.A2.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.A2.setObjectName("A2")
        self.AIn1 = QtWidgets.QCheckBox(self.centralwidget)
        self.AIn1.setGeometry(QtCore.QRect(40, 120, 16, 17))
        self.AIn1.setText("")
        self.AIn1.setObjectName("AIn1")
        self.A7 = QtWidgets.QLCDNumber(self.centralwidget)
        self.A7.setGeometry(QtCore.QRect(377, 15, 60, 101))
        self.A7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.A7.setDigitCount(1)
        self.A7.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.A7.setObjectName("A7")
        self.AIn4 = QtWidgets.QCheckBox(self.centralwidget)
        self.AIn4.setGeometry(QtCore.QRect(220, 120, 16, 17))
        self.AIn4.setText("")
        self.AIn4.setObjectName("AIn4")
        self.A6 = QtWidgets.QLCDNumber(self.centralwidget)
        self.A6.setGeometry(QtCore.QRect(317, 15, 60, 101))
        self.A6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.A6.setDigitCount(1)
        self.A6.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.A6.setObjectName("A6")
        self.AIn3 = QtWidgets.QCheckBox(self.centralwidget)
        self.AIn3.setGeometry(QtCore.QRect(160, 120, 16, 17))
        self.AIn3.setText("")
        self.AIn3.setObjectName("AIn3")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(17, 15, 481, 131))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: lightblue")
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(2)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")
        self.AIn2 = QtWidgets.QCheckBox(self.centralwidget)
        self.AIn2.setGeometry(QtCore.QRect(100, 120, 16, 17))
        self.AIn2.setText("")
        self.AIn2.setObjectName("AIn2")
        self.AIn7 = QtWidgets.QCheckBox(self.centralwidget)
        self.AIn7.setGeometry(QtCore.QRect(400, 120, 16, 17))
        self.AIn7.setText("")
        self.AIn7.setObjectName("AIn7")
        self.AIn8 = QtWidgets.QCheckBox(self.centralwidget)
        self.AIn8.setGeometry(QtCore.QRect(460, 120, 16, 17))
        self.AIn8.setText("")
        self.AIn8.setObjectName("AIn8")
        self.A5 = QtWidgets.QLCDNumber(self.centralwidget)
        self.A5.setGeometry(QtCore.QRect(257, 15, 60, 101))
        self.A5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.A5.setDigitCount(1)
        self.A5.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.A5.setObjectName("A5")
        self.AIn5 = QtWidgets.QCheckBox(self.centralwidget)
        self.AIn5.setGeometry(QtCore.QRect(280, 120, 16, 17))
        self.AIn5.setText("")
        self.AIn5.setObjectName("AIn5")
        self.A4 = QtWidgets.QLCDNumber(self.centralwidget)
        self.A4.setGeometry(QtCore.QRect(197, 15, 60, 101))
        self.A4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.A4.setDigitCount(1)
        self.A4.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.A4.setObjectName("A4")
        self.A3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.A3.setGeometry(QtCore.QRect(137, 15, 60, 101))
        self.A3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.A3.setDigitCount(1)
        self.A3.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.A3.setObjectName("A3")
        self.B3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.B3.setGeometry(QtCore.QRect(137, 175, 60, 101))
        self.B3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.B3.setDigitCount(1)
        self.B3.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.B3.setObjectName("B3")
        self.BIn6 = QtWidgets.QCheckBox(self.centralwidget)
        self.BIn6.setGeometry(QtCore.QRect(340, 280, 16, 17))
        self.BIn6.setText("")
        self.BIn6.setObjectName("BIn6")
        self.BIn1 = QtWidgets.QCheckBox(self.centralwidget)
        self.BIn1.setGeometry(QtCore.QRect(40, 280, 16, 17))
        self.BIn1.setText("")
        self.BIn1.setObjectName("BIn1")
        self.BIn2 = QtWidgets.QCheckBox(self.centralwidget)
        self.BIn2.setGeometry(QtCore.QRect(100, 280, 16, 17))
        self.BIn2.setText("")
        self.BIn2.setObjectName("BIn2")
        self.BIn5 = QtWidgets.QCheckBox(self.centralwidget)
        self.BIn5.setGeometry(QtCore.QRect(280, 280, 16, 17))
        self.BIn5.setText("")
        self.BIn5.setObjectName("BIn5")
        self.B1 = QtWidgets.QLCDNumber(self.centralwidget)
        self.B1.setGeometry(QtCore.QRect(17, 175, 60, 101))
        self.B1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.B1.setDigitCount(1)
        self.B1.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.B1.setObjectName("B1")
        self.B7 = QtWidgets.QLCDNumber(self.centralwidget)
        self.B7.setGeometry(QtCore.QRect(377, 175, 60, 101))
        self.B7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.B7.setDigitCount(1)
        self.B7.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.B7.setObjectName("B7")
        self.B6 = QtWidgets.QLCDNumber(self.centralwidget)
        self.B6.setGeometry(QtCore.QRect(317, 175, 60, 101))
        self.B6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.B6.setDigitCount(1)
        self.B6.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.B6.setObjectName("B6")
        self.BIn7 = QtWidgets.QCheckBox(self.centralwidget)
        self.BIn7.setGeometry(QtCore.QRect(400, 280, 16, 17))
        self.BIn7.setText("")
        self.BIn7.setObjectName("BIn7")
        self.BIn8 = QtWidgets.QCheckBox(self.centralwidget)
        self.BIn8.setGeometry(QtCore.QRect(460, 280, 16, 17))
        self.BIn8.setText("")
        self.BIn8.setObjectName("BIn8")
        self.B8 = QtWidgets.QLCDNumber(self.centralwidget)
        self.B8.setGeometry(QtCore.QRect(437, 175, 60, 101))
        self.B8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.B8.setDigitCount(1)
        self.B8.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.B8.setObjectName("B8")
        self.BIn4 = QtWidgets.QCheckBox(self.centralwidget)
        self.BIn4.setGeometry(QtCore.QRect(220, 280, 16, 17))
        self.BIn4.setText("")
        self.BIn4.setObjectName("BIn4")
        self.B4 = QtWidgets.QLCDNumber(self.centralwidget)
        self.B4.setGeometry(QtCore.QRect(197, 175, 60, 101))
        self.B4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.B4.setDigitCount(1)
        self.B4.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.B4.setObjectName("B4")
        self.B2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.B2.setGeometry(QtCore.QRect(77, 175, 60, 101))
        self.B2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.B2.setDigitCount(1)
        self.B2.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.B2.setObjectName("B2")
        self.BIn3 = QtWidgets.QCheckBox(self.centralwidget)
        self.BIn3.setGeometry(QtCore.QRect(160, 280, 16, 17))
        self.BIn3.setText("")
        self.BIn3.setObjectName("BIn3")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(17, 175, 481, 131))
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setStyleSheet("background-color: lightblue")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(2)
        self.frame_2.setMidLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.B5 = QtWidgets.QLCDNumber(self.centralwidget)
        self.B5.setGeometry(QtCore.QRect(257, 175, 60, 101))
        self.B5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.B5.setDigitCount(1)
        self.B5.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.B5.setObjectName("B5")
        self.DIn1 = QtWidgets.QCheckBox(self.centralwidget)
        self.DIn1.setGeometry(QtCore.QRect(40, 600, 16, 17))
        self.DIn1.setText("")
        self.DIn1.setObjectName("DIn1")
        self.CIn2 = QtWidgets.QCheckBox(self.centralwidget)
        self.CIn2.setGeometry(QtCore.QRect(100, 440, 16, 17))
        self.CIn2.setText("")
        self.CIn2.setObjectName("CIn2")
        self.CIn4 = QtWidgets.QCheckBox(self.centralwidget)
        self.CIn4.setGeometry(QtCore.QRect(220, 440, 16, 17))
        self.CIn4.setText("")
        self.CIn4.setObjectName("CIn4")
        self.DIn2 = QtWidgets.QCheckBox(self.centralwidget)
        self.DIn2.setGeometry(QtCore.QRect(100, 600, 16, 17))
        self.DIn2.setText("")
        self.DIn2.setObjectName("DIn2")
        self.CIn8 = QtWidgets.QCheckBox(self.centralwidget)
        self.CIn8.setGeometry(QtCore.QRect(460, 440, 16, 17))
        self.CIn8.setText("")
        self.CIn8.setObjectName("CIn8")
        self.C8 = QtWidgets.QLCDNumber(self.centralwidget)
        self.C8.setGeometry(QtCore.QRect(437, 335, 60, 101))
        self.C8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.C8.setDigitCount(1)
        self.C8.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.C8.setObjectName("C8")
        self.CIn1 = QtWidgets.QCheckBox(self.centralwidget)
        self.CIn1.setGeometry(QtCore.QRect(40, 440, 16, 17))
        self.CIn1.setText("")
        self.CIn1.setObjectName("CIn1")
        self.C6 = QtWidgets.QLCDNumber(self.centralwidget)
        self.C6.setGeometry(QtCore.QRect(317, 335, 60, 101))
        self.C6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.C6.setDigitCount(1)
        self.C6.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.C6.setObjectName("C6")
        self.C3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.C3.setGeometry(QtCore.QRect(137, 335, 60, 101))
        self.C3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.C3.setDigitCount(1)
        self.C3.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.C3.setObjectName("C3")
        self.CIn3 = QtWidgets.QCheckBox(self.centralwidget)
        self.CIn3.setGeometry(QtCore.QRect(160, 440, 16, 17))
        self.CIn3.setText("")
        self.CIn3.setObjectName("CIn3")
        self.C1 = QtWidgets.QLCDNumber(self.centralwidget)
        self.C1.setGeometry(QtCore.QRect(17, 335, 60, 101))
        self.C1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.C1.setDigitCount(1)
        self.C1.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.C1.setObjectName("C1")
        self.DIn6 = QtWidgets.QCheckBox(self.centralwidget)
        self.DIn6.setGeometry(QtCore.QRect(340, 600, 16, 17))
        self.DIn6.setText("")
        self.DIn6.setObjectName("DIn6")
        self.DIn3 = QtWidgets.QCheckBox(self.centralwidget)
        self.DIn3.setGeometry(QtCore.QRect(160, 600, 16, 17))
        self.DIn3.setText("")
        self.DIn3.setObjectName("DIn3")
        self.DIn5 = QtWidgets.QCheckBox(self.centralwidget)
        self.DIn5.setGeometry(QtCore.QRect(280, 600, 16, 17))
        self.DIn5.setText("")
        self.DIn5.setObjectName("DIn5")
        self.D2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.D2.setGeometry(QtCore.QRect(77, 495, 60, 101))
        self.D2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.D2.setDigitCount(1)
        self.D2.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.D2.setObjectName("D2")
        self.D7 = QtWidgets.QLCDNumber(self.centralwidget)
        self.D7.setGeometry(QtCore.QRect(377, 495, 60, 101))
        self.D7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.D7.setDigitCount(1)
        self.D7.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.D7.setObjectName("D7")
        self.C5 = QtWidgets.QLCDNumber(self.centralwidget)
        self.C5.setGeometry(QtCore.QRect(257, 335, 60, 101))
        self.C5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.C5.setDigitCount(1)
        self.C5.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.C5.setObjectName("C5")
        self.D8 = QtWidgets.QLCDNumber(self.centralwidget)
        self.D8.setGeometry(QtCore.QRect(437, 495, 60, 101))
        self.D8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.D8.setDigitCount(1)
        self.D8.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.D8.setObjectName("D8")
        self.D6 = QtWidgets.QLCDNumber(self.centralwidget)
        self.D6.setGeometry(QtCore.QRect(317, 495, 60, 101))
        self.D6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.D6.setDigitCount(1)
        self.D6.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.D6.setObjectName("D6")
        self.CIn7 = QtWidgets.QCheckBox(self.centralwidget)
        self.CIn7.setGeometry(QtCore.QRect(400, 440, 16, 17))
        self.CIn7.setText("")
        self.CIn7.setObjectName("CIn7")
        self.CIn5 = QtWidgets.QCheckBox(self.centralwidget)
        self.CIn5.setGeometry(QtCore.QRect(280, 440, 16, 17))
        self.CIn5.setText("")
        self.CIn5.setObjectName("CIn5")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(17, 495, 481, 131))
        self.frame_3.setAutoFillBackground(False)
        self.frame_3.setStyleSheet("background-color: lightblue")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setLineWidth(2)
        self.frame_3.setMidLineWidth(0)
        self.frame_3.setObjectName("frame_3")
        self.D5 = QtWidgets.QLCDNumber(self.centralwidget)
        self.D5.setGeometry(QtCore.QRect(257, 495, 60, 101))
        self.D5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.D5.setDigitCount(1)
        self.D5.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.D5.setObjectName("D5")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(17, 335, 481, 131))
        self.frame_4.setAutoFillBackground(False)
        self.frame_4.setStyleSheet("background-color: lightblue")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setLineWidth(2)
        self.frame_4.setMidLineWidth(0)
        self.frame_4.setObjectName("frame_4")
        self.D4 = QtWidgets.QLCDNumber(self.centralwidget)
        self.D4.setGeometry(QtCore.QRect(197, 495, 60, 101))
        self.D4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.D4.setDigitCount(1)
        self.D4.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.D4.setObjectName("D4")
        self.D1 = QtWidgets.QLCDNumber(self.centralwidget)
        self.D1.setGeometry(QtCore.QRect(17, 495, 60, 101))
        self.D1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.D1.setDigitCount(1)
        self.D1.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.D1.setObjectName("D1")
        self.CIn6 = QtWidgets.QCheckBox(self.centralwidget)
        self.CIn6.setGeometry(QtCore.QRect(340, 440, 16, 17))
        self.CIn6.setText("")
        self.CIn6.setObjectName("CIn6")
        self.C2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.C2.setGeometry(QtCore.QRect(77, 335, 60, 101))
        self.C2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.C2.setDigitCount(1)
        self.C2.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.C2.setObjectName("C2")
        self.D3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.D3.setGeometry(QtCore.QRect(137, 495, 60, 101))
        self.D3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.D3.setDigitCount(1)
        self.D3.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.D3.setObjectName("D3")
        self.DIn7 = QtWidgets.QCheckBox(self.centralwidget)
        self.DIn7.setGeometry(QtCore.QRect(400, 600, 16, 17))
        self.DIn7.setText("")
        self.DIn7.setObjectName("DIn7")
        self.C7 = QtWidgets.QLCDNumber(self.centralwidget)
        self.C7.setGeometry(QtCore.QRect(377, 335, 60, 101))
        self.C7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.C7.setDigitCount(1)
        self.C7.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.C7.setObjectName("C7")
        self.C4 = QtWidgets.QLCDNumber(self.centralwidget)
        self.C4.setGeometry(QtCore.QRect(197, 335, 60, 101))
        self.C4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.C4.setDigitCount(1)
        self.C4.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.C4.setObjectName("C4")
        self.DIn4 = QtWidgets.QCheckBox(self.centralwidget)
        self.DIn4.setGeometry(QtCore.QRect(220, 600, 16, 17))
        self.DIn4.setText("")
        self.DIn4.setObjectName("DIn4")
        self.DIn8 = QtWidgets.QCheckBox(self.centralwidget)
        self.DIn8.setGeometry(QtCore.QRect(460, 600, 16, 17))
        self.DIn8.setText("")
        self.DIn8.setObjectName("DIn8")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(550, 40, 200, 561))
        self.frame_5.setAutoFillBackground(False)
        self.frame_5.setStyleSheet("background-color: lightblue")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_5.setLineWidth(2)
        self.frame_5.setObjectName("frame_5")
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        self.label_4.setGeometry(QtCore.QRect(40, 540, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        self.label_5.setGeometry(QtCore.QRect(150, 540, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_5)
        self.label_6.setGeometry(QtCore.QRect(10, 20, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_5)
        self.label_7.setGeometry(QtCore.QRect(10, 180, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_5)
        self.label_8.setGeometry(QtCore.QRect(10, 340, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_19 = QtWidgets.QLabel(self.frame_5)
        self.label_19.setGeometry(QtCore.QRect(10, 500, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        self.label_3.setGeometry(QtCore.QRect(30, 220, 131, 111))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(800, 263, 411, 111))
        self.frame_6.setAutoFillBackground(False)
        self.frame_6.setStyleSheet("background-color: lightblue")
        self.frame_6.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_6.setLineWidth(2)
        self.frame_6.setMidLineWidth(0)
        self.frame_6.setObjectName("frame_6")
        self.output = QtWidgets.QLCDNumber(self.frame_6)
        self.output.setGeometry(QtCore.QRect(2, 2, 401, 101))
        self.output.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.output.setFrameShadow(QtWidgets.QFrame.Plain)
        self.output.setDigitCount(8)
        self.output.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.output.setProperty("value", 99999999.0)
        self.output.setObjectName("output")
        self.frame_7 = QtWidgets.QFrame(self.centralwidget)
        self.frame_7.setGeometry(QtCore.QRect(670, 630, 72, 135))
        self.frame_7.setAutoFillBackground(False)
        self.frame_7.setStyleSheet("background-color: lightblue")
        self.frame_7.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_7.setLineWidth(2)
        self.frame_7.setObjectName("frame_7")
        self.S0 = QtWidgets.QLCDNumber(self.frame_7)
        self.S0.setGeometry(QtCore.QRect(7, 5, 60, 101))
        self.S0.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.S0.setDigitCount(1)
        self.S0.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.S0.setObjectName("S0")
        self.S0In = QtWidgets.QCheckBox(self.frame_7)
        self.S0In.setGeometry(QtCore.QRect(30, 110, 16, 17))
        self.S0In.setText("")
        self.S0In.setObjectName("S0In")
        self.frame_8 = QtWidgets.QFrame(self.centralwidget)
        self.frame_8.setGeometry(QtCore.QRect(560, 630, 72, 135))
        self.frame_8.setAutoFillBackground(False)
        self.frame_8.setStyleSheet("background-color: lightblue")
        self.frame_8.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_8.setLineWidth(2)
        self.frame_8.setObjectName("frame_8")
        self.S1 = QtWidgets.QLCDNumber(self.frame_8)
        self.S1.setGeometry(QtCore.QRect(7, 5, 60, 101))
        self.S1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.S1.setDigitCount(1)
        self.S1.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.S1.setObjectName("S1")
        self.S1In = QtWidgets.QCheckBox(self.frame_8)
        self.S1In.setGeometry(QtCore.QRect(30, 110, 16, 17))
        self.S1In.setText("")
        self.S1In.setObjectName("S1In")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(1060, 560, 121, 16))
        self.label_10.setObjectName("label_10")
        self.InADec = QtWidgets.QLabel(self.centralwidget)
        self.InADec.setGeometry(QtCore.QRect(1060, 530, 121, 16))
        self.InADec.setObjectName("InADec")
        self.frame_9 = QtWidgets.QFrame(self.centralwidget)
        self.frame_9.setGeometry(QtCore.QRect(1050, 505, 151, 261))
        self.frame_9.setAutoFillBackground(True)
        self.frame_9.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_9.setLineWidth(1)
        self.frame_9.setObjectName("frame_9")
        self.OutputDec = QtWidgets.QLabel(self.frame_9)
        self.OutputDec.setGeometry(QtCore.QRect(10, 230, 121, 16))
        self.OutputDec.setObjectName("OutputDec")
        self.label_17 = QtWidgets.QLabel(self.frame_9)
        self.label_17.setGeometry(QtCore.QRect(10, 210, 121, 16))
        self.label_17.setObjectName("label_17")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1060, 510, 121, 16))
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(1060, 660, 121, 16))
        self.label_11.setObjectName("label_11")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(1060, 610, 121, 16))
        self.label_15.setObjectName("label_15")
        self.InBDec = QtWidgets.QLabel(self.centralwidget)
        self.InBDec.setGeometry(QtCore.QRect(1060, 580, 121, 16))
        self.InBDec.setObjectName("InBDec")
        self.InDDec = QtWidgets.QLabel(self.centralwidget)
        self.InDDec.setGeometry(QtCore.QRect(1060, 680, 121, 16))
        self.InDDec.setObjectName("InDDec")
        self.InCDec = QtWidgets.QLabel(self.centralwidget)
        self.InCDec.setGeometry(QtCore.QRect(1060, 630, 121, 16))
        self.InCDec.setObjectName("InCDec")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(585, 600, 20, 30))
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(700, 600, 20, 30))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(750, 320, 50, 3))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(496, 385, 55, 3))
        self.line_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_4.setLineWidth(2)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(496, 225, 55, 3))
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setLineWidth(2)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(496, 65, 55, 3))
        self.line_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_6.setLineWidth(2)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(496, 545, 55, 3))
        self.line_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_7.setLineWidth(2)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setObjectName("line_7")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(730, 310, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.frame_9.raise_()
        self.frame_3.raise_()
        self.frame_4.raise_()
        self.frame.raise_()
        self.frame_2.raise_()
        self.A8.raise_()
        self.AIn6.raise_()
        self.A1.raise_()
        self.A2.raise_()
        self.AIn1.raise_()
        self.A7.raise_()
        self.AIn4.raise_()
        self.A6.raise_()
        self.AIn3.raise_()
        self.AIn2.raise_()
        self.AIn7.raise_()
        self.AIn8.raise_()
        self.A5.raise_()
        self.AIn5.raise_()
        self.A4.raise_()
        self.A3.raise_()
        self.B3.raise_()
        self.BIn6.raise_()
        self.BIn1.raise_()
        self.BIn2.raise_()
        self.BIn5.raise_()
        self.B1.raise_()
        self.B7.raise_()
        self.B6.raise_()
        self.BIn7.raise_()
        self.BIn8.raise_()
        self.B8.raise_()
        self.BIn4.raise_()
        self.B4.raise_()
        self.B2.raise_()
        self.BIn3.raise_()
        self.B5.raise_()
        self.DIn1.raise_()
        self.CIn2.raise_()
        self.CIn4.raise_()
        self.DIn2.raise_()
        self.CIn8.raise_()
        self.C8.raise_()
        self.CIn1.raise_()
        self.C6.raise_()
        self.C3.raise_()
        self.CIn3.raise_()
        self.C1.raise_()
        self.DIn6.raise_()
        self.DIn3.raise_()
        self.DIn5.raise_()
        self.D2.raise_()
        self.D7.raise_()
        self.C5.raise_()
        self.D8.raise_()
        self.D6.raise_()
        self.CIn7.raise_()
        self.CIn5.raise_()
        self.D5.raise_()
        self.D4.raise_()
        self.D1.raise_()
        self.CIn6.raise_()
        self.C2.raise_()
        self.D3.raise_()
        self.DIn7.raise_()
        self.C7.raise_()
        self.C4.raise_()
        self.DIn4.raise_()
        self.DIn8.raise_()
        self.frame_5.raise_()
        self.frame_6.raise_()
        self.frame_7.raise_()
        self.frame_8.raise_()
        self.label_10.raise_()
        self.InADec.raise_()
        self.label_9.raise_()
        self.label_11.raise_()
        self.label_15.raise_()
        self.InBDec.raise_()
        self.InDDec.raise_()
        self.InCDec.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        self.line_5.raise_()
        self.line_6.raise_()
        self.line_7.raise_()
        self.label_20.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1226, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.output.display("00000000")

        # 00 - A, 01 - B, 10 - C, 11 - D

        self.timer = QTimer()
        self.timer.timeout.connect(self.muxLogic)
        self.timer.start(1)

        # INPUT A SIGNALS
        self.AIn1.stateChanged.connect(self.AUpdate1)
        self.AIn2.stateChanged.connect(self.AUpdate2)
        self.AIn3.stateChanged.connect(self.AUpdate3)
        self.AIn4.stateChanged.connect(self.AUpdate4)
        self.AIn5.stateChanged.connect(self.AUpdate5)
        self.AIn6.stateChanged.connect(self.AUpdate6)
        self.AIn7.stateChanged.connect(self.AUpdate7)
        self.AIn8.stateChanged.connect(self.AUpdate8)

        # INPUT B SIGNALS
        self.BIn1.stateChanged.connect(self.BUpdate1)
        self.BIn2.stateChanged.connect(self.BUpdate2)
        self.BIn3.stateChanged.connect(self.BUpdate3)
        self.BIn4.stateChanged.connect(self.BUpdate4)
        self.BIn5.stateChanged.connect(self.BUpdate5)
        self.BIn6.stateChanged.connect(self.BUpdate6)
        self.BIn7.stateChanged.connect(self.BUpdate7)
        self.BIn8.stateChanged.connect(self.BUpdate8)

        # INPUT C SIGNALS
        self.CIn1.stateChanged.connect(self.CUpdate1)
        self.CIn2.stateChanged.connect(self.CUpdate2)
        self.CIn3.stateChanged.connect(self.CUpdate3)
        self.CIn4.stateChanged.connect(self.CUpdate4)
        self.CIn5.stateChanged.connect(self.CUpdate5)
        self.CIn6.stateChanged.connect(self.CUpdate6)
        self.CIn7.stateChanged.connect(self.CUpdate7)
        self.CIn8.stateChanged.connect(self.CUpdate8)

        # INPUT D SIGNALS
        self.DIn1.stateChanged.connect(self.DUpdate1)
        self.DIn2.stateChanged.connect(self.DUpdate2)
        self.DIn3.stateChanged.connect(self.DUpdate3)
        self.DIn4.stateChanged.connect(self.DUpdate4)
        self.DIn5.stateChanged.connect(self.DUpdate5)
        self.DIn6.stateChanged.connect(self.DUpdate6)
        self.DIn7.stateChanged.connect(self.DUpdate7)
        self.DIn8.stateChanged.connect(self.DUpdate8)

        # SELECT SIGNALS
        self.S0In.stateChanged.connect(self.S0Update)
        self.S1In.stateChanged.connect(self.S1Update)

    def muxLogic(self):
        if self.S1.value() == 0:
            if self.S0.value() == 0:
                self.output.display(format(self.sumA, "08b"))
                self.OutputDec.setText(str(self.sumA))
            elif self.S0.value() == 1:
                self.output.display(format(self.sumB, "08b"))
                self.OutputDec.setText(str(self.sumB))
        elif self.S1.value() == 1:
            if self.S0.value() == 0:
                self.output.display(format(self.sumC, "08b"))
                self.OutputDec.setText(str(self.sumC))
            elif self.S0.value() == 1:
                self.output.display(format(self.sumD, "08b"))
                self.OutputDec.setText(str(self.sumD))

    # Select I/O
    def S0Update(self):
        if self.S0In.isChecked():
            self.S0.display(1)
        else:
            self.S0.display(0)
        
    def S1Update(self):
        if self.S1In.isChecked():
            self.S1.display(1)
        else:
            self.S1.display(0)

    # Input A I/O
    def updateSumALabel(self):
        self.InADec.setText(str(self.sumA))

    def AUpdate1(self):
        if self.AIn1.isChecked():
            self.A1.display(1)
            self.sumA += 128
        else:
            self.A1.display(0)
            self.sumA -= 128
        self.updateSumALabel()

    def AUpdate2(self):
        if self.AIn2.isChecked():
            self.A2.display(1)
            self.sumA += 64
        else:
            self.A2.display(0)
            self.sumA -= 64
        self.updateSumALabel()

    def AUpdate3(self):
        if self.AIn3.isChecked():
            self.A3.display(1)
            self.sumA += 32
        else:
            self.A3.display(0)
            self.sumA -= 32
        self.updateSumALabel()

    def AUpdate4(self):
        if self.AIn4.isChecked():
            self.A4.display(1)
            self.sumA += 16
        else:
            self.A4.display(0)
            self.sumA -= 16
        self.updateSumALabel()

    def AUpdate5(self):
        if self.AIn5.isChecked():
            self.A5.display(1)
            self.sumA += 8
        else:
            self.A5.display(0)
            self.sumA -= 8
        self.updateSumALabel()

    def AUpdate6(self):
        if self.AIn6.isChecked():
            self.A6.display(1)
            self.sumA += 4
        else:
            self.A6.display(0)
            self.sumA -= 4
        self.updateSumALabel()

    def AUpdate7(self):
        if self.AIn7.isChecked():
            self.A7.display(1)
            self.sumA += 2
        else:
            self.A7.display(0)
            self.sumA -= 2
        self.updateSumALabel()

    def AUpdate8(self):
        if self.AIn8.isChecked():
            self.A8.display(1)
            self.sumA += 1
        else:
            self.A8.display(0)
            self.sumA -= 1
        self.updateSumALabel()

    # Input B I/O
    def updateSumBLabel(self):
        self.InBDec.setText(str(self.sumB))

    def BUpdate1(self):
        if self.BIn1.isChecked():
            self.B1.display(1)
            self.sumB += 128
        else:
            self.B1.display(0)
            self.sumB -= 128
        self.updateSumBLabel()

    def BUpdate2(self):
        if self.BIn2.isChecked():
            self.B2.display(1)
            self.sumB += 64
        else:
            self.B2.display(0)
            self.sumB -= 64
        self.updateSumBLabel()

    def BUpdate3(self):
        if self.BIn3.isChecked():
            self.B3.display(1)
            self.sumB += 32
        else:
            self.B3.display(0)
            self.sumB -= 32
        self.updateSumBLabel()

    def BUpdate4(self):
        if self.BIn4.isChecked():
            self.B4.display(1)
            self.sumB += 16
        else:
            self.B4.display(0)
            self.sumB -= 16
        self.updateSumBLabel()

    def BUpdate5(self):
        if self.BIn5.isChecked():
            self.B5.display(1)
            self.sumB += 8
        else:
            self.B5.display(0)
            self.sumB -= 8
        self.updateSumBLabel()

    def BUpdate6(self):
        if self.BIn6.isChecked():
            self.B6.display(1)
            self.sumB += 4
        else:
            self.B6.display(0)
            self.sumB -= 4
        self.updateSumBLabel()

    def BUpdate7(self):
        if self.BIn7.isChecked():
            self.B7.display(1)
            self.sumB += 2
        else:
            self.B7.display(0)
            self.sumB -= 2
        self.updateSumBLabel()

    def BUpdate8(self):
        if self.BIn8.isChecked():
            self.B8.display(1)
            self.sumB += 1
        else:
            self.B8.display(0)
            self.sumB -= 1
        self.updateSumBLabel()

    # Input C I/O
    def updateSumCLabel(self):
        self.InCDec.setText(str(self.sumC))

    def CUpdate1(self):
        if self.CIn1.isChecked():
            self.C1.display(1)
            self.sumC += 128
        else:
            self.C1.display(0)
            self.sumC -= 128
        self.updateSumCLabel()

    def CUpdate2(self):
        if self.CIn2.isChecked():
            self.C2.display(1)
            self.sumC += 64
        else:
            self.C2.display(0)
            self.sumC -= 64
        self.updateSumCLabel()

    def CUpdate3(self):
        if self.CIn3.isChecked():
            self.C3.display(1)
            self.sumC += 32
        else:
            self.C3.display(0)
            self.sumC -= 32
        self.updateSumCLabel()

    def CUpdate4(self):
        if self.CIn4.isChecked():
            self.C4.display(1)
            self.sumC += 16
        else:
            self.C4.display(0)
            self.sumC -= 16
        self.updateSumCLabel()

    def CUpdate5(self):
        if self.CIn5.isChecked():
            self.C5.display(1)
            self.sumC += 8
        else:
            self.C5.display(0)
            self.sumC -= 8
        self.updateSumCLabel()

    def CUpdate6(self):
        if self.CIn6.isChecked():
            self.C6.display(1)
            self.sumC += 4
        else:
            self.C6.display(0)
            self.sumC -= 4
        self.updateSumCLabel()

    def CUpdate7(self):
        if self.CIn7.isChecked():
            self.C7.display(1)
            self.sumC += 2
        else:
            self.C7.display(0)
            self.sumC -= 2
        self.updateSumCLabel()

    def CUpdate8(self):
        if self.CIn8.isChecked():
            self.C8.display(1)
            self.sumC += 1
        else:
            self.C8.display(0)
            self.sumC -= 1
        self.updateSumCLabel()

    # Input D I/O
    def updateSumDLabel(self):
        self.InDDec.setText(str(self.sumD))

    def DUpdate1(self):
        if self.DIn1.isChecked():
            self.D1.display(1)
            self.sumD += 128
        else:
            self.D1.display(0)
            self.sumD -= 128
        self.updateSumDLabel()

    def DUpdate2(self):
        if self.DIn2.isChecked():
            self.D2.display(1)
            self.sumD += 64
        else:
            self.D2.display(0)
            self.sumD -= 64
        self.updateSumDLabel()

    def DUpdate3(self):
        if self.DIn3.isChecked():
            self.D3.display(1)
            self.sumD += 32
        else:
            self.D3.display(0)
            self.sumD -= 32
        self.updateSumDLabel()

    def DUpdate4(self):
        if self.DIn4.isChecked():
            self.D4.display(1)
            self.sumD += 16
        else:
            self.D4.display(0)
            self.sumD -= 16
        self.updateSumDLabel()

    def DUpdate5(self):
        if self.DIn5.isChecked():
            self.D5.display(1)
            self.sumD += 8
        else:
            self.D5.display(0)
            self.sumD -= 8
        self.updateSumDLabel()

    def DUpdate6(self):
        if self.DIn6.isChecked():
            self.D6.display(1)
            self.sumD += 4
        else:
            self.D6.display(0)
            self.sumD -= 4
        self.updateSumDLabel()

    def DUpdate7(self):
        if self.DIn7.isChecked():
            self.D7.display(1)
            self.sumD += 2
        else:
            self.D7.display(0)
            self.sumD -= 2
        self.updateSumDLabel()

    def DUpdate8(self):
        if self.DIn8.isChecked():
            self.D8.display(1)
            self.sumD += 1
        else:
            self.D8.display(0)
            self.sumD -= 1
        self.updateSumDLabel()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "8-Bit 4-Way Multiplexer - Rafael Almazar"))
        self.label_4.setText(_translate("MainWindow", "S1"))
        self.label_5.setText(_translate("MainWindow", "S0"))
        self.label_6.setText(_translate("MainWindow", "A in"))
        self.label_7.setText(_translate("MainWindow", "B in"))
        self.label_8.setText(_translate("MainWindow", "C in"))
        self.label_19.setText(_translate("MainWindow", "D in"))
        self.label_3.setText(_translate("MainWindow", "8-Bit         4-Way Multiplexer"))
        self.label_10.setText(_translate("MainWindow", "B in (01) Decimal Value:"))
        self.InADec.setText(_translate("MainWindow", "0"))
        self.OutputDec.setText(_translate("MainWindow", "0"))
        self.label_17.setText(_translate("MainWindow", "Output Decimal Value"))
        self.label_9.setText(_translate("MainWindow", "A in (00) Decimal Value:"))
        self.label_11.setText(_translate("MainWindow", "D in (11) Decimal Value"))
        self.label_15.setText(_translate("MainWindow", "C in (10) Decimal Value:"))
        self.InBDec.setText(_translate("MainWindow", "0"))
        self.InDDec.setText(_translate("MainWindow", "0"))
        self.InCDec.setText(_translate("MainWindow", "0"))
        self.label_20.setText(_translate("MainWindow", "Q"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())