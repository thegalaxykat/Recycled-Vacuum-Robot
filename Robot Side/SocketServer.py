import socket
import RobotControl as Robot

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host and port
serversocket.bind(('0.0.0.0', 1776)) # pardon me are you Aaron Burr, sir?

serversocket.listen(5) # listen for client connections

def separateCommands(data):
    decodedData = data.decode("utf-8") # process into readable format
    cleanData = decodedData.strip("\r\n") #strip extra characters
    commandPair = cleanData.split(", ") # separate into list of individual direction and distance commands
    return commandPair
    #* commands are now in a list as ['direction', 'time']

while True: # loop
    try:
        c, addr = serversocket.accept() # connects with client
        c.send(bytes("-------------------- \nEnter direction and time separated by ','\n",'ascii')) #send text back
        
        data = c.recv(1024) # reveive raw data
        commandList = separateCommands(data) # separate commands into individual strings

        Robot.Drive(commandList[0], float(commandList[1]))
    except:
        print("SockerServer.py.WhileLoop :(")
    finally:
        c.close() # closes connection
        print ('\nConnection closed.\n')
