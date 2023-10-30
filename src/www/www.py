import os
import logging
import threading
from flask import Flask, request, send_from_directory

www = Flask(__name__)
logOutput = logging.getLogger('werkzeug')
logOutput.disabled = True

@www.route('/', methods=['GET','POST'])
def main():

	downloadFilePath = os.path.join(www.root_path, "../../bin/")
	return send_from_directory(downloadFilePath, "ckacnm.py")

def serveWebPage(WHOST, WPORT): www.run(host=WHOST, port=WPORT)
def serverWebPageThreaded(WHOST, WPORT): threading.Thread(target=serveWebPage, args=(WHOST,WPORT)).start()

