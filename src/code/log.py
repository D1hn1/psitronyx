#!/usr/bin/python3

from datetime import datetime

def printWriteFile(PATH_FILE, STRING, STDOUT):

	if STDOUT: print(STRING)

	with open(PATH_FILE, "+a") as file:
		file.write(f"{STRING}\n")
		file.close()

class LOG:

	def __init__(self, STDOUT):
		self.INFO 	= 0
		self.WARN 	= 1
		self.CRITIC = 2
		self.STDOUT = STDOUT
		self.logfile= "./logs/psitronyx.log"

	def __enter__(self): return self

	def __exit__(self, typeOf, value, traceback): return self

	def log(self, INFOLEVEL, STRING):
		LOG_MESSAGE_INFO = f"[Info] {STRING} | {datetime.now()}"
		LOG_MESSAGE_WARN = f"[Warning] {STRING} | {datetime.now()}"
		LOG_MESSAGE_CRIT = f"[Critical] {STRING} | {datetime.now()}"

		if ( INFOLEVEL == self.INFO ): printWriteFile(self.logfile, LOG_MESSAGE_INFO, self.STDOUT)
		elif ( INFOLEVEL == self.WARN ): printWriteFile(self.logfile, LOG_MESSAGE_WARN, self.STDOUT)
		elif ( INFOLEVEL == self.CRITIC ): printWriteFile(self.logfile, LOG_MESSAGE_CRIT, self.STDOUT)
