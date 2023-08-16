from datetime import datetime

import matplotlib.pyplot as plt
import numpy as np

from moistureReadings import moisture_levels1, moisture_levels2, moisture_levels3

"""
OPDRACHT:

Je buurman heeft geen groene vingers maar houdt ontzettend van mooie tuinen. Zijn planten gaan altijd dood omdat hij
niet weet hoeveel en wanneer hij de planten water moet geven. Daarom heeft hij besloten om een systeem aan te
schaffen die de vochtlevels in zijn tuin meten zodat hij beter weet waar en hoeveel hij water met geven aan de tuin.
het probleem is dat dit systeem alleen nummers geeft en de buurman snapt niet goed wat hij hiermee aan moet.
omdat jij een goede buur bent help jij de buurman.

je krijgt de waarde van de metingen al deze heten moisture_levels1,moisture_levels2, moisture_levels3
en staan in het andere python bestand, NIET SPIEKEN.

TIP je zou de volgende functies van numpy en mathplotlib handig kunnen vinden.

- plt.imshow
- plt.colorbar
- plt.title
- plt.grid
- plt.xlim
- plt.ylim
- plt.show
- plt.scatter

TAAK 1 maak de metingen visueel met een functie makGraph.
TAAK 2 haal de locatie van de droge plekken op en print deze met een functie get_locations.
BONUS taak 3 zet cirkels op de kaart om de droge plekken.
Bonus TAAK 4 maak een klasse van moisture reading met de variabele reading, date.
en de functies makegraph en getlocation DEZE IS ALLEEN TE MAKEN ALS DE GROEP AL KLASSE HEEFT GEHAD!!

Stappenplan:
1. Importeer de nodige modules, in dit geval matplotlib.pyplot en numpy

"""


class MoistureReading:
    def __init__(self, reading, date):
        self.reading = reading
        self.date = date
        self.locations = self.get_locations()

    def makeGraph(self):
        plt.imshow(self.reading, cmap='viridis')
        plt.colorbar()
        plt.title(f'Moisture Levels in the Garden ({self.date})', fontweight="bold")
        plt.grid(color='black', linestyle='--', linewidth=0.5)
        plt.xlim(0, 20)
        plt.ylim(0, 20)
        for loc in self.locations:
            plt.scatter(loc[1], loc[0], s=400, facecolors='none', edgecolors='r')
        plt.show()

    def get_locations(self):
        locations = np.argwhere(self.reading < 10)
        return np.array(locations)


reading1 = MoistureReading(moisture_levels1, datetime(2023, 1, 1))
reading2 = MoistureReading(moisture_levels2, datetime(2023, 1, 2))
reading3 = MoistureReading(moisture_levels3, datetime(2023, 1, 3))

reading1.makeGraph()
print(reading1.locations)

reading2.makeGraph()
print(reading2.locations)

reading3.makeGraph()
print(reading3.locations)