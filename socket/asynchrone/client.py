#!/usr/bin/env python3

import socket
import sys
import logging
import threading

logging.basicConfig(level=logging.DEBUG)

HOST = ("127.0.0.1", int(sys.argv[1]))

BYE = "bye"
ARRET = "arret"


def handle_client(client):
    msgsrv = ""
    while msgsrv != BYE and msgsrv != ARRET:
        msgsrv = client.recv(1024).decode()
        print(f"Reçu du serveur: {msgsrv}")
    client.close()

def main():
    client = socket.socket()
    client.connect(HOST)

    client_handler = threading.Thread(target=handle_client, args=[client])
    client_handler.start()

    msgcl = ""
    while msgcl != BYE and msgcl != ARRET:
        msgcl = input("Message:")
        client.send(msgcl.encode())
    client.close()


if __name__ == "__main__":
    main()
