import random

prefix = str(input("Moechten Sie, dass die Nummer mit einer Vorwahl geschrieben wird? (Ja/Nein) "))
country_code = "+41"

def random_number(country_code, prefix_number):
    x = str(random.randint(1000000, 9999999))
    anbieter = str("07") + str(random.randint(6, 9))
    if prefix_number == "Ja" or "ja" or "JA":
        return country_code + anbieter[1:] + x
    else:
        return anbieter + x

print(random_number(country_code, prefix))