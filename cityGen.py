#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import seed, getrandbits, choice, randrange

# Initializes random generator
randomStart = getrandbits(100)
seed(randomStart)

# Start defines for City class


class City:
    'Class for the city. This will be called later to define individual cities'
    cityCount = 0

    def __init__(self):
        self.cityCount += 1

# Sets Name and Size Type selection

    def setValues(self, name="None", size="None"):
        self.name = name
        self.size = size
        if name == "None":
            self.name = "Random"
        if size == "None":
            self.size = "Random"

# Randomizes city population and area based on city Size Type (self.size).

    def cityPopulation(self):
        cityTypes = ['Thorp',
                     'Hamlet',
                     'Village',
                     'Small Town',
                     'Large Town',
                     'Small City',
                     'Large City',
                     'Metropolis'
                     ]

        if self.size == "Random":
            self.size = (choice(cityTypes))

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

# Calculates the population density.

    def calcPopulation(self):
        self.popDensity = self.cityPop / self.cityArea
        if self.popDensity < 1:
            self.popDensity = 1

# Calculates a percentage of self.cityPop that are children
# Children are unable to work and are dependent upon adults

    def calcChildren(self):
        # Randomly generates a percentage of the city that are children
        self.childPercent = (round((randrange(0, 50) / 100.0), 2))
        self.childPop = self.cityPop * self.childPercent

    def runCalc(self):
        self.setValues()
        self.cityPopulation()
        self.calcPopulation()
        self.calcChildren()

# Prints all previously defined variables.

    def displayCity(self):
        tOverview = "Name: " + self.name + " City Size: " + self.size
        tPop = "\nTotal population (including children): " + str(self.cityPop)
        tKidsPop = "\nTotal children: " + str(round(self.childPop, 0))
        tKidsPer = " (" + str(self.childPercent) + "%)"
        tArea = "\nTotal city area: " + str(self.cityArea)
        tDense = "\nPopulation density: "+str(round(self.popDensity, 0))+"\n"
        outString = str(tOverview)+str(tPop)+str(tArea)+str(tDense)+str(tKidsPop)+str(tKidsPer)
        return outString
        # print str(outString) # Uncomment to test functional changes

# Uncomment
# city1 = City()
# city1.runCalc()
# city1.displayCity()


