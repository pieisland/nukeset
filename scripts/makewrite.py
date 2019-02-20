#coding:utf8
import nuke

def main():
	tail = nuke.selectedNode()
	w = nuke.nodes.Write()
	w.setInput(0, tail)
