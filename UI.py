import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from untitled import Ui_Form
from norad_id import NORAD
import api_request as rq



class MyForm(Ui_Form, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.UpdateButton.clicked.connect(self.update_cords)

        self.OpenInGooglMaps.clicked.connect(rq.open_browser_map)

    def update_cords(self):
        station = self.comboBox.currentText()
        norad = NORAD[station]

        print(f'Station: {station}\nNORAD id: {norad}')

        latitude, longitude = rq.coordinates(norad)

        print(f'Широта: {str(latitude)}\nДолгота: {str(longitude)}')

        self.latitude_label.setText(str(latitude))
        self.longitude_label.setText(str(longitude))


app = QApplication(sys.argv)
ex = MyForm()
ex.show()
sys.exit(app.exec_())
