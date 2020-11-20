import socket
from time import sleep

__author__ = "Stringtheory"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('127.0.0.1', 9000))

while (True):
    client.send(b'Stringtheory Github.')
    response = client.recv(4096)

    print(response)
    sleep(5)

'''

Output:
    Loop:
        Client:
            Connect:
                - Address: 127.0.0.1
                - Port: 9000
            - Client send message to server server.
            - Recieve message response from the server.

''
