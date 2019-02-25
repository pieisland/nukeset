#coding:utf8
from PySide2.QtWidgets import *
import os

class NkLibrary(QWidget):#위젯을 상속한다.
	def __init__(self):#클래스 생성 시 자동으로 호출되는 함수
		super(NkLibrary, self).__init__()#상속.
		
		#widget
		self.nklist=QListWidget()#리스트. 여러 개 있는 거 아닌가. 여기다 추가할 듯.
		#이전에는 콤보박스를 썼나본데, 콤보박는 눌러서 쭈르륵 나오는 거였나

		
		self.addNklist()
		self.ok=QPushButton("OK")#버튼 만드는 건 큐푸시버튼
		self.cancel=QPushButton("Cancel")#마찬가지
			
		#layout
		#레이아웃을 먼저 만든 후에, 위에서 만들었던 위젯들을 넣어주네.
		#만든 레이아웃에 위젯을 배치해주기. vertical로. 그래서 qv
		#위젯..흐으으음. 아가야 위젯들??
		layout=QVBoxLayout()
		layout.addWidget(self.nklist)
		layout.addWidget(self.ok)
		layout.addWidget(self.cancel)
		self.setLayout(layout)

	def addNklist(self):
		nkpath=os.getenv("NUKE_PATH")+"/tmp/nukeset/nk"
		if not os.path.exists(nkpath):
			nuke.message(nkpath +"경로가 존재하지 않습니다.")
			#return
		for i in os.listdir(nkpath):
			base, ext = os.path.splitext(i)
			if ext!=".nk":
				continue
			self.nklist.addItem(QListWidgetItem(i))
		

def main():
	global customApp
	try:
		customApp.close()
	except:
		pass

	customApp=NkLibrary()
	try:
		customApp.show()
	except:
		pass
