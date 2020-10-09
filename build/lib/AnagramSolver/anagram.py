import json
from threading import Thread as T_
from itertools import permutations
import concurrent.futures

class jsonLoader:
    def __init__(self, jsonFile:str):
        self.writeList = []
        self.allData = []
        self.jsonFile = jsonFile

    def load_data_threaded(self):
        with open(self.jsonFile) as jFile:
            data = json.load(jFile)

        jFile.close()

        for key, item in data.items():
            key = key.lower()
            self.writeList.append(key)

    def load_data(self):
        threadFunc = T_(target=self.load_data_threaded())
        threadFunc.start()
        threadFunc.join()

    def load_keys(self):
        with open(self.jsonFile) as jFile:
            data = json.load(jFile)

        jFile.close()

        for key, item in data.items():
            key = key.lower()
            self.allData.append([key,item])


def split(word:str):
    return [char for char in word]

class wordBrute:
    def __init__(self, letters:str):
        self.writeList = []
        self.letters = letters

    def brute(self):
        x = []

        self.writeList = [''.join(p) for p in permutations(self.letters)]

        newList = []

        for p in self.writeList:
            chars = split(p)
            while len(chars) > 1:
                newList.append("".join(chars))
                del chars[-1]

        self.writeList = newList

    def solve(self,jsonData:str):
        correctWord_ = list(set(jsonData) & set(self.writeList))
        return correctWord_

def Threaded_Solve(words:str, JsonFile:str):
    words = words.lower()
    dataHandler = jsonLoader(JsonFile)
    dataHandler.load_data()
    fullData = dataHandler.writeList
    bruteHandler = wordBrute(words)
    bruteHandler.brute()
    bruteList = bruteHandler.writeList
    solutions = sorted(bruteHandler.solve(fullData), key=len)

    return solutions

def Solve(words:str, JsonFile:str):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(Threaded_Solve, words, JsonFile)
        return_value = future.result()
        return return_value

# Example
if __name__ == '__main__':
    def speedTest():
        import time
        start_time = time.time()
        print(Solve('Anagrams', 'dictionary.json'))
        print("--- %s seconds ---" % (time.time() - start_time))

    speedTest()
