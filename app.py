import json
from difflib import get_close_matches

data = json.load(open('data.json'))


def get_definition(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        ans = input("Did you mean {} instead? Enter Y for yes, or N for No: ".format(
            get_close_matches(word, data.keys())[0]))
        if ans.upper() == 'Y':
            return data[get_close_matches(word, data.keys())[0]]
        elif ans.upper() == 'N':
            return "We don't seem to have a definition for that word. Try another"
        else:
            return "Sorry we don't understand that input"
    else:
        return "We don't seem to have a definition for that word. Try another"


word = input('Enter word__')
print(get_definition(word))
