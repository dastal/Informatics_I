# In this case it's better to use functions because you can understand better (or at least faster) what the program is doing
# with the input.

user_sentence = str(input("Please write a sentence: "))


def word_count(sentence):
    count = 1
    for ch in sentence:
        if ch == " ":
            count += 1
    print("Your sentence contains", count ,"word(s).")
word_count(user_sentence)


def reverse_string(sentence):
    reverse = sentence[::-1]
    print(reverse)
reverse_string(user_sentence)


def print_char_by_char(sentence):
    for i in range(0, len(sentence)):
        print(sentence[i])
print_char_by_char(user_sentence)