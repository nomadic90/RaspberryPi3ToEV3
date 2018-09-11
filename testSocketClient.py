import socket

# HOST = '192.168.0.9'
HOST = '172.30.1.38'
PORT = 50008


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

direction = "forward"
value = 10

s.send('right,1'.encode())

s.close()