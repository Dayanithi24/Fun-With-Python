import socket
import json

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# IP and port to listen on
server_address = ('localhost', 12345)
sock.bind(server_address)
sock.listen(1)

print("Waiting for a connection...")
connection, client_address = sock.accept()
print("Connected to:", client_address)
connection.send(str.encode("Welcome To Amazon"))

# Receive buffer size
buffer_size = 8192

# Dictionary to send
data_dict = {"1": "Redmi Note 10 pro", "2": "Lenovo Ideapad Slim 3","3":"Exit"}
p_dict={"1":{"Product_Name":"Redmi Note 10 pro","Price":"20,000","Ram | Rom":"6GB | 128GB","Colours":"Black, Blue, Red"},"2":{"Product_Name":"Lenovo Ideapad Slim 3","Price":"79,990","Processor":"Intel i5","Display":"15.46 inch","OS":"Windows 10","RAM | ROM":"8GB | 512GB SSD"}}

data = connection.recv(buffer_size)
if(data.decode()=="start"):

    # Serialize the dictionary to JSON and encode as bytes
    json_data = json.dumps(data_dict).encode()

    # Send the data
    connection.sendall(json_data)
while True:
    a=connection.recv(buffer_size).decode()
    print(a)
    if a=='3':
        break
    connection.sendall(json.dumps(p_dict[a]).encode())

print("Connection Ended")
# Close the connection and socket
connection.close()
sock.close()
