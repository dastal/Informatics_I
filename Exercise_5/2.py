import random
import math

#task 2a)
class Pokemon():

    def __init__(self, kind):
        self.__kind = kind
        self.__strength = random.randint(1, 255)
        self.__catch_rate = random.randint(1, 10)

    def get_kind(self):
        return self.__kind

    def get_strength(self):
        return self.__strength

    def get_catch_rate(self):
        return self.__catch_rate

    def __subtract(self, integer):
        return self.__strength - integer

    def attack(self, other_pkmn):
        self.__strength = Pokemon.__subtract(self, 1.1 * other_pkmn)
        return self.__strength


#task 2b)
class Trainer():

    def __init__(self, name):
        self.__name = name
        self.__pokemon = []

    def get_name(self):
        return self.__name

    def get_pokemon(self):
        return self.__pokemon

    def catch_pokemon(self):
        pokemon_type = 0
        while len(self.__pokemon) <= 6:
            pokemon = Pokemon(pokemon_type)
            random_integer = random.randint(1, 100)
            catch_rate = pokemon.get_catch_rate()
            if random_integer % catch_rate != 0:
                print("The wild pokemon fled.")
            else:
                if len(self.__pokemon) > 5:
                    print("The trainer has already 6 pokemon.")
                    break
                else:
                    print("The trainer successfully caught the pokemon.")
                    self.__pokemon.append(pokemon)
            pokemon_type += 1

    def print_pokemon_stats(self):
        for pokemon in self.__pokemon:
            Pokemon(pokemon)
            print("Pokemon No.:", self.__pokemon.index(pokemon) + 1 ,", kind:", pokemon.get_kind() ,"strength:", pokemon.get_strength())

    def release_pokemon(self, integer):
        if integer < len(self.__pokemon):
            self.__pokemon = self.__pokemon[1:]
            return self.__pokemon


#task 2c)
def fight(trainer1,trainer2):
    pokemons_trainer1 = trainer1.get_pokemon()
    pokemons_trainer2 = trainer2.get_pokemon()
    trainer1.print_pokemon_stats()
    trainer2.print_pokemon_stats()
    if pokemons_trainer1 == [] and pokemons_trainer2 == []:
        print("you cannot fight!")
        return
    elif pokemons_trainer1 == []:
        print("{0:s} has no pokemon left. {1:s} won!".format(trainer1.get_name(),trainer2.get_name()))
        return
    elif pokemons_trainer2 == []:
        print("{0:s} has no pokemon left. {1:s} won!.".format(trainer2.get_name(),trainer1.get_name()))
        return
    else:
        pokemon_trainer1 = pokemons_trainer1[0]
        pokemon_trainer2 = pokemons_trainer2[0]
        strength_1 = int(pokemon_trainer1.get_strength())
        strength_2 = int(pokemon_trainer2.get_strength())
        while strength_1 > 0 and strength_2 > 0:
            strength_2 = pokemon_trainer2.attack(strength_1)
            print(strength_2)
            if strength_2 > 0:
                strength_1 = pokemon_trainer1.attack(strength_2)
                print(strength_1)
            if strength_1 <= 0:
                trainer1.release_pokemon(0)
            if strength_2 <= 0:
                trainer2.release_pokemon(0)
        return fight(trainer1,trainer2)


trainer1 = Trainer("trainer1")
trainer2 = Trainer("trainer2")
trainer1.catch_pokemon()
trainer2.catch_pokemon()

fight(trainer1,trainer2)