import nuke
import os
import nukescripts

def main():
	node = nuke.selectedNode()
	path = node["file"].value()
	os.system("nautilus %s" % os.path.dirname(path))
