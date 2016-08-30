#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import random
import cityui
from random import randrange
from PyQt4 import QtCore, QtGui
from PyQt4.Qt import QTextEdit, QString, QLineEdit
from libxml2mod import parent
from blivet import size

# Start defines for City class


class City:
    'Class for the city. This will be called later to define individual cities'
    cityCount = 0

    def __init__(self):
        self.cityCount += 1

    def setValues(self, name="None", size="None"):
        self.name = name
        self.size = size
        if size == "None":
            self.randomSize()
        if name == "None":
            name = "Random"

    def randomSize(self):
        sizeChoice = ['Thorp',
                      'Hamlet',
                      'Village',
                      'Small Town',
                      'Large Town',
                      'Small City',
                      'Large City',
                      'Metropolis'
                      ]
        self.size = random.choice(sizeChoice)

    def cityPopulation(self):
        cityPopRange = {'Thorp': (1, 20),
                        'Hamlet': (21, 60),
                        'Village': (61, 200),
                        'Small Town': (201, 2000),
                        'Large Town': (2001, 5000),
                        'Small City': (5001, 10000),
                        'Large City': (10001, 25000),
                        'Metropolis': (25000, 50000)
                        }
        cityAreaRange = {'Thorp': (1, 20),
                         'Hamlet': (1, 40),
                         'Village': (5, 60),
                         'Small Town': (100, 1000),
                         'Large Town': (200, 2000),
                         'Small City': (30, 80),
                         'Large City': (80, 200),
                         'Metropolis': (12000, 20000)
                         }
        self.cityPop = (
                        randrange(cityPopRange[self.size][0],
                                  cityPopRange[self.size][1])
                        )
        self.cityArea = (
                        randrange(cityAreaRange[self.size][0],
                                  cityAreaRange[self.size][1])
                        )

    def calcPopulation(self):
        self.popDensity = self.cityPop / self.cityArea
        if self.popDensity < 1:
            self.popDensity = 1

    def calcChildren(self):
        # Randomly generates a percentage of the city that are children
        self.childPercent = (round((randrange(0, 50) / 100.0), 2))
        self.childPop = self.cityPop * self.childPercent

    def displayCity(self):
        tOverview = "Name: " + self.name + " City Size: " + self.size
        tPop = "\nTotal population (including children): " + str(self.cityPop)
        tKidsPop = "\nTotal children: " + str(round(self.childPop, 0))
        tKidsPer = " (" + str(self.childPercent) + "%)"
        tArea = "\nTotal city area: " + str(self.cityArea)
        tDense = "\nPopulation density: "+str(round(self.popDensity, 0))+"\n"
        outString = str(tOverview)+str(tPop)+str(tArea)+str(tDense)+str(tKidsPop)+str(tKidsPer)
        return outString


class Main(QtGui.QMainWindow, cityui.Ui_MainWindow):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.generateCity.clicked.connect(self.defineOutput)
        self.cityNameF.returnPressed.connect(self.setCity)
        self.cityTypeF.returnPressed.connect(self.setCity)

    def addCity(self, cityInput):
        self.city = cityInput

    def setCity(self):
        cityType = str(self.cityTypeF.text())
        cityName = str(self.cityNameF.text())
        # Uncomment to test values: print cityName, cityType
        self.city.setValues(cityName, cityType)

    def defineOutput(self):
        cityOutput = self.city.displayCity()
        qCityOutput = QtCore.QString(cityOutput)
        self.cityOutput.append(qCityOutput)


def main():
    app = QtGui.QApplication(sys.argv)
    city1 = City()
    city1.setValues()
    city1.cityPopulation()
    city1.calcPopulation()
    city1.calcChildren()
    form = Main()
    form.addCity(city1)
    form.setCity()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()

