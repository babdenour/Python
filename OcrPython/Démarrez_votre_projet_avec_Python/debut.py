quote = "Ecoutez-moi, Monsieur Shakespeare: Nous avons beau être ou ne pas être, nous sommes !"

my_dic = {"paris": "75000", "melun": "77000", "dll": "77190"}
prog = {"quote": ["A la place de quote"], "character": ["Alvin", "Mulan", "Tony Hawk", "Luffy Mugiwaraya"]}

print(quote)
print(my_dic["paris"])
print(prog["quote"])
print(prog["character"])


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
