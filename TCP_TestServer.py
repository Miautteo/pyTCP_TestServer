import socket as S

encoding = "utf-8"

##Establish listen on Port
socket = S.socket(S.AF_INET, S.SOCK_STREAM)
socket.bind(('localhost', 11000))
socket.listen(5)

while True:
    ##Establish Connection
    clientsocket, address = socket.accept()
    print(f"Connection from {address}")

    ##Recieve data from connection
    recvData = clientsocket.recv(1024)
    recvMsg = recvData.decode(encoding)
    print(recvMsg)

    ##Respond with data
    SendData = bytes(":Empfangen:", encoding)
    clientsocket.send(SendData)

    ##Close Connection
    clientsocket.close()

socket.close()