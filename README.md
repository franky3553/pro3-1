# pro3-1

How to use pro3-1

Step A
	1. Download following files in folder named "pro3-1":
  	pro3-1.py
  	starting.csv
  	park.csv
  	race.csv
  	win.csv

Step B
	2. Open terminal
	3. Go to pro3.1 folder route
	4. Execute:
		python pro3-1.py

Step C
	5. Type the translation of the word that appears on the screen
	6. Pulse enter to examn your answer
	7. Pulse enter again to continue

ExtraStep
	8. type and enter the following to exit:
		-exit
		
		
		
How pro-3 works

First
	import, export and transforming csv and decks data formats
		1. read startingCSV
		2. extract data from starting.csv and insert in auxiliarDeck
		3. transform format in auxiliarDeck and insert in park.csv
		4. extract first capsule from park.csv and insert in race.csv
			to have a first to start from
			capsule is a section data composed by two lines
				first line contains fuel, tank and auxiliar value
					fuel value indicate your corresponding capsule level
					tank value indicate your capacity to achieve more level in corresponding capsule
					auxiliar value is reserved for future utilities (deep value, indicates if the capsule is out of your level)
				second line contains sentence and answer data
				example:
					2,4,0
					run, correr
	initiate while loop
		5. ask capsule
			request previous failure data
				you have to answer the first one correctly
			ask sentence
		6. ask sentence
			print sentence in console
			ask answer
		7. ask answer
			request answer
				get answer in a variable named answerRequest
		8. exam answer
			compare answerRequest value with actual capsule sentence value
				get actual capsule sentence using raceDeck[0][1][0]
			if they match, return "Correct", if not, return "Incorrect"
		9. examination action
			if its incorrect
				if it has no previously failed, decrease fuel value and ask answer again (start loop again from there) 
				if it has previously failed, ask answer again without decrease fuel value
					fuel value decrese once per exam
			if its correct, go to successfulAnswerAction
				if it has previously failed, increase fuel value
				if it has previously failed, continue without increase fuel value
					you have to answer the first one correctly
		10. and, if its correct:
			exam capsule movement
				capsules are arranged according to fuel
				if the fuel is increased, the order changes
			order capsules
			adjust fuel
				decrease in 1 all capsule fuel values
			exam capsule movement
				if after this the fuel value of any capsule is +12, the capsule go to win.csv
					this means that you have answered capsule correctly considerable times
					means you have reached the maximum level in that capsule
		11. All changes are updated by exporting from deck to csv files
		12. The loop start again
			
			
				
		
		
		
		
		
