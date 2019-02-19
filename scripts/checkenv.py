#coding:utf8
import os
import nuke
from PySide2.QtWidgets import *

"""
class CheckEnv(QWidget):
	def __init__(self):
		super(CheckEnv, self).__init__()
		qmBox = QMessageBox(None)
		qmBox.setText("$USER : %s" % (os.environ['USER']))
		qmBox.show()
"""

def main():
	result=[]
	envs=["OCIO", "NUKE_PATH", "NUKE_FONT_PATH", "USER"]
	
	for env in envs:
		result.append("$%s : %s"%(env, os.environ[env]))
	nuke.message("\n".join(result))
