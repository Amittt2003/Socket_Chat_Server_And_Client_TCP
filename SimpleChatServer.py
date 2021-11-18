import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 444

try:
    serversocket.bind((host, port))
    serversocket.listen(3)
except:
    print("Unable to start the server :(")

print("SERVER STARTED!" + "\r\n" + "Waiting for connection...")

while True:
    clientsocket, address = serversocket.accept()
    print("received connection from %s" % str(address))
    while True:
        ClientMessage = clientsocket.recv(1024)
        print("CLIENT >> %s" % str(ClientMessage.decode('utf-8')))
        serverMessage = input("Server >> ")
        clientsocket.sendto(serverMessage.encode('utf-8'), address)

        print("Waiting for Client response...")

        if ClientMessage == b"EXIT":
            clientsocket.close()
            print("connection closed!" + "\r\n" + "waiting for new connection...")
            break
        elif serverMessage == "EXIT":
            print("server closed!")
            break
    if serverMessage == "EXIT":
        serversocket.close()
        break


