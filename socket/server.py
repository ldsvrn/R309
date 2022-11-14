#!/usr/bin/env python3

import socket
import sys
import threading

connections = []

host = "127.0.0.1"
port = int(sys.argv[1])
reply = "reply"

def recieve_thread():
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(5)
    while True:
        conn, address = server_socket.accept()
        if conn not in connections:
            connections.append(conn)
        data = conn.recv(1024).decode()
        print(data)
        conn.send(reply.encode())

if __name__ == "__main__":
    t = threading.Thread(target=recieve_thread)
    t.start()
    t.join()