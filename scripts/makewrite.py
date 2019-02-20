#coding:utf8
import nuke

def main():
	if len(nuke.selectedNodes()) != 1:
		nuke.message("노드를 하나만 선택해주세요.")
		return
	tail = nuke.selectedNode()
	w = nuke.nodes.Write()
	w.setInput(0, tail)
