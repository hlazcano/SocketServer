import socket

HEADER = 64 #THE HEADER TELLS NUMBER OF BYTES THAT WE WILL REQUIRE FOR THE NEXT MESSAGE
PORT = 1120
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send("HELLO WORLD!")
input()
send("This is another test")
input()
send("it doesn't matter, the length it will be handled")

send(DISCONNECT_MESSAGE)
'''
#Old Code
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.1.8", 1120))

full_msg = ''
while True:
    msg = s.recv(16)
    if len(msg) <=0:
        break
    full_msg += msg.decode("utf-8")

    print(full_msg)
    '''