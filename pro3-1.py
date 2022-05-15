import csv

## def clearConsole

def clear_console():
    os.system('cls')

global print1
global print2

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

## def starting importExport functions

def importStartingCSVinStartingDeck(startingCSV, startingDeck):
   resetDeck(auxiliarDeck)
   copyStartingCSVinAuxiliarDeck(startingCSV, auxiliarDeck)
   copyAuxiliarDeckinStartingDeck(auxiliarDeck, startingDeck)
   resetDeck(auxiliarDeck)
	
def exportStartingDeckinParkCSV(startingDeck, csv):
   resetDeck(auxiliarDeck)
   copyStartingDeckinAuxiliarDeck(startingDeck, auxiliarDeck)
   copyAuxiliarDeckinCSV(auxiliarDeck, csv)
   resetDeck(auxiliarDeck)

## def functions inside starting importExport functions

def copyStartingCSVinAuxiliarDeck(startingCSV, auxiliarDeck):
   with open("{}.csv".format(startingCSV)) as file:
      reader = csv.reader(file, delimiter=",")
      for row in reader:
            auxiliarDeck.append(row)

def copyAuxiliarDeckinStartingDeck(auxiliarDeck, startingDeck):
   element = 0
   for element in range(len(auxiliarDeck)):
      startingDeck.append(auxiliarDeck[element])
      element += 1

def copyStartingDeckinAuxiliarDeck(startingDeck, auxiliarDeck):
   totalLines = len(startingDeck)
   for line in range(totalLines):
      auxiliarDeck.append([0, 0, 0])
      auxiliarDeck.append(startingDeck[line])


## def askCapsule

def askCapsule():
   previousFaultState = "NoPriorFailure"
   askStatement(previousFaultState)

## def askStatement

def askStatement(previousFaultState):
   global print1
   print1 = chooseItem("statement")
   print(chooseItem("statement"))
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
   if request == chooseItem("answer"): 
      print1 += "\n:" + "\033[92m {}\033[00m" .format(print2)
      return "Correct"
   else:
      print(print1 + "\n:" + "\033[91m {}\033[00m" .format(print2))
      print(">", chooseItem("answer"))
      step = input()
      return "Incorrect"

## def examinationAction

def examinationAction(examAnswer, previousFaultState):
   if examAnswer == "Incorrect":
      failedAnswerAction(previousFaultState)
   elif examAnswer == "Correct":
      successfulAnswerAction(previousFaultState)

## def chooseItem
def chooseItem(item):
   if item == "capsule":
      capsule = raceDeck[0]
      return capsule
   elif item == "fuel":
      fuel = int(raceDeck[0][0][0])
      return fuel
   elif item == "tank":
      tank = int(raceDeck[0][0][1])
      return tank
   elif item == "statement":
      statement = raceDeck[0][1][0]
      return statement 
   elif item == "answer":
      answer = raceDeck[0][1][1]
      return answer
      