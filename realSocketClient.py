import socket
import serial
import time
import EV3BT

HOST = ''
PORT = 50007

EV3 = serial.Serial('/dev/rfcomm0')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()

    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)

            recvData = data.decode()
            print(recvData)

            splitData = recvData.split(",")
            direction = splitData[0]

            value = float(splitData[1])

            print(direction, value)
            
            '''
            w = EV3.inWaiting()
            if w != 0:
                n = EV3.read(w)
                mail, value, n = EV3BT.decodeMessage(n, EV3BT.MessageType.Numeric)
                print(mail, value)
            else:
                time.sleep(0.1)

            if value > 50:
                movement = EV3BT.encodeMessage(EV3BT.MessageType.Numeric, direction, inputValue)
                EV3.write(movement)
            '''

