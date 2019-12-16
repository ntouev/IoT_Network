import socket

SERVER = "127.0.0.1"
PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))

while True:
    print("Give input...")
    out_data = input()      #user gives input
    out_data = out_data.encode()

    if out_data == 'bye':
        client.close()

    print("sending...")

    client.sendall(out_data)

    in_data = client.recv(1024)
    in_data = in_data.decode()

    print("Received: ", in_data)
