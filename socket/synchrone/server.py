#!/usr/bin/env python3

import socket
import sys
import logging

logging.basicConfig(level=logging.DEBUG)

HOST = ("127.0.0.1", int(sys.argv[1]))

BYE = "bye"
ARRET = "arret"

connections = []


def main():
    server = socket.socket()
    server.bind(HOST)
    server.listen(5)

    
    msgcl = ""
    msgsrv = ""
    while ARRET not in (msgcl, msgsrv):
        conn, address = server.accept()
        if conn not in connections:
            logging.info(f"Connected to {address}")
            connections.append(conn)
        
        msgcl = ""
        msgsrv = ""

        while BYE not in (msgcl, msgsrv) and ARRET not in (msgcl, msgsrv):
            try:
                msgcl = conn.recv(1024).decode()
                print(msgcl)
                if str(msgcl) == BYE or str(msgcl) == ARRET:
                    break
                msgsrv = input("Message:")
                conn.send(msgsrv.encode())
            except BrokenPipeError:
                logging.error(f"BrokenPipeError with {address}")
                break
        
        if str(msgcl) == BYE or str(msgsrv) == BYE:
            logging.info(f"Closing connection with {address}...")
            conn.send(BYE.encode())


    # Quand ARRET est envoyé (normalement jespere plz help)
    logging.info("Stopping server...")
    try:
        conn.send(ARRET.encode())
    except BrokenPipeError: # On s'en fout de l'erreur ici honnetement, elle arrive quand le serv veut l'arret car le client est déjà déco...
        pass
    for i in connections: # il y a moyen que ça pose problème plus tard car on déco déjà une conn avant
        i.close()
    server.close()
    sys.exit(0)


if __name__ == "__main__":
    main()
