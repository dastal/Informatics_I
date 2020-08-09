user_1 = str(input("Player 1: rock, paper, scissors? "))
if (user_1 == "rock") or (user_1 == "paper") or (user_1 == "scissors"):
    print("Accepted")
else:
    print("Error")
user_2 = str(input("Player 2: rock, paper, scissors? "))
if (user_2 == "rock") or (user_2 == "paper") or (user_2 == "scissors"):
    print("Accepted")
else:
    print("Error")


if ((user_1 == "rock") and (user_2 == "rock")) or ((user_1 == "paper") and (user_2 == "paper")) or ((user_1 == "scissors") and (user_2 == "sicssors")):
    print("It's a tie. Play again!")
elif (user_1 == "rock") and (user_2 == "scissors"):
    print("Player 1 wins!")
elif (user_1 == "scissors") and (user_2 == "paper"):
    print("Player 1 wins!")
elif (user_1 == "paper") and (user_2 == "rock"):
    print("Player 1 wins!")
else:
    print("Player 2 wins!")