import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(x):
    x = x.lower()
    if x in data:
        return data[x]
    elif x.title() in data:
        return data[x.title()]
    elif x.upper() in data:
        return data[x.upper()]
    elif len(get_close_matches(x, data.keys())) > 0:
        yn = input("Did you mean to %s instead? (Y/N)?" % get_close_matches(x, data.keys())[0])
        if yn.lower() == "y":
            return data[get_close_matches(x, data.keys())[0]]
        elif yn.lower() == "n":
            return "The word doesn't exist. Please double check your spelling :)"
        else:
            return "We didn't understand your response, sorry!"
    else:
        return "The word doesn't exist. Please double check your spelling :)"

word = input("Enter word and receive definition: ")

final = translate(word)

if type(final) == list:
    for i in final:
        print(i)
else:
    print(final)




