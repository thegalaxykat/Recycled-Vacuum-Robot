# This Python file uses the following encoding: utf-8
# if __name__ == "__main__":
#     pass
import socket


def SendData(direction, time):
    # connect to server
    serversocket = socket.socket()
    serversocket.connect(('172.16.177.148', 1776))
    print("connected to server")

    # send commands
    commands = (direction + ', ' + time)
    data = commands.encode("utf-8")
    serversocket.send(data)
    serversocket.close


def forwardButton():
    print ("forward button pressed")
    SendData('forward', 10)


def leftButton():
    print ("left button pressed")
    SendData('left', .5)


def rightButton():
    print ("right button pressed")
    SendData('right', .5)


def backButton():
    print ("back button pressed")
    SendData('backward', 5)


def stopButton():
    print ("stop button pressed")
    SendData(stop)