#! /usr/bin/env python3
import serial
import time
import EV3BT

EV3 = serial.Serial('/dev/rfcomm0')

while True:

    direction = input("type mode (forward, right, left) :")
    inputValue = input("type value : ")

    print(direction, inputValue)

    value = EV3BT.encodeMessage(EV3BT.MessageType.Numeric, direction, inputValue)
    EV3.write(value)

    w = EV3.inWaiting()
    if w != 0:
        n = EV3.read(w)
        mail, value, n = EV3BT.decodeMessage(n, EV3BT.MessageType.Numeric)
        print(mail, value)
    else:
        time.sleep(0.1)

EV3.close()


