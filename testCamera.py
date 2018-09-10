import io
import socket
import struct
import time
import picamera
import sys
import websocket

def cameraTest():

    print(sys.argv[1], sys.argv[2])

    # client_socket = socket.socket()
    # client_socket.connect((sys.argv[1], int(sys.argv[2])))
    # connection = client_socket.makefile('wb')
    # print(connection)

    # factory = WebSocketClientFactory("ws://172.30.1.45:8000")

    # ws = create_connection("ws://172.30.1.45:8000")

    # ws = websocket.WebSocket()
    # ws.connect("ws://172.30.1.45:8000")

    try:
        socket.gethostbyname(sys.argv[1])
    except socket.error:
        print("Invalid host name. Exiting. Next time enter in proper format.")
        sys.exit()

    host = sys.argv[1]

    try:
        port = int(sys.argv[2])
    except ValueError:
        print("Error. Exiting. Please enter a valid port number.")
        sys.exit()
    except IndexError:
        print("Error. Exiting. Please enter a valid port number next time.")
        sys.exit()

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        print("Client socket initialized")
        s.setblocking(0)
        s.settimeout(15)
    except socket.error:
        print("Failed to create socket")
        sys.exit()

    try:
        s.sendto("".encode('utf-8'),(host, port))
    except ConnectionResetError:
        print(
            "Error. Port numbers are not matching. Exiting. Next time please enter same port numbers.")
        sys.exit()


    print("Checking for acknowledgement")
    try:
        ClientData, clientAddr = s.recvfrom(4096)
    except ConnectionResetError:
        print(
            "Error. Port numbers not matching. Exiting. Next time enter same port numbers.")
        sys.exit()
    except:
        print("Timeout or some other error")
        sys.exit()

    text = ClientData.decode('utf8')
    print(text)
    print("We shall start sending data.")

    # stream out!
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
                stream.seek(0)
                # connection.write(stream.read())
                # count += 1

                c = 0

                size = os.stat(stream)
                sizeS = size.st_size  # number of packets
                #sizeS = sizeS[:-1]
                print("File size in bytes: " + str(sizeS))
                Num = int(sizeS / 4096)
                Num = Num + 1
                print("Number of packets to be sent: " + str(Num))
                till = str(Num)
                tillC = till.encode('utf8')
                s.sendto(tillC, clientAddr)
                tillIC = int(Num)

                while tillIC != 0:

                    #Run = GetRun.read(1024)
                    Run = stream.read()
                    # print(str(Run))
                    #CLC = CL[1].encode('utf-8')
                    # GetRun.close()
                    #propMsg = b"put" + b"|||" + CLC + b"|||" + Run
                    s.sendto(Run, clientAddr)
                    c += 1
                    tillIC -= 1
                    print("Packet number:" + str(c))
                    print("Data sending in process:")

                GetRun.close()

                if time.time() - start > 20:
                    break

                stream.seek(0)
                stream.truncate()

        # connection.write(struct.pack('<L', 0))
    finally:
        connection.close()
        client_socket.close()
        finish = time.time()

if __name__ == "__main__":
    cameraTest()