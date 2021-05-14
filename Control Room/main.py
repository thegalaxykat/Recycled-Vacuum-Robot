
# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
from PySide2 import QtGui
from PySide2 import QtCore
from PySide2.QtCore import QObject, SIGNAL
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine, QtQml
import DriveFunctions


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.load(os.fspath(Path(__file__).resolve().parent / "main.qml"))  
    
    screen = engine.rootObjects()[0] # define everything on the screen after this
    
    # defining buttons
    forward_button = screen.findChild(QtCore.QObject, "forward_button") # define button
    QObject.connect(forward_button, SIGNAL ('clicked()'), DriveFunctions.forwardButton) # connect button to signal

    left_button = screen.findChild(QtCore.QObject, "left_button")
    QObject.connect(left_button, SIGNAL ('clicked()'), DriveFunctions.leftButton)

    right_button = screen.findChild(QtCore.QObject, "right_button")
    QObject.connect(right_button, SIGNAL ('clicked()'), DriveFunctions.rightButton)

    back_button = screen.findChild(QtCore.QObject, "back_button")
    QObject.connect(back_button, SIGNAL ('clicked()'), DriveFunctions.backButton)

    stop_button = screen.findChild(QtCore.QObject, "stop_button")
    QObject.connect(stop_button, SIGNAL ('clicked()'), DriveFunctions.stopButton)


    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())