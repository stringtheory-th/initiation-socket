import socket

__author__ = "Stringtheory"


def __remote_machine_info():
    while(True):
        remote_host = str(
            input("Enter the hostname [without protocols]: ")).lower()

        try:
            print("IP Address: %s\n" % socket.gethostbyname(remote_host))
        except socket.error as err_msg:
            print("%s: %s\n" % (remote_host, err_msg))

        try_again = str(input("Do you want try again? [Y/N]: ")).lower()
        if try_again == 'y':
            __remote_machine_info()
        else:
            break


if __name__ == '__main__':
    __remote_machine_info()


'''

Output:
    Loop:
        - Input
        - IP Address: <Value from Input>
        - Try again
            If == Else:
                - Break

'''
