text = "A list, similarly to a tuple, is an ordered set of values (or elements), where each value is identified by an index. The contained values can be of any type and a single list can even contain mixed values. The main difference between the twodata structures is that lists are mutable."


def word_count(string):
    i = 1
    for singn in string:
        if singn == " ":
            i += 1
    print("The string has", i , "words.")


word_count(text)