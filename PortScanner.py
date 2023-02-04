# Port scanner will scan the open ports on an IP Address

# 1. Import the socket module to start a connection between two nodes (Done)
# 2. Get the IP Address from user (Done)
# 3. Make a connection to IP Address (Done)
# 4. Scan for ports (Done)
# 5. Display the result and throw some errors if any. (Done)

import socket
import sys # To get the arguments supplied by user
from datetime import datetime as dt# Just as  show

def line_broke():
	print('*'*50)

line_broke()
print('Port Scanner is starting')
print(f'Start Time: {dt.now()}')
line_broke()


# print(sys.argv)
if len(sys.argv) == 2:
	target = sys.argv[1] #This is what I will do
	target = socket.gethostbyname(sys.argv[1]) # This will convert the Hostname to IP Address (IPV4), it will only return one IP Address whereas the hostname might resolve into multiple IP Address
	print(f'Scanning for the target {target}')
	line_broke()
else:
	print('Nope, You supplied wrong number of arguments')
	line_broke()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	try:
		for ports in range(440, 444):
			results = s.connect_ex((target, ports)) # Establish a connection to some port
			# print(results)
			if(results == 0): # If it is open specify
				print(f'Port {posts} is open')
			s.close() # After connection is establish close the connection and start with fresh port
	except KeyboardInterrupt:
		print('Exiting the scanner')
		sys.exit()
	except socket.gaierror():
		print('Error with hostname provided')
		sys.exit()
	except socket.error():
		print('Error while establishing the connection')
		sys.exit()