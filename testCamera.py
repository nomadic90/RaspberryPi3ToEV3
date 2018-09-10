import io
import socket
import struct
import time
import picamera
import sys
from websocket import create_connection

def cameraTest():

    print(sys.argv[1], sys.argv[2])

    # client_socket = socket.socket()
    # client_socket.connect((sys.argv[1], int(sys.argv[2])))
    # connection = client_socket.makefile('wb')
    # print(connection)

    # factory = WebSocketClientFactory("ws://172.30.1.45:8000")

    ws = create_connection("ws://172.30.1.45:8000")

    try:
        with picamera.PiCamera() as camera:
            camera.resolution = (640, 480)
            camera.framerate = 30
            start = time.time()
            count = 0
            stream = io.BytesIO()
            print("start steam")
            for foo in camera.capture_continuous(stream, sys.argv[3], use_video_port=True):
                # connection.write(struct.pack('<L', stream.tell()))
                # connection.flush()
                # stream.seek(0)
                # connection.write(stream.read())
                # count += 1

                # print(foo)

                if time.time() - start > 2:
                    break

                # stream.seek(0)
                # stream.truncate()

                ws.send(foo)

        # connection.write(struct.pack('<L', 0))
    finally:
        connection.close()
        client_socket.close()
        finish = time.time()

if __name__ == "__main__":
    cameraTest()