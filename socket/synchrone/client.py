#!/usr/bin/env python3

import socket
import sys
import logging

logging.basicConfig(level=logging.DEBUG)

HOST = ("127.0.0.1", int(sys.argv[1]))

BYE = "bye"
ARRET = "arret"


def main():
    client = socket.socket()
    client.connect(HOST)

    msgcl = ""
    msgsrv = ""
    while BYE not in (msgcl, msgsrv) and ARRET not in (msgcl, msgsrv):
        msgcl = input("Message:")
        client.send(msgcl.encode())
        msgsrv = client.recv(1024).decode()
        print(msgsrv)
    client.close()


if __name__ == "__main__":
    main()
