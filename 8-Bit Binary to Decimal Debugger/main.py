from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from PyQt5.QtCore import *
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    total = 0

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(701, 263)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lcdNumber_1 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_1.setGeometry(QtCore.QRect(30, 30, 81, 141))
        self.lcdNumber_1.setAutoFillBackground(False)
        self.lcdNumber_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_1.setDigitCount(1)
        self.lcdNumber_1.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_1.setObjectName("lcdNumber_1")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(110, 30, 81, 141))
        self.lcdNumber_2.setAutoFillBackground(False)
        self.lcdNumber_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_2.setDigitCount(1)
        self.lcdNumber_2.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_3.setGeometry(QtCore.QRect(190, 30, 81, 141))
        self.lcdNumber_3.setAutoFillBackground(False)
        self.lcdNumber_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_3.setDigitCount(1)
        self.lcdNumber_3.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.lcdNumber_4 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_4.setGeometry(QtCore.QRect(270, 30, 81, 141))
        self.lcdNumber_4.setAutoFillBackground(False)
        self.lcdNumber_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_4.setDigitCount(1)
        self.lcdNumber_4.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_4.setObjectName("lcdNumber_4")
        self.lcdNumber_8 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_8.setGeometry(QtCore.QRect(590, 30, 81, 141))
        self.lcdNumber_8.setAutoFillBackground(False)
        self.lcdNumber_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_8.setDigitCount(1)
        self.lcdNumber_8.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_8.setObjectName("lcdNumber_8")
        self.lcdNumber_5 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_5.setGeometry(QtCore.QRect(350, 30, 81, 141))
        self.lcdNumber_5.setAutoFillBackground(False)
        self.lcdNumber_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_5.setDigitCount(1)
        self.lcdNumber_5.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_5.setObjectName("lcdNumber_5")
        self.lcdNumber_6 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_6.setGeometry(QtCore.QRect(430, 30, 81, 141))
        self.lcdNumber_6.setAutoFillBackground(False)
        self.lcdNumber_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_6.setDigitCount(1)
        self.lcdNumber_6.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_6.setObjectName("lcdNumber_6")
        self.lcdNumber_7 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_7.setGeometry(QtCore.QRect(510, 30, 81, 141))
        self.lcdNumber_7.setAutoFillBackground(False)
        self.lcdNumber_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_7.setDigitCount(1)
        self.lcdNumber_7.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_7.setObjectName("lcdNumber_7")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(65, 175, 16, 21))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(145, 175, 16, 21))
        self.checkBox_2.setText("")
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(225, 175, 16, 21))
        self.checkBox_3.setText("")
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(305, 175, 16, 21))
        self.checkBox_4.setText("")
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(380, 175, 16, 21))
        self.checkBox_5.setText("")
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_6.setGeometry(QtCore.QRect(460, 175, 16, 21))
        self.checkBox_6.setText("")
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_7.setGeometry(QtCore.QRect(540, 175, 16, 21))
        self.checkBox_7.setText("")
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_8.setGeometry(QtCore.QRect(620, 175, 16, 21))
        self.checkBox_8.setText("")
        self.checkBox_8.setObjectName("checkBox_8")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 200, 41, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 220, 47, 13))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 30, 661, 171))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color: lightblue")
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.frame.raise_()
        self.lcdNumber_1.raise_()
        self.lcdNumber_2.raise_()
        self.lcdNumber_3.raise_()
        self.lcdNumber_4.raise_()
        self.lcdNumber_8.raise_()
        self.lcdNumber_5.raise_()
        self.lcdNumber_6.raise_()
        self.lcdNumber_7.raise_()
        self.checkBox.raise_()
        self.checkBox_2.raise_()
        self.checkBox_3.raise_()
        self.checkBox_4.raise_()
        self.checkBox_5.raise_()
        self.checkBox_6.raise_()
        self.checkBox_7.raise_()
        self.checkBox_8.raise_()
        self.label.raise_()
        self.label_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 701, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.checkBox.stateChanged.connect(self.lcdOne)
        self.checkBox_2.stateChanged.connect(self.lcdTwo)
        self.checkBox_3.stateChanged.connect(self.lcdThree)
        self.checkBox_4.stateChanged.connect(self.lcdFour)
        self.checkBox_5.stateChanged.connect(self.lcdFive)
        self.checkBox_6.stateChanged.connect(self.lcdSix)
        self.checkBox_7.stateChanged.connect(self.lcdSeven)
        self.checkBox_8.stateChanged.connect(self.lcdEight)

    def updateLabel(self):
        self.label_2.setText(str(self.total))

    def lcdOne(self):
        if self.checkBox.isChecked():
            self.lcdNumber_1.display(1)
            self.total += 128
        else:
            self.lcdNumber_1.display(0)
            self.total -= 128
        self.updateLabel()

    def lcdTwo(self):
        if self.checkBox_2.isChecked():
            self.lcdNumber_2.display(1)
            self.total += 64
        else:
            self.lcdNumber_2.display(0)
            self.total -= 64
        self.updateLabel()

    def lcdThree(self):
        if self.checkBox_3.isChecked():
            self.lcdNumber_3.display(1)
            self.total += 32
        else:
            self.lcdNumber_3.display(0)
            self.total -= 32
        self.updateLabel()
    
    def lcdFour(self):
        if self.checkBox_4.isChecked():
            self.lcdNumber_4.display(1)
            self.total += 16
        else:
            self.lcdNumber_4.display(0)
            self.total -= 16
        self.updateLabel()

    def lcdFive(self):
        if self.checkBox_5.isChecked():
            self.lcdNumber_5.display(1)
            self.total += 8
        else:
            self.lcdNumber_5.display(0)
            self.total -= 8
        self.updateLabel()

    def lcdSix(self):
        if self.checkBox_6.isChecked():
            self.lcdNumber_6.display(1)
            self.total += 4
        else:
            self.lcdNumber_6.display(0)
            self.total -= 4
        self.updateLabel()

    def lcdSeven(self):
        if self.checkBox_7.isChecked():
            self.lcdNumber_7.display(1)
            self.total += 2
        else:
            self.lcdNumber_7.display(0)
            self.total -= 2
        self.updateLabel()

    def lcdEight(self):
        if self.checkBox_8.isChecked():
            self.lcdNumber_8.display(1)
            self.total += 1
        else:
            self.lcdNumber_8.display(0)
            self.total -= 1
        self.updateLabel()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Binary to Decimal Converter - Rafael Almazar"))
        self.label.setText(_translate("MainWindow", "Decimal:"))
        self.label_2.setText(_translate("MainWindow", "0"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())