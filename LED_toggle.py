from PyQt5 import QtCore, QtGui, QtWidgets
'''usr code'''
import RPi.GPIO as GPIO
from gpiozero import LED

GPIO.setmode(GPIO.BCM)
led=LED(23)

led_pin=23
GPIO.setup(led_pin,GPIO.OUT)
pwm=GPIO.PWM(led_pin,100)
pwm.start(100)

def ledToggle():
    if led.is_lit:
        led.off()
    else:
        led.on()    
    
'''usr code'''

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(514, 363)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        
        '''usr code'''
        self.verticalSlider.setMinimum(0)
        self.verticalSlider.setMaximum(100)
        self.verticalSlider.setValue(100)
        '''usr code'''

        self.verticalSlider.setGeometry(QtCore.QRect(350, 90, 22, 160))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")

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
        '''usr code'''
        self.pushButton.clicked.connect(ledToggle)
        self.verticalSlider.valueChanged.connect(self.sliderMov)

    def sliderMov(self):
        value=self.verticalSlider.value()
        print(value)
        pwm.ChangeDutyCycle(value)
        '''usr code'''
        
'''usr code'''
import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow=QtWidgets.QMainWindow()
ui=Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
'''usr code'''
