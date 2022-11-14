#!/usr/bin/env python3

import socket
import sys
import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG)

message = "test"
host = "127.0.0.1"
port = int(sys.argv[1])

def recieve_thread():
    logging.debug("Created thread")
    client_socket = socket.socket()
    client_socket.connect((host, port))
    while True:
        data = client_socket.recv(1024).decode()
        print(data)

if __name__== "__main__":
    t = threading.Thread(target=recieve_thread)
    t.start()

    send_socket = socket.socket()
    send_socket.connect((host, port))
    while True:
        logging.debug("Sending test message")
        send_socket.send(message.encode())
        time.sleep(1)