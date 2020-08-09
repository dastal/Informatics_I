string = "101 Dalmatians"
number = 101

def is_number_in_string(string,number):
    number = str(number)
    new_string = string
    while len(string) >= 3:
        if new_string[0] != number[0] and new_string[1] != number[1] and new_string[2] != number[2]:
            return False
        elif string[0] == number[0] and string[1] == number[1] and string[2] == number[2]:
            return True
            break
        new_string = new_string[1:]


print(is_number_in_string(string,number))