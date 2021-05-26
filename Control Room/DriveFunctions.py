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
    commands = (direction + ', ' + str(time))
    data = commands.encode("utf-8")
    serversocket.send(data)
    serversocket.close


def forwardButton():
    print ("forward button pressed")
    SendData('forward', 2.5)


def leftButton():
    print ("left button pressed")
    SendData('left', .5)


def rightButton():
    print ("right button pressed")
    SendData('right', .5)


def backButton():
    print ("back button pressed")
    SendData('backward', 2)


def stopButton():
    print ("stop button pressed")
    SendData("stop")