# import socket

# msgFromClient       = "Hello UDP Server"

# bytesToSend         = str.encode(msgFromClient)

# serverAddressPort   = ("127.0.0.1", 20001)

# bufferSize          = 1024

# UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# UDPClientSocket.sendto(bytesToSend, serverAddressPort)

# msgFromServer = UDPClientSocket.recvfrom(bufferSize)

# msg = "Message from Server {}".format(msgFromServer[0])

# print(msg)

import socket
import struct

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# IP and port of the receiver (server)
server_address = ('localhost', 12345)

# Float data to send
float_data = float(input("Enter the reading:"))

# Pack float data as bytes using struct
data = struct.pack('f', float_data)

# Send the data
sock.sendto(data, server_address)
print(sock.recvfrom(1024)[0].decode())
print(32*'*')

# buffer_size = struct.calcsize('f')
# m,d=sock.recvfrom(buffer_size)
# print(struct.unpack('f',m)[0])
print(sock.recvfrom(1024)[0].decode())
print(32*'*')

# Close the socket
sock.close()