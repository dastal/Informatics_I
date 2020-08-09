a = 'random string'

def print_reverse(wort):
    neues_wort = wort[::-1]
    return neues_wort

print(print_reverse(a))

def print_reverse_rec(wort):
    neues_wort = " "
    while len(wort) >= 1:
        b = wort[0]
        neues_wort = b + neues_wort
        wort = wort[1:]
    return neues_wort

print(print_reverse_rec(a))