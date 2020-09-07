import json
from threading import Thread as T_
from itertools import permutations
import gc
import multiprocessing

class jsonLoader:
    def __init__(self, jsonFile):
        self.writeList = []
        self.jsonFile = jsonFile

    def load_data_threaded(self):
        with open(self.jsonFile) as jFile:
            data = json.load(jFile)
            gc.collect()

        jFile.close()

        for key, item in data.items():
            self.writeList.append(key)

    def load_data(self):
        threadFunc = T_(target=self.load_data_threaded())
        threadFunc.start()
        threadFunc.join()

def split(word):
    return [char for char in word]
    gc.collect()

def returnPerm(x):
    return x

class wordBrute:
    def __init__(self, letters):
        self.writeList = []
        self.letters = letters

    def brute(self):
        x = []

        with multiprocessing.Pool() as pool:
            results = pool.map(returnPerm, permutations(self.letters))

        perms = results

        for p in perms:
            self.writeList.append(''.join(p))

        newList = []

        for p in self.writeList:
            gc.collect()
            chars = split(p)

            while len(chars) > 1:

                newList.append("".join(chars))
                del chars[-1]

        newList = list(newList)

        for i in newList:
            self.writeList.append(i)

        del newList

    def solve(self,jsonData):
        correctWord_ = list(set(jsonData) & set(self.writeList))

        return correctWord_

class Anagram:
    def Solve(JsonFile, words):
        dataHandler = jsonLoader(JsonFile)
        dataHandler.load_data()
        fullData = dataHandler.writeList
        bruteHandler = wordBrute(words)
        bruteHandler.brute()
        bruteList = bruteHandler.writeList
        solutions = bruteHandler.solve(fullData)
        solutions = sorted(solutions, key=len)

        return solutions

# Example
if __name__ == '__main__':
    print(Anagram.Solve('dictionary_compact.json', 'Anagram'))
