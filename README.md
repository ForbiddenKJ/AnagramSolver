# AnagramSolver

## Files

A python program to solve anagrams

- `anagram.py` library

- `example.py` example code

- `dictionary_compact.json` english dictionary json file

### Auto

We only need to import Anagram from anagram.py
```python
from anagram import Anagram
```

Our json file will be dictionary_compact.json
```python
solutions = Solve('dictionary_compact.json', Anagram)
print(solutions)
```

### Manual

Load the library like this:
```python
from anagram import *
```

Next you need to load you json library of choice where the keys are words
We will use 'dictionary_compact.json' as our example
```python
dataHandler = jsonLoader('dictionary_compact.json')
dataHandler.load_data()
```

We then need to save the data into a list
```python
fullData = dataHandler.writeList
```

Now that all the json has been setup we can get to the
Heart of our operation
```python
x = Your Anagram
bruteHandler = wordBrute(x)
bruteHandler.brute()
bruteList = bruteHandler.writeList
```

And we have finished with the setup we can start completing things
```python
correctWord = bruteHandler.solve(fullData)
print(correctWord)
```
