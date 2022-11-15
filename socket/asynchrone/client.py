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
        print(f"\nReçu du serveur: {msgsrv}")
    client.close()

def main():
    client = socket.socket()
    try:
        client.connect(HOST)
    except PermissionError:
        print(f"Permissions insuffisantes pour utiliser le port {HOST[1]}")
        sys.exit(13) # EACCES Permission denied
    except ConnectionRefusedError:
        print(f"Impossible de ce connecter au serveur {HOST}")
    else:
        client_handler = threading.Thread(target=handle_client, args=[client])
        client_handler.start()

        msgcl = ""
        while msgcl != BYE and msgcl != ARRET:
            msgcl = input("Message:")
            client.send(msgcl.encode())
        client.close()


if __name__ == "__main__":
    main()
