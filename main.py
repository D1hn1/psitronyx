#/usr/bin/pythnon3

import sys
sys.path.insert(0, "./src/code/")
sys.path.insert(0, "./src/www/")

from www import serverWebPageThreaded
from kam import listenForKeepAliveThreaded
from vscnm import hostDialogVisualization

KEEP_ALIVE_PORT = 10010
KEEP_ALIVE_IP	= '127.0.0.1'
CLIENT_CONNECTION_PORT = 10011
DIALOG_BIN_PATH = "/usr/bin/dialog"
DEVICES_CONNECTED = [("0","Update Page")]

listenForKeepAliveThreaded(KEEP_ALIVE_PORT, KEEP_ALIVE_IP, DEVICES_CONNECTED, False)
serverWebPageThreaded()

while True:
    hostDialogVisualization(DEVICES_CONNECTED, DIALOG_BIN_PATH, CLIENT_CONNECTION_PORT)

# MAKE HERE THE START OF THE PROGRAM

