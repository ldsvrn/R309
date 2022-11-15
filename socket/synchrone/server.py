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
    conn, address = server.accept()
    if conn not in connections:
        logging.info(f"Connected to {address}")
        connections.append(conn)
    while True:
        try:
            data = conn.recv(1024).decode()
            print(data)
            if str(data) == BYE:
                logging.info(f"Closing connection with {address}...")
                conn.send(BYE.encode())
                break
            elif str(data) == ARRET:
                logging.info("Stopping server...")
                conn.send(ARRET.encode())
                for i in connections:
                    i.close()
                server.close()
                sys.exit(0)
            conn.send("ack".encode())
        except BrokenPipeError:
            logging.error(f"BrokenPipeError with {address}")
            break
    conn.close()


if __name__ == "__main__":
    main()
