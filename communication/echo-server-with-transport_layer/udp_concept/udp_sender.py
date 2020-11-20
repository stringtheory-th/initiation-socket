import socket
from time import sleep

__author__ = "Stringtheory"

UDP_ADDRESS = "127.0.0.1"
UDP_PORT = 2547

print(""" 
Target Address: %s
Target Port: %s
""" % (UDP_ADDRESS, UDP_PORT))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while (True):
    message = str(input("Message to send: "))
    sock.sendto(message.encode(), (UDP_ADDRESS, UDP_PORT))
    print("Send message to receiver.")
    sleep(1)

'''

Output:
    Loop:
        Sender:
            Information:
                - Target Address: 127.0.0.1
                - Target Port: 2547
        
            - Send the message to reciever
            - Wait for 1 second

'''
