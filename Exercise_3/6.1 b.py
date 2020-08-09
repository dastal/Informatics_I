sherlock_holmes = open("Sherlock_Holmes.txt", "r")

sentence = input("Please enter a sentnence:\n")


def check_if_in_file(filename, text):
    if text in filename.read():
        print(True)
    else:
        print(False)


check_if_in_file(sherlock_holmes, sentence)