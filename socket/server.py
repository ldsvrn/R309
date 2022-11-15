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
        data = conn.recv(1024).decode()
        print(data)
        match str(data):
            case "bye":
                logging.info(f"Closing connection with {address}...")
                conn.send(BYE.encode())
                break
            case "arret":
                logging.info("Stopping server...")
                conn.send(ARRET.encode())
                for i in connections:
                    i.close()
                server.close()
                sys.exit(0)
        conn.send("ack".encode())
    conn.close()


if __name__ == "__main__":
    main()
