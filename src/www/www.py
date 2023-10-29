import os
import logging
import threading
from flask import Flask, request, send_from_directory

www = Flask(__name__)
logOutput = logging.getLogger('werkzeug')
logOutput.disabled = True

WHOST = '127.0.0.1'
WPORT = 8080

@www.route('/', methods=['GET','POST'])
def main():

	osHeader = request.headers.get('User-Agent')
	parameter = request.args.get('something')

	if ( "Linux" in osHeader ):
		downloadFilePath = os.path.join(www.root_path, "../../bin/Linux/")
		return send_from_directory(downloadFilePath, "main.cpp")

	elif ( "Windows" in osHeader ):
		downloadFilePath = os.path.join(www.root_path, "../../bin/Windows/")
		return send_from_directory(downloadFilePath, "main.cpp")

	else:
		return "False"

def serveWebPage(): www.run(host=WHOST, port=WPORT)
def serverWebPageThreaded(): threading.Thread(target=serveWebPage).start()

