import socket
import RobotControl as Robot

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host and port
serversocket.bind(('0.0.0.0', 1782)) #* pardon me are you Aaron Burr, sir?

serversocket.listen(5) # 'listens' for client connection, queue 5 or less requests

def separateCommands(data):
    decodedData = data.decode("utf-8") #process into readable format
    CommandPairs = decodedData.split(":") #separates into individual direction and distance commands
    #where data is in the format (direction, time)

while True: #loop
    c, addr = serversocket.accept() #connects with client
    c.send(bytes("-------------------- \nEnter commands separated by ':'\n",'ascii')) #send text back
    
    data = c.recv(1024) #reveive raw data
    separateCommands(data) #separate commands into individual strings
   
    c.close() #closes connection
    print ('\nConnection closed.\n')