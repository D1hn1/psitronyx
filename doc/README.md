# PSITRONYX DOCUMENTATION

![](./image.png)

## 1. Downloading and Dependences
```shell
$ git clone https://github.com/d1hn1/psitronyx
$ cd psitronyx

$ sudo apt install python3-dialog
$ pip3 install flask
$ pip3 install logging
```
> Start by clonning the repo into your local machine, then cd into it. Then you will have to install some things like python3-dialog and some pip3 libraries like flask and logging that´s already in the sistem but just in case.

## 2. Ussage
```shell
$ python3 main.py
```
> To start PSITRONYX you just have to python3 main.py, so do it. You will have in front a dialog style UI waiting for connections. In the background there´s a port receiving Keep Alive requests and another for a web to download the ../bin/ckacnm.pyw file.

## 3. Configuring the ckacnm.pyw file
```python3
#!/usr/bin/python3

import os
import time
import socket
import threading

CLIENT_IP = '0.0.0.0' #
CLIENT_PORT = 10011 #

SERVER_KA_IP 	= '127.0.0.1' #
SERVER_KA_PORT	= 10010 #
```
> Here is a portion of the file, you will have to change (or not) the variables marked with # according to your configuration
