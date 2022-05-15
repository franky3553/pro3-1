import csv

auxiliarDeck = []
startingDeck = []
parkDeck = []
raceDeck = []
winDeck = []

## def non starting importExport functions

def importCSVinDeck(csv, deck):
   resetDeck(auxiliarDeck)
   copyCSVinAuxiliarDeck(csv, auxiliarDeck)
   copyAuxiliarDeckinDeck(auxiliarDeck, deck)
   resetDeck(auxiliarDeck)
	
def exportDeckinCSV(csv, deck):
   resetDeck(auxiliarDeck)
   copyDeckinAuxiliarDeck(deck, auxiliarDeck)
   copyAuxiliarDeckinCSV(auxiliarDeck, csv)
   resetDeck(auxiliarDeck)