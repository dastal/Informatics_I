secret_word = str(input("Player 1 enter the secret word: "))


def hangman(secret_word, num_guesses):
    print("The secret word has", len(secret_word) ,"characters.")
    guessed_word = len(secret_word) * ["_ "]
    print(''.join(guessed_word))
    guess_store = []
    while num_guesses > 0:
        guess = str(input("Player 2 enter your guess (Please only enter letters of the Greek alphabet): "))
        if len(guess) > 1:
            print("You entered too many characters!")
        elif not guess.isalpha():
            print("You entered an invalid character! Please only enter letters of the Greek alphabet.")
        elif guess in guess_store:
            print("You already asked this character! Try another one.")
        else:
            guess_store.append(guess)
            if guess not in secret_word:
                print("Sorry, this character is not in the secret word.")
            else:
                print("Nice try. The character you entered is in the secret word.")
                i = 0
                while i <= len(secret_word)-1:
                    if secret_word[i] == guess:
                        guessed_word[i] = guess + " "
                    i += 1
            num_guesses -= 1
            result = ''.join(guessed_word)
            final_result = result.replace(" ", "")
            if final_result.isalpha():
                print("Congratulations, you have guessed the word %s!" % (secret_word))
                break
            print(''.join(guessed_word))
            print("You have", num_guesses, "guesses left.")
            if num_guesses == 0:
                print("Sorry, this was your last try. You lost.")


hangman(secret_word, 8)