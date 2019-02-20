#coding:utf8
import os
from PySide2.QtWidgets import *

class Hello(QWidget):
	def __init__(self):
		super(Hello, self).__init__()
		self.layout=QVBoxLayout()
		self.setLayout(self.layout)
		self.setEnv()

	def setEnv(self):
		string="hello nuke"
		self.layout.addWidget(QLabel("%s" % string))

def main():
	global customApp

	try:
		customApp.close()
	except:
		pass


	customApp=Hello()
	try:
		customApp.show()
	except:
		pass
