#!/usr/bin/python3

import socket
import threading
from log import LOG

# KAM ( Keep Alive Method )

def listenForKeepAlive(KAPORT, KAIP, KALIST, STDOUT):

	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as karoot:

		with LOG(STDOUT=STDOUT) as log:

			TEMPLIST = []
			NUMBER = 1

			try:
				karoot.bind((KAIP,KAPORT))
				karoot.listen(10)

			except socket.error as error:
				karoot.close()
				log.log(log.CRITIC, f"{error}")
				exit(1)

			log.log(log.INFO, f"Started KA Listener in {KAIP}:{KAPORT}")

			while True:

				try:
					clientSock, ConnData = karoot.accept()
					clientSock.recv(1024)
					
					# TODO: MAKE SOMETHING WITH THE DATA

				except socket.error as error:
					log.log(log.WARN, f"{error}")
		
				log.log(log.INFO, f"Connection from {ConnData}")

				if ( ConnData[0] not in TEMPLIST ):
					KALIST.append((str(NUMBER), f"{ConnData[0]} {ConnData[1]}"))
					TEMPLIST.append(ConnData[0])
					NUMBER+=1				

				clientSock.close()

def listenForKeepAliveThreaded(KAPORT, KAIP, KALIST, STDOUT):

	threading.Thread(target=listenForKeepAlive, args=(KAPORT, KAIP, KALIST, STDOUT)).start()
