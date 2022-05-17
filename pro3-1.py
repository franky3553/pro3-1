import csv
import os

## def clearConsole

def clear_console():
   os.system('cls')

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))

global print1
global print2

race = True

auxiliarDeck = []
startingDeck = []
parkDeck = []
raceDeck = []
winDeck = []

## def non starting importExport functions

def importCSVinDeck(csvFile, deck):
   resetDeck(auxiliarDeck)
   copyCSVinAuxiliarDeck(csvFile)
   copyAuxiliarDeckinDeck(auxiliarDeck, deck)
   resetDeck(auxiliarDeck)
	
def exportDeckinCSV(deck, csvFile):
   resetDeck(auxiliarDeck)
   copyDeckinAuxiliarDeck(deck)
   copyAuxiliarDeckinCSV(auxiliarDeck, csvFile)
   resetDeck(auxiliarDeck)

## def functions inside non starting importExport functions

def resetDeck(deck):
   for capsule in range(len(deck)):
      del deck[0]
# capsule is a section of a deck composed of status line and statmentAnswer line

def copyCSVinAuxiliarDeck(csvFile):
   with open("{}.csv".format(csvFile)) as file:
      reader = csv.reader(file, delimiter=",")
      for row in reader:
            auxiliarDeck.append(row)

def copyAuxiliarDeckinDeck(auxiliarDeck, deck):
   CSVline = 0
   linesPerCapsule = 2
   totalLines = len(auxiliarDeck)
   totalCapsules = int(totalLines / linesPerCapsule)
   for capsule in range(totalCapsules):
      deck.append([])
      for linea in range(linesPerCapsule):
         deck[capsule].append(auxiliarDeck[CSVline])         
         CSVline += 1

def copyDeckinAuxiliarDeck(deck):
   linesPerCapsule = 2
   for capsule in range(len(deck)):
      for line in range(linesPerCapsule):
         auxiliarDeck.append(deck[capsule][line])

def copyAuxiliarDeckinCSV(auxiliarDeck, csvFile):
   with open("{}.csv".format(csvFile), "w", newline="") as file:
      writer = csv.writer(file, delimiter=",")
      writer.writerows(auxiliarDeck)

## def starting importExport functions

def importStartingCSVinStartingDeck(startingCSV, startingDeck):
   resetDeck(auxiliarDeck)
   copyStartingCSVinAuxiliarDeck(startingCSV)
   copyAuxiliarDeckinStartingDeck(auxiliarDeck, startingDeck)
   resetDeck(auxiliarDeck)
	
def exportStartingDeckinCSV(startingDeck, csvFile):
   resetDeck(auxiliarDeck)
   copyStartingDeckinAuxiliarDeck(startingDeck)
   copyAuxiliarDeckinCSV(auxiliarDeck, csvFile)
   resetDeck(auxiliarDeck)

## def functions inside starting importExport functions

def copyStartingCSVinAuxiliarDeck(startingCSV):
   with open("{}.csv".format(startingCSV)) as file:
      reader = csv.reader(file, delimiter=",")
      for row in reader:
            auxiliarDeck.append(row)

def copyAuxiliarDeckinStartingDeck(auxiliarDeck, startingDeck):
   element = 0
   for element in range(len(auxiliarDeck)):
      startingDeck.append(auxiliarDeck[element])
      element += 1

def copyStartingDeckinAuxiliarDeck(startingDeck):
   totalLines = len(startingDeck)
   for line in range(totalLines):
      auxiliarDeck.append([0, 0, 0])
      auxiliarDeck.append(startingDeck[line])


## def askCapsule

def askCapsule():
   previousFaultState = "noPriorFailure"
   askStatement(previousFaultState)

## def askStatement

def askStatement(previousFaultState):
   global print1
   print1 = item["statement"]
   print(item["statement"])
   askAnswer(previousFaultState)

## def askAnswer

def askAnswer(previousFaultState):
   global print2
   clear_console()
   print(print1)
   answerRequest = input(": ")
   clear_console()
   print2 = answerRequest
   print(print1 + ": " + print2)

   examAnswer = examRequestWithItem(answerRequest)
   examinationAction(examAnswer, previousFaultState)

## def examRequestWithItem

def examRequestWithItem(request):
   global print1
   clear_console()
   if request == "-reset":
      return "-reset"
   if request == "-exit":
      return "-exit"
   elif request == item["answer"]: 
      print1 += "\n:" + "\033[92m {}\033[00m" .format(print2)
      return "Correct"
   else:
      print(print1 + "\n:" + "\033[91m {}\033[00m" .format(print2))
      print(">", item["answer"])
      step = input()
      return "Incorrect"

## def examinationAction

