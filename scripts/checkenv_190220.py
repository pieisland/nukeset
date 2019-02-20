#coding:utf8
import os
from PySide2.QtWidgets import *

class CheckEnv(QWidget):
	layout = QVBoxLayout()
	def __init__(self):
		super(CheckEnv, self).__init__()
		self.setLayout(self.layout)#QtWidgets의 method. layout setting.
		self.setEnv()
	
	def setEnv(self):
		envs=["USER", "OCIO", "NUKE_PATH", "NUKE_FONT_PATH"]
		for e in envs:
			self.layout.addWidget(QLabel("$%s : %s" % (e, os.environ.get(e, ""))))

def main():
	global customApp #global로 안하면 안만들어짐..?
	
	#이미 띄어진 창이 있으면 닫음
	try:
		customApp.close()
	except:
		pass

	#새로운 창을 만듦
	customApp=CheckEnv()
	try:
		customApp.show()
	except:
		pass

