# In this case it's better to use functions because you can define the function once and use it for several words, instead of writing
# the whole commands as many times as you want to test more words for the same character.
name_1 = "Annalena"
name_2 = "Louise"
name_3 = "Frodo"

def count_o(name):
    count = 0
    for ch in name:
        if ch.lower() == "o":
            count += 1
    return count

def count_l(name):
    count = 0
    for ch in name:
        if ch.lower() == "l":
            count += 1
    return count

print("There are", count_o(name_1) ,"o's in the name", name_1)
print("There are", count_l(name_2) ,"l's in the name", name_2)
print("There are", count_o(name_3) ,"o's in the name", name_3)