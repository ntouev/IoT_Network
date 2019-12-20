import socket

SERVER = "192.168.1.185"
#SERVER = "127.0.0.1"
PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))

while True:
    
    #user gives input
    out_data = input('Give input... ')

    print("sending: ", out_data)

    client.sendall(out_data.encode())

    #wait for response
    in_data = client.recv(1024)
    in_data = in_data.decode()

    #print the response
    print("Received: ", in_data)
