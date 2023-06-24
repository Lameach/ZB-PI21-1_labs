import socket, threading


class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientSocket):
        threading.Thread.__init__(self)
        self.csock = clientSocket
        print ('New connection added: ', clientAddress)

    def run(self):
        print ('Connection from:', clientAddress)
        self.csock.send(bytes('Hello! This is server.', 'utf-8'))
        msg = ''
        while True:
            data = self.csock.recv(2048)
            msg = data.decode()
            if msg == 'exit':
                break

            print('Client:', msg)
            self.csock.send(bytes(msg,'UTF-8'))

        print ('Client at', clientAddress, 'disconnected.')

LOCALHOST = "127.0.0.1"
PORT = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print('Server started')
print('Waiting for client request.')

while True:
    server.listen(1)
    clientSock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientSock)
    newthread.start()

