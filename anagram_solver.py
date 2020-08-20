from ws import *

fullData = []

dataHandler = jsonLoader(fullData, 'dictionary_compact.json')
dataHandler.load_data()

rLetters = input("Anagram > ")
bruteList = []; bruteHandler = wordBrute(bruteList, rLetters);
bruteHandler.brute()
correctWord = bruteHandler.solve(fullData)

correctWord = sorted(correctWord, key=len)

for i in correctWord:
    if len(i) > 2:
        print(i+': '+str(len(i)))
