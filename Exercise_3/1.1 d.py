string_1 = "Donald"
string_2 = "Trump"
number = 3

def combine_strings(string_1, string_2, number):
    string = string_2[:number+1]
    reverse_2 = string[::-1]
    new_string = string_1[:number] + reverse_2
    return new_string

print(combine_strings(string_1, string_2, number))