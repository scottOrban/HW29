from PyQt5 import QtCore, QtGui, QtWidgets
'''user code'''
import RPi.GPIO as GPIO
from gpiozero import LED

GPIO.setmode(GPIO.BCM)
led=LED(23)

led_pin=24
GPIO.setup(led_pin,GPIO.OUT)

def ledToggle():
    if led.is_lit:
        led.off()
    else:
        led.on()    
    
'''user code'''

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(514, 363)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 120, 211, 101))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Message Box"))
        self.pushButton.setText(_translate("MainWindow", "Click me"))
        '''user code'''
        self.pushButton.clicked.connect(ledToggle)
        
import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow=QtWidgets.QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
'''user code'''