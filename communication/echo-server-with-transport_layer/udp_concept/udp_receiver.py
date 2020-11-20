import socket

__author__ = "Stringtheory"

UDP_ADDRESS = "127.0.0.1"
UDP_PORT = 2547

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_ADDRESS, UDP_PORT))

while (True):
    print("Waiting for new messages to arrive, please wait. ..")
    data, addr = sock.recvfrom(1024)
    print("\nRecieved Message from Sender: ", data)

'''

Output:
    Loop:
        Reciever:
            Information:
                - Address: 127.0.0.1
                - Port: 2547

            - Waiting message from send
            If sender send message to reciever:
                - reciever show message from sender

'''
