import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.bind(('0.0.0.0', 10007))

sock.listen(1)

connections = []

def handler(c,a):
	global connections
	while True:
		data = c.recv(1024)
		for connection in connections:
			if connection != c:
				connection.send(bytes(data))
			
		if not data:
			connections.remove(c)
			c.close()
			break

while True:
	c, a = sock.accept()
	cThread = threading.Thread(target=handler, args=(c,a))
	cThread.daemon = True
	cThread.start()
	connections.append(c)
	print(connections)
