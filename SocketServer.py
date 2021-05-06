import socket
#import RobotDrive as Drive

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host and port
serversocket.bind(('0.0.0.0', 1782)) #* pardon me are you Aaron Burr, sir?

serversocket.listen(5) # 'listens' for client connection, queue three or less requests

def separateCommands(data):
    decodedData = data.decode("utf-8") #process into readable format
    splitCommands = decodedData.split(":") #separates each command into a list item
    Drive_Command_List = [] #create empty list
    for x in splitCommands: #strips white space and adds to final list
       command = x.strip()
       print(command)
       Drive_Command_List.append(command) #create new list of properly formatted commands
    return Drive_Command_List #ready to send to drive script

while True: #loop
    c, addr = serversocket.accept() #connects with client
    c.send(bytes("-------------------- \nEnter commands separated by ':'\n",'ascii')) #send text back
    
    data = c.recv(1024) #reveive raw data
    separateCommands(data) #separate commands into individual strings
   
    c.close() #closes connection
    print ('\nConnection closed.\n')