# import socket

 

# localIP     = "127.0.0.1"

# localPort   = 20001

# bufferSize  = 1024

 

# msgFromServer       = "Hello UDP Client"

# bytesToSend         = str.encode(msgFromServer)

 

# # Create a datagram socket

# UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# # Bind to address and ip

# UDPServerSocket.bind((localIP, localPort))

 

# print("UDP server up and listening")

 

# # Listen for incoming datagrams

# while(True):

#     bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

#     message = bytesAddressPair[0]

#     address = bytesAddressPair[1]

#     clientMsg = "Message from Client:{}".format(message)
#     clientIP  = "Client IP Address:{}".format(address)
    
#     print(clientMsg)
#     print(clientIP)

   

#     # Sending a reply to client

#     UDPServerSocket.sendto(bytesToSend, address)

import socket
import struct

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# IP and port to listen on
server_address = ('localhost', 12345)
sock.bind(server_address)

# Receive buffer size
buffer_size = struct.calcsize('f')

# Receive and unpack float data
data, address = sock.recvfrom(buffer_size)
read = struct.unpack('f', data)[0]

print("Received float:", read)
sock.sendto(str.encode("Welcome to TN Elictrical Board"),address)

a=0.0

if read<=100:
    pass
elif read>100 and read<=200:
    a=read*1.5
elif read>200 and read<=500:
    a=read*2
else:
    a=read*3

# sock.sendto(struct.pack('f',a),address)
if a==0.0:
    sock.sendto(str.encode("No Charge"),address)
else:
    sock.sendto(str.encode("Your Electricity Bill: "+str(a)),address)
    
# Close the socket
sock.close()
