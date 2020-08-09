argument = str(input("Geben Sie ein Wort beginnend mit a und Wortlänge < 20 ein: "))

def validate(word):
    if len(word) < 20 and word[0] == "a":
        return True
    else:
        return False

print(validate(argument))