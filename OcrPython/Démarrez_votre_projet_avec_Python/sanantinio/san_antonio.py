#conding: utf-8
import random
import json
quotes = [
        "Ecoutez-moi, Monsieur Shakespeare: Nous avons beau être ou ne pas être, nous sommes !",
        "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
        ]
characters = [
        "alvin et les Chipmunks",
        "Babar",
        "betty boop",
        "calimero",
        "casper",
        "le chat potté",
        "Kirikou"
        ]
#read value from json file
def read_value_from_json():
    values = []
    #open file json with my object
    with open('characters.json') as f:
        #load all the data contain in my file. data = entries
        data = json.load(f)
    for entry in data:
        values.append(entry['character'])
    return values

def get_random_item(my_list):
    r = random.randint(0, len(my_list) - 1)
    item = my_list[r]
    return item

def get_random_character():
    all_values = read_value_from_json()
    return get_random_item(all_values)

def capitalize(words):
    for word in words:
        word.capitalize()

def message(character, quote):
    capitalize(character)
    capitalize(quote)
    message = "{} a dit {}".format(character, quote)
    return message

#Program!!!
user_answer = input("Tapez entrer pour connaitre une autre citaion ou B pour quitterle programme.")
while user_answer != "B":
    print(message(get_random_item(characters), get_random_character()))
    user_answer = input("Tapez entrer pour connaitre une autre citaion ou B pour quitterle programme.")
