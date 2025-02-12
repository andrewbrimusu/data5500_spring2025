'''
This program queries datamuse for words associated with a given word.
The associated words are given a score.
'''

import requests
import json

# example url to query datamuse web json api
example_url = "https://api.datamuse.com/words?ml=aggies"

req = requests.get(example_url)

print(req.text)

# data = req.json()
data = json.loads(req.text)

print(data)

word_key = "word"
score_key = "score"

for dct in data:
    print(dct)
    if dct[word_key] == "usu":
        print(dct[score_key])



# amazing code which will find the word score for aggies and usu
# go!














