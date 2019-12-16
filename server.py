import socket
import threading
import subprocess

class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        #listen for up to 4 connections, then reject
        self.sock.listen(4)
        while True:
            (client, address) = self.sock.accept()
            threading.Thread(target = self.listenToClient,args = (client,address)).start()

    #The following is threaded
    def listenToClient(self, client, address):
        size = 1024
        while True:
            try:
                data = client.recv(size)
                if data:
                    #give data as arg in the executable and redirect its output
                    #to retrieve output data
                    proc = subprocess.Popen(['./test_exec', data], stdout=subprocess.PIPE,)
                    response = proc.communicate()[0]
                    #send it to the client
                    client.sendall(response)
                else:
                    raise error('Client disconnected')
            except:
                client.close()
                return False

if __name__ == "__main__":
    while True:
        port_number = input("Which port to listen to? ")
        try:
            port_number = int(port_number)
            break
        except ValueError:
            pass

    ThreadedServer('0.0.0.0',port_number).listen()
    #ThreadedServer('localhost',port_number).listen()
