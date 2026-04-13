from socket import *

serverName = "local"
serverPort = 12000

#AF_INET = IPV4 | SOCK_STREAM = TCP
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect(
    (serverName, serverPort)
)

print("[SYSTEM] Masukan pesan")

running = True
while running:
    message = input("> ")

    clientSocket.send(message.encode())

    if message == "exit":
        print("[SYSTEM] Keluar dari program ")
        running = False
        break


    modifiedMessage = clientSocket.recv(2048)

    print("[SERVER] pesan: ", modifiedMessage.decode())


clientSocket.close()
print("[SYSTEM] Socket ditutup")