import socket
import serial
import time
import EV3BT

HOST = ''
PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()

    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            # if not data: break
            recvData = data.decode()
            splitData = recvData.split(",")
            direction = splitData[0]
            value = int(splitData[1])

            print(direction, value)