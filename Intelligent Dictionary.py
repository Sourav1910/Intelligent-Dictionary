import json
from difflib import get_close_matches as gcm

with open('data.json') as file:  
    data = json.load(file)
x=(input("Enter the word:")).lower()

if x in data:
    print(data[x])
elif len(gcm(x,data.keys()))>0:
    yn=input("Did you mean %s instead? Enter Y if yes , N if no: " %gcm(x,data.keys())[0])
    if yn=='Y':
        print(data[gcm(x,data.keys())[0]])
    elif yn=='N':
        print("Sorry.This word does not exist.")
    else:
        print("We didnt understand your entry.")
else:
    print("Sorry.This word does not exist.")
