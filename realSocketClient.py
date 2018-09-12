import socket
import serial
import time
import EV3BT

HOST = ''
PORT = 50010

EV3 = serial.Serial('/dev/rfcomm0')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # s.setblocking(0)
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)

            if not data:
                continue

            recvData = data.decode()
            print("data decoded : " + recvData)

            splitData = recvData.split(",")
            print(splitData)
            print(len(splitData))

            if len(splitData) != 2:
                time.sleep(1)
                continue
            
            try:
                
                direction = splitData[0]
                inputValue = splitData[1]
                intValue = int(inputValue)

                w = EV3.inWaiting()
                if w != 0:
                    n = EV3.read(w)
                    mail, value, n = EV3BT.decodeMessage(n, EV3BT.MessageType.Numeric)
                    print(mail, value)

                    if value > 50:
                        print(direction, intValue)
                        movement = EV3BT.encodeMessage(EV3BT.MessageType.Numeric, direction, intValue)
                        EV3.write(movement)

                else:
                    time.sleep(0.1)

            except Exception as e:
                print("check lego and bluetooth status!")
                continue

