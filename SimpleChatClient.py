import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 444

try:
    clientsocket.connect((host, port))
except:
    print("Unable to connect :( ")
    clientsocket.close()

while True:
    ClientMessage = input("CLIENT >>")
    clientsocket.send(ClientMessage.encode('utf-8'))

    print("Waiting for Server response...")

    ServerMessage = clientsocket.recv(1024)
    print("SERVER >> %s" % str(ServerMessage.decode('utf-8')))

    if ClientMessage == "EXIT" or ServerMessage == b"EXIT":
        print("connection closed!")
        clientsocket.close()
        break






