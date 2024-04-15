# import socket
# client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# client.connect(('103.196.28.171',8080))
# client.send("I am client\n")
# from_server=client.recv(4096)
# client.close()
# print(from_server)

import socket
import json

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# IP and port of the receiver (server)
server_address = ('localhost', 12345)

# Connect to the server
sock.connect(server_address)

buffer_size=8192

print(sock.recv(buffer_size).decode())

s=input()
sock.send(str.encode(s))

# Receive the data
data = sock.recv(buffer_size)

# Deserialize the JSON data into a dictionary
received_dict = json.loads(data.decode())

print("Choose Product:")
for i in received_dict.items():
    print(i[0]+"."+i[1])

while True:

    a=input()
    if(a=='3'):
        sock.send(str.encode(a))
        break
    elif a>'0' and a<'3':
        sock.send(str.encode(a))
    else:
        print("Invalid Input")
        continue

    p=sock.recv(buffer_size)
    p1=json.loads(p.decode())


    print("Product details:")
    for i in p1.items():
        print(i[0]+" : "+i[1])


# Close the socket
sock.close()
