<div align="center">

![imagen](https://user-images.githubusercontent.com/45402163/168968927-27e58363-18df-4cf9-861a-40bb9dde3ef0.png)

</div>

# How to use pro3-1

## Step A
### 1. Download following files in previously created folder named "pro3-1":
  	pro3-1.py
  	starting.csv
  	park.csv
  	race.csv
  	win.csv

## Step B
### 2. Open terminal
### 3. Go to pro3.1 folder route
### 4. Execute:
	python pro3-1.py

## Step C
### 5. Type the translation of the word that appears on the screen
### 6. Pulse enter to examn your answer
### 7. Pulse enter again to continue

## ExtraStep
### 8. Type and enter the following to exit:
	-exit
### 9. Type and enter the following to reset all data:
	-reset
		
		
		
# How pro-3 works

## STEP A: Import, export and transforming csv and decks data formats
### 1. Read startingCSV
### 2. Extract data from starting.csv and insert in auxiliarDeck
### 3. Transform format in auxiliarDeck and insert in park.csv
### 4. Extract first capsule from park.csv and insert in race.csv
- To have a first to start from
- Capsule is a section data composed by two lines
- First line contains fuel, tank and auxiliar value. Fuel value indicate your corresponding capsule level. Tank value indicate your capacity to achieve more level in corresponding capsule. Auxiliar value is reserved for future utilities (deep value, indicates if the capsule is out of your level)
- Second line contains sentence and answer data
- Capsule example:
	````
	2,4,0
	run, correr
	````
## STEP B: Initiate while loop
### 5. Ask capsule
- Request previous failure data (You have to answer the first one correctly)
### 6. Ask sentence
- Print sentence in console
### 7. Ask answer
- Request answer (Get answer in a variable named answerRequest)
### 8. Exam answer
- Compare answerRequest value with actual capsule sentence value
- If they match, return "Correct", if not, return "Incorrect"
### 9. Examination action
- If its incorrect and if it has no previously failed, decrease fuel value and ask answer again (start loop again from there) 
- If its incorrect and if it has previously failed, ask answer again without decrease fuel value (Fuel value decrese once per exam)
	
### 10. But, if its correct: Go to successfulAnswerAction
- If it has previously failed, increase fuel value
- If it has previously failed, continue without increase fuel value (You have to answer the first one correctly)
### 11. Exam capsule movement
- Capsules are arranged according to fuel
- If the fuel is increased, the order changes
### 12. Order capsules
### 13. Adjust fuel
- Decrease in 1 all capsule fuel values
### 14. Exam capsule movement
- If after this the fuel value of any capsule is +12, the capsule go to win.csv
- This means that you have answered capsule correctly considerable times
- Means you have reached the maximum level in that capsule
### 15. Update all changes by exporting from deck to csv files
### 16. The loop start again
		
		
				
		
		
		
		
		
