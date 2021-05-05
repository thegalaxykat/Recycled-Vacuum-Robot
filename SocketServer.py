import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host and port
serversocket.bind(('0.0.0.0', 1776)) #* pardon me are you Aaron Burr, sir?

serversocket.listen(5) # 'listens' for client connection, queue three or less requests

def separate_commands(data):
    decodedData = data.decode("utf-8") #process into readable format
    splitCommands = decodedData.split(":") #separates each command into a list item
    for x in splitCommands: #strips white space
       command = x.strip()
       print(command)

while True:
    c, addr = serversocket.accept() #connects with client
    c.send(bytes("-------------------- \nEnter commands separated by ':'\n",'ascii')) #send text back
    
    data = c.recv(1024) #reveive raw data
    separate_commands(data)  
   
    c.close() #closes connection
    print ('\nConnection closed.\n')