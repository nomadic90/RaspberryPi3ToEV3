import io
import socket
import struct
import time
import picamera

# client_socket = socket.socket()
# client_socket.connect(('http://127.0.0.1', 8000))
# connection = client_socket.makefile('wb')

try:
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.framerate = 30
        start = time.time()
        count = 0
        stream = io.BytesIO()
        for foo in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
            # connection.write(struct.pack('<L', stream.tell()))
            # connection.flush()
            stream.seek(0)
            # connection.write(stream.read())
            count += 1

            print(foo)

            if time.time() - start > 30:
                break

            stream.seek(0)
            stream.truncate()
    connection.write(struct.pack('<L', 0))
finally:
    connection.close()
    client_socket.close()
    finish = time.time()