# event
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyApp (QWidget):
	def __init__(self):
		super().__init__()
		self.initUi()

	def initUi(self):
		self.setWindowTitle("PyQt Button Test")
		self.move(300, 300)
		self.resize(400, 200)

		btn = QPushButton("Click", self)
		btn.move(20, 20)
  		# 이벤트 핸들러를 connect로 연결
		btn.clicked.connect(self.btn_clicked)

	def btn_clicked(self):
		QMessageBox.about(self, "message", "clicked")

if __name__ == "__main__":
	app = QApplication(sys.argv)
	ex = MyApp()
	ex.show()
	sys.exit(app.exec_())
