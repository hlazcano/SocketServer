import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1120))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print("Connection stablished!")
    print(f"{address}")
    clientsocket.send(bytes("Successfully connected", "utf-8"))
    clientsocket.close()