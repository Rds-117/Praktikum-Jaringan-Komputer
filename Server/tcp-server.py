from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(
    ('', serverPort)
)

serverSocket.listen(1)
print("[SYSTEM] server tcp siap digunakan")

running = True
while running: 

    connectionSocket, addr = serverSocket.accept()

    while True: 
        message = connectionSocket.recv(2048).decode()

        if not message:
            break

        if message.lower() == "exit":
            print("[SYSTEM] client ingin keluar")
            running = False
            break

    
        modifiedmessage = message.upper()
        print("[SERVER] diterima: ", modifiedmessage)

        connectionSocket.send(
            modifiedmessage.encode()
        )

    connectionSocket.close()

serverSocket.close()