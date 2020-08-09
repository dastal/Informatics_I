grenze = int(input('Geben Sie eine Grenze ein: '))
basis = int(input('Geben Sie eine Basis ein: '))

def multiples_of(a, b):
    c = b
    result = ""
    while c <= a:
        if c % b == 0:
            result = result + "  " + str(c)
        c += 1
    return result

print(multiples_of(grenze, basis))