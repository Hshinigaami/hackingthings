import socket

HOST='127.0.0.1'
PORT=62345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST,PORT))
	s.sendall(b'Hello World') # sending in binary
	data=s.recv(1024) # Whatever server is sending

print(data)