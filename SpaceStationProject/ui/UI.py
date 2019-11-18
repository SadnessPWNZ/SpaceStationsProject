import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from ui.untitled import Ui_Form
import src.api_request as rq
from src.norad_id import NORAD


class MyForm(Ui_Form, QMainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.update_cords()

        self.UpdateButton.clicked.connect(self.update_cords)

        self.OpenInGooglMaps.clicked.connect(self.open_map)

        self.VisualPasses.clicked.connect(self.passes)

    def update_cords(self):
        station = self.comboBox.currentText()
        norad = NORAD[station]

        latitude, longitude = rq.coordinates(norad)

        print(f'Широта: {str(latitude)}\nДолгота: {str(longitude)}')

        self.latitude_label.setText(str(latitude))
        self.longitude_label.setText(str(longitude))

    def passes(self):
        passes_list = rq.visual_passes(25544, 37.953757, 58.336792, 129, 10, 300)
        for i in range(len(passes_list)):
            self.listWidget.insertItem(i + 1, str(passes_list[i]))

    def open_map(self):
        rq.open_browser_map(self.latitude_label.text(), self.longitude_label.text())


app = QApplication(sys.argv)
ex = MyForm()
ex.show()
sys.exit(app.exec_())
