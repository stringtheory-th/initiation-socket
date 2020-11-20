import socket
import threading

__author__ = "Stringtheory"

BIND_ADDRESS = '0.0.0.0'
BIND_PORT = 9000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((BIND_ADDRESS, BIND_PORT))
server.listen(5)
print('Listening on {}:{}'.format(BIND_ADDRESS, BIND_PORT))


def __handle_client_connection(client_socket):
    while (True):
        request = client_socket.recv(1024)
        print('Recieved {}'.format(request))
        client_socket.send(b'ACK!')


while (True):
    client_sock, address = server.accept()
    print('Accept connection from {}:{}'.format(address[0], address[1]))
    client_handler = threading.Thread(
        target=__handle_client_connection,
        args=(client_sock,)
    )
    client_handler.start()

'''

Output:
    Loop:
        Server:
            Information:
                - Address: 0.0.0.0 # No matter where they come from
                - Port: 9000
            - Recieve from client (message)
            - Send message for response ('ACK!')

'''
