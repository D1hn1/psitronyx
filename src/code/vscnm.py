#/usr/bin/python3

import os
import socket
from log import LOG
from dialog import Dialog

# VSCNM ( Visualization & Connection Method  )

with LOG(STDOUT=False) as log:
		log.log(log.INFO, "Started Visualization Module")

def hostDialogVisualization(VLIST, VBIN_PATH, CLIENT_PORT):
	
	dialogMain = Dialog(dialog=VBIN_PATH)
	dialogMain.set_background_title("PSITRONYX")
	code, tag = dialogMain.menu(f"Choose your option whisely", choices=[lista for lista in VLIST])
	
	if ( code == "cancel" ):
		dialogMain.clear()
		print("Ctrl-c to exit")
		exit(1)

	if ( int(tag) != 0 ):

		for data in VLIST:
			if ( tag == data[0] ):
				dialogMain.clear()
				
				CLIENT_IP = data[1].split(" ")[0]
				CLIENT_PORT_SRC = data[1].split(" ")[1]
				CMD = ""
				
				print("Type exit to terminate the session")

				while ( CMD != "exit" ):
					with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as vsroot:
						# TODO: HANDLE WITH TRY AND EXCEPT WHEN YOU CAN´T CONNECT TO A TARGET
						vsroot.connect((CLIENT_IP, CLIENT_PORT))
						vsroot.send(b"Helo")
						
						CMD = input(f"{CLIENT_IP} $ ")
						
						if ( CMD != "exit" ):
							vsroot.send(CMD.encode("utf-8"))
							message = vsroot.recv(1024).decode("utf-8")
							print(message)
							vsroot.close()	
						else:
							vsroot.send(b"Finalize")
							vsroot.close()

				os.system("clear")
