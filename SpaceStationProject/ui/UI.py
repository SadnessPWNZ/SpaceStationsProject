import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

import SpaceStationProject.src.api_request as rq
from SpaceStationProject.src import database_backend as db

from SpaceStationProject.ui.untitled import Ui_Form

NORAD = db.get_stations_and_norad()


class MyForm(Ui_Form, QMainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        # Get country list
        country_list = list(db.get_countries())

        # Assign Operator Combobox country list
        self.OperatorComboBox.addItems(country_list)

        # Get station list
        station_list = db.get_stations(str(self.OperatorComboBox.currentText()))
        str_station_list = map(str, station_list)
        self.StationComboBox.addItems(str_station_list)

        # Attaching funcs to buttons
        self.UpdateCoordinatesButton.clicked.connect(self.update_cords)
        self.OpenInGooglMaps.clicked.connect(self.open_map)
        self.VisualPasses.clicked.connect(self.passes)
        self.informationUpdateButton.clicked.connect(self.satellite_info)

        # Attaching func operator box changing event
        self.OperatorComboBox.currentTextChanged.connect(self.update_satellites)

    def update_cords(self) -> None:
        station = self.StationComboBox.currentText()

        latitude, longitude = rq.coordinates(NORAD[station], 37.953757, 58.336792, 129)

        print(f'Широта: {str(latitude)}\nДолгота: {str(longitude)}')
        print('---------------------------------------------------')

        self.latitudeLabel.setText(str(latitude))
        self.longitudeLabel.setText(str(longitude))

    def passes(self) -> None:
        station = self.StationComboBox.currentText()
        # Clear list from old data
        self.listWidget.clear()

        passes_list = rq.visual_passes(NORAD[station], 37.953757, 58.336792, 129, int(self.durationSpinBox.text()), 300)

        for i in range(len(passes_list)):
            self.listWidget.insertItem(i + 1, str(passes_list[i]))

        if passes_list[0] is None:
            # If None,than make text red
            self.listWidget.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            # Else text'll be green
            self.listWidget.setStyleSheet("color: rgb(0, 170, 0);")

    def open_map(self) -> None:
        rq.open_browser_map(self.latitude_label.text(), self.longitude_label.text())

    def update_satellites(self) -> None:
        station_list = db.get_stations(str(self.OperatorComboBox.currentText()))
        str_station_list = map(str, station_list)
        # print('combobox changed')
        self.StationComboBox.clear()
        self.StationComboBox.addItems(str_station_list)

    def satellite_info(self) -> None:
        # Clear old data
        self.informationText.clear()
        # Get and set new data
        info = db.get_station(self.StationComboBox.currentText())
        self.informationText.setText(str(info.info()))


app = QApplication(sys.argv)
ex = MyForm()
ex.show()
sys.exit(app.exec_())
