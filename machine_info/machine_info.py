import socket

__author__ = "Stringtheory"


def __machine_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print("\nHostname: %s" % hostname)
    print("IP Address: %s\n" % ip_address)


if __name__ == "__main__":
    __machine_info()

'''

Output:
    - Hostname: <Your Hostname>
    - IP Address: <Your IP Address>
    
'''
