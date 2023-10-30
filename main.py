#/usr/bin/pythnon3

import sys
sys.path.insert(0, "./src/code/")
sys.path.insert(0, "./src/www/")

from www import serverWebPageThreaded
from kam import listenForKeepAliveThreaded
from vscnm import hostDialogVisualization

HOST_IP = '0.0.0.0'

WEB_PORT = 8080
KEEP_ALIVE_PORT = 10010
CLIENT_CONNECTION_PORT = 10011

DIALOG_BIN_PATH = "/usr/bin/dialog"
DEVICES_CONNECTED = [("0","Update Page")]

listenForKeepAliveThreaded(KEEP_ALIVE_PORT, HOST_IP, DEVICES_CONNECTED, False)
serverWebPageThreaded(HOST_IP, WEB_PORT)

while True:
    hostDialogVisualization(DEVICES_CONNECTED, DIALOG_BIN_PATH, CLIENT_CONNECTION_PORT)
