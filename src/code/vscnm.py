#/usr/bin/python3

import os
import socket
from log import LOG
from dialog import Dialog

# VSCNM ( Visualization & Connection Method  )

with LOG(STDOUT=False) as log:
		log.log(log.INFO, "Started Visualization Module")

def hostDialogVisualization(VLIST, VBIN_PATH):
	
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
				CLIENT_PORT = data[1].split(" ")[1]
				CMD = ""
				
				print("Type exit to terminate the session")

				while ( CMD != "exit" ):

					with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as vsroot:
						CMD = input(f"{CLIENT_IP} $ ")

						# TODO: MAKE HERE THE INTERACTIVE SHELL

				os.system("clear")
