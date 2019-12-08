import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

import SpaceStationProject.src.api_request as rq
from SpaceStationProject.src import database_backend as db

from SpaceStationProject.ui.untitled import Ui_Form

from SpaceStationProject.cfg import coordinates

NORAD = db.get_stations_and_norad()

LATITUDE, LONGITUDE, ALTITUDE, = coordinates['LAT'], coordinates['LNG'], coordinates['ALT']


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
        self.VisualPassesButton.clicked.connect(self.passes)
        self.informationUpdateButton.clicked.connect(self.satellite_info)

        # Attaching func to box changing event
        self.OperatorComboBox.currentTextChanged.connect(self.update_satellites)

        # Updating coordinates on startup
        self.update_cords()

    def update_cords(self) -> None:
        station = self.StationComboBox.currentText()

        latitude, longitude = rq.coordinates(NORAD[station], LATITUDE, LONGITUDE, ALTITUDE)

        print(f'Широта: {str(latitude)}\nДолгота: {str(longitude)}')
        print('---------------------------------------------------')

        self.latitudeLabel.setText(str(latitude))
        self.longitudeLabel.setText(str(longitude))

    def passes(self) -> None:
        station = self.StationComboBox.currentText()
        # Clear list from old data
        self.VisaulPasseslistWidget.clear()

        passes_list = rq.visual_passes(NORAD[station], LATITUDE, LONGITUDE, ALTITUDE, int(self.durationSpinBox.text()),
                                       10)

        for i in range(len(passes_list)):
            self.VisaulPasseslistWidget.insertItem(i + 1, str(passes_list[i]))

        if passes_list[0] is None:
            # If None,than make text red
            self.VisaulPasseslistWidget.setStyleSheet("color: rgb(255, 0, 0);")
            self.VisualPassesTotal.setText(f'Either no any passes or External error')
            self.VisualPassesTotal.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            # Else text'll be green
            # Also there is update of Total Passes label
            self.VisaulPasseslistWidget.setStyleSheet("color: rgb(0, 170, 0);")
            self.VisualPassesTotal.setStyleSheet("color: rgb(0, 170, 0);")
            self.VisualPassesTotal.setText(f'Total Passes: {len(passes_list)}')

    def open_map(self) -> None:
        rq.open_browser_map(self.latitudeLabel.text(), self.longitudeLabel.text())

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
