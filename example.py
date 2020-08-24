from ws import *

# Setting up json
dataHandler = jsonLoader('dictionary_compact.json') # Json file

dataHandler.load_data() # Loads json file

<<<<<<< HEAD
fullData = dataHandler.writeList # Load list into a variable
=======
fullData = dataHandler.writeList # Loads the file into a list
>>>>>>> master

rLetters = input("Anagram > ")

bruteHandler = wordBrute(rLetters)

bruteHandler.brute() # Brute forcing all possible cominations

bruteList = bruteHandler.writeList # Load list into a variable

correctWord = bruteHandler.solve(fullData) # Comparing compinations to the json file keys

correctWord = sorted(correctWord, key=len) # Sorts the list into length of order

for i in correctWord:
    if len(i) > 2:
        print(i+': '+str(len(i)))
