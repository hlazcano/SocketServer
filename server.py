import socket

import threading

HEADER = 64 #THE HEADER TELLS NUMBER OF BYTES THAT WE WILL REQUIRE FOR THE NEXT MESSAGE
PORT = 1120
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected =True
    while connected:

        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            #How many bytes will we receive
            #Will wait until it receives the msg
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}]:: {msg}")
            conn.send("Received message!".encode(FORMAT))
    conn.close()

#New connections
def start():
    serverSocket.listen()
    print(f"[LISTENING] Server is listening on {ADDR}")
    while True:
        conn, addr = serverSocket.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1 }")
        thread.start()

print(f"Starting server...")
start()

'''
#Old Code
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("192.168.1.8", 1120))
s.listen(16)

while True:
    clientsocket, address = s.accept()
    print("Connection stablished!")
    print(f"{address}")
    clientsocket.send(bytes("Successfully connected", "utf-8"))
    clientsocket.close()
    '''