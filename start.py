from PyQt5.QtWidgets import QApplication
import sys
from ui.UI import MyForm

app = QApplication(sys.argv)
ex = MyForm()
ex.show()
sys.exit(app.exec_())
