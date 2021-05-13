import socket

serversocket = socket.socket()

serversocket.connect (('172.16.177.148', 1776)) #connect to server
print("connected")

#prompt user for direction and time 
direction = input("Robot Direction: ")
time = input("Drive Time in Seconds: ")
commands = (direction + ', ' + time)
data = commands.encode("utf-8")

serversocket.send(data)
serversocket.close