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

## def functions inside non starting importExport functions

def resetDeck(deck):
   for capsule in range(len(deck)):
      del deck[0]
# capsule is a section of a deck composed of status line and statmentAnswer line

def copyCSVinAuxiliarDeck(csv, auxiliarDeck):
   with open("{}.csv".format(csv)) as file:
      reader = csv.reader(file, delimiter=",")
      for row in reader:
            auxiliarDeck.append(row)

def copyAuxiliarDeckinDeck(auxiliarDeck, deck):
   CSVline = 0
   linesPerCapsule = 2
   totalLines = len(csv)
   totalCapsules = int(totalLines / linesPerCapsule)
   for capsule in range(totalCapsules):
      deck.append([])
      for linea in range(linesPerCapsule):
         deck[capsule].append(auxiliarDeck[CSVline])         
         CSVline += 1

def copyDeckinAuxiliarDeck(deck, auxiliarDeck):
   linesPerCapsule = 2
   for capsule in range(len(deck)):
      for line in range(linesPerCapsule):
         auxiliarDeck.append(deck[capsule][line])

def copyAuxiliarDeckinCSV(auxiliarDeck, csv):
   with open("{}.csv".format(csv), "w", newline="") as file:
      writer = csv.writer(file, delimiter=",")
      writer.writerows(auxiliarDeck)
      