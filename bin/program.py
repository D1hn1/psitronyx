#!/usr/bin/python3

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

if __name__ == "__main__":
	threading.Thread(target=keepAliveToServerThreaded, args=(SERVER_KA_IP, SERVER_KA_PORT)).start()