def examinationAction(examAnswer, previousFaultState):
   if examAnswer == "-reset":
      resetPro3()
      print("Reset Complete")
   elif examAnswer == "-exit":
      global race 
      race = False
   elif examAnswer == "Incorrect":
      failedAnswerAction(previousFaultState)
   elif examAnswer == "Correct":
      successfulAnswerAction(previousFaultState)

## def failedAnswerAction

def failedAnswerAction(previousFaultState):
   if previousFaultState == "noPriorFailure":
      raceDeck[0][0][1] = decreaseTank()

      askAnswer("priorFailure")

   elif previousFaultState == "priorFailure":
      askAnswer("priorFailure")

## def successfulAnswerAction

def successfulAnswerAction(previousFaultState):

   if previousFaultState == "noPriorFailure": 
      raceDeck[0][0][1] = increaseTank() 

   print(print1)
   
   examCapsuleMovement()

   adjustFuel()

   sortDeck(raceDeck)
   
   examCapsuleMovement()

## def decreaseTank

def decreaseTank():
   tankSelection = int(raceDeck[0][0][1])
   if tankSelection < 2:
      tankOperation = 0
   else:
      tankOperation = tankSelection - 2
   return str(tankOperation)

## def increaseTank 

def increaseTank():
   tankOperation = int(raceDeck[0][0][1]) + 2
   return str(tankOperation)

## def adjustFuel

def adjustFuel():     
   raceDeck[0][0][0] = refuel()

   spendFuel()

## def functions inside adjustFuel function

def refuel():
   return str(raceDeck[0][0][1]) 

def spendFuel():
   for row in raceDeck:
      fuelSelection = int(row[0][0])
      if fuelSelection > 0:
         fuelSelection -= 1
         row[0][0] = str(fuelSelection)

## def sortDeck and selectionParameterOrder

def sortDeck(deck):
   deck.sort(key=selectionParameterOrder)
def selectionParameterOrder(parameterOrder):
  return parameterOrder[0][0][0]

## def examCapsuleMovement

def examCapsuleMovement():
   fuel = int(raceDeck[0][0][0])
   tank = int(raceDeck[0][0][1])

   if tank >= 12:

      extractFromDeckInsertToDeck(raceDeck, winDeck)

      resetWinCapsule()

      exportDeckinCSV(winDeck, "win")
      exportDeckinCSV(raceDeck, "race")
      prYellow("WWWWWIIIIIIIIIINNNNNNNNNNNNNNNNNNNNNNNN")
      step = input()

   if fuel >= 1:
   ## if elegirElemento("combustible")
      extractFromDeckInsertToDeck(parkDeck, raceDeck)

      exportDeckinCSV(parkDeck, "park")
      exportDeckinCSV(raceDeck, "race")
      prYellow("ONE MOOOOOREEEEEEE")
      step = input()

## def extractFromDeckInsertToDeck

def extractFromDeckInsertToDeck(extractionDeck, insertionDeck):
   insertionDeck.insert(0, extractCapsulefromDeck(extractionDeck, 0)) 
def extractCapsulefromDeck(deck, position):
   capsuleSave = deck[position]
   del deck[position]
   return capsuleSave

## def resetWinCapsule

def resetWinCapsule(): 
   winDeck[0][0][0] = 0
   winDeck[0][0][1] = 10
   winDeck[0][0][2] = 3

## def preparation

def preparation():
   extractFromDeckInsertToDeck(parkDeck, raceDeck)
# to extract first capsule from park and insert in race to initiate correctly

# def exirPreparation

def resetPro3():
   resetDeck(parkDeck)
   exportDeckinCSV(parkDeck, "park")
   resetDeck(raceDeck)
   exportDeckinCSV(raceDeck, "race")
   resetDeck(winDeck)
   exportDeckinCSV(winDeck, "win")


## importExport CSV and decks

importStartingCSVinStartingDeck("starting", startingDeck)
exportStartingDeckinCSV(startingDeck, "park")

importCSVinDeck("park", parkDeck)
importCSVinDeck("race", raceDeck)
importCSVinDeck("win", winDeck)

preparation()
exportDeckinCSV(parkDeck, "park")
exportDeckinCSV(raceDeck, "race")

## MAIN LOOP

while race:

   item = {
      "fuel": int(raceDeck[0][0][0]),
      "tank": int(raceDeck[0][0][1]),
      "statement": raceDeck[0][1][0],
      "answer": raceDeck[0][1][1],
   }

   print1 = ""
   print2 = ""

   askCapsule()

   exportDeckinCSV(parkDeck, "park")
   exportDeckinCSV(raceDeck, "race")
   exportDeckinCSV(winDeck, "win")
   
   if race == True:
      prYellow("CONTIIIINUE>>>>>>>>")
      step = input()
   else:
      pass

print("Exit Complete")
step=input()