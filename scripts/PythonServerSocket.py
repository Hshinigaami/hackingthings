# Sockets have different types, the ones which we are using in this tutorial is Internet socket (Berkley Socket or BSD Sockets)
# There is also Unix Socket, which is used for intercommunication between processes.

# Pythons Socket module provides an interface to Berkley Socket API

# First lets create a socket using socket object => socket.socket()
# Then we need to specify what stream we would be using TCP or UDP
# socket.SOCK_STREAM => TCP Stream => reliable since data is send in order and can be resend if dropped
# socket.SOCK_DGRAM => UDP Stream => Not in order and cannot be resend again

import socket

HOST='127.0.0.1'
PORT=62345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST,PORT))
	s.listen()
	conn,addr=s.accept()

	with conn:
		print(f"Connected by {addr}")
		while True:
			data=conn.recv(1024)
			if not data:
				break
			conn.sendall(data)
