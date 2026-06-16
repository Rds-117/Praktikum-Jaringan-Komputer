from socket import *
import threading

def handle_client(connectionSocket):
    try:
        #menerima pesan user
        message = connectionSocket.recv(1024).decode()

        message = message[4:16]
        print(message)


        #isi message = /GET /index.html HTTP/1.1
        #filename = message.split()[1]


        f = open(message[1:])

        outputdata = f.read()


        #kirim respon
        connectionSocket.send(
                "HTTP/1.1 200 OK\r\n\r\n".encode()
             )
        

        #KIRIM DATA
        connectionSocket.sendall(outputdata.encode())


        #close connection
        connectionSocket.close()
    

        #error
    except IOError:
        #kirim respon untuk error not found
        connectionSocket.send(
            "HTTP/1.1 404 NOT FOUND\r\n\r\n".encode()
            )
        

        #kirim data

        connectionSocket.send(
            "<h1>404 Not Found</h1>".encode()
        )
        
        #close connection
        connectionSocket.close()
                    
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', 6767))
serverSocket.listen(5) # menerima sebanyak 5 client
print("[SYSTEM] system is running...")



while True:
    connectionSocket, addr = serverSocket.accept()



    thread = threading.Thread(
        target=handle_client,
        args=(connectionSocket,)
        )


    thread.start()