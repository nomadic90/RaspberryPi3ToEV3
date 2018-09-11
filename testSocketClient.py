import socket

HOST = '192.168.0.9'
PORT = 50007


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

direction = "forward"
value = 10

s.send('right,0.5'.encode())

s.close()