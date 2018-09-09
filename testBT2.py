#! /usr/bin/env python3
import serial
import time
import EV3BT

EV3 = serial.Serial('/dev/rfcomm0')

while True:

    typedMessage = input('type any message : ')

    if typedMessage == 'quit':
        break
                        
    s = EV3BT.encodeMessage(EV3BT.MessageType.Numeric, 'abc', int(typedMessage))
    print(EV3BT.printMessage(s))
    EV3.write(s)
    time.sleep(1)

EV3.close()

