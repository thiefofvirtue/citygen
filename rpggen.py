#!/user/bin/python
# Version 0.1 of Vaporose's RPG Generator

import sys
from mainui import Ui_MainWindow
from cityGen import City
from PyQt4 import QtCore, QtGui

# Class for main application window


class Main(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.generateCity.clicked.connect(self.defineOutput)
        self.cityNameF.textChanged.connect(self.setCity)
        # self.cityTypeS.returnPressed.connect(self.setCity)

    def addCity(self, cityInput):
        self.city = cityInput

    def setCity(self):
        cityName = str(self.cityNameF.text())
        cityType = "Village"
        self.city.setValues(cityName, cityType)
        # str(self.cityTypeF.text())
        # Uncomment to test values: print cityName, cityType

    def defineOutput(self):
        cityOutput = self.city.displayCity()
        qCityOutput = QtCore.QString(cityOutput)
        self.city.runCalc()
        self.cityOutput.append(qCityOutput)


def main():
    app = QtGui.QApplication(sys.argv)
    city1 = City()
    city1.setValues()
    city1.runCalc()
    form = Main()
    form.show()
    form.addCity(city1)
    form.setCity()
    app.exec_()


if __name__ == '__main__':
    main()
