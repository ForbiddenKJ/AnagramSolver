# AnagramSolver

## Files

A python program to solve anagrams

- `anagram.py` library

- You will need a dictionary filled with words as keys we recommend https://github.com/matthewreagan/WebstersEnglishDictionary (dictionary_compact.json)

### Example

We only need to import Anagram from anagram.py
```python
from AnagramSolver.anagram import Solve
```

Our json file will be dictionary_compact.json
```python
solutions = Solve(Anagram, 'dictionary_compact.json')
print(solutions)
```
