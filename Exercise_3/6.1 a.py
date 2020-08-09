sherlock_holmes = open("Sherlock_Holmes.txt", "r")


def print_file(filename, num_char, num_lines = 0):
    lines = [lines for lines in filename.readlines() if lines.strip()]
    if num_lines == 0:
        i = 0                                                                   # Zählvariable
        while i <= len(lines)-1:
            line = lines[i]
            output = line[:num_char]
            print(output)
            i += 1
    else:
        i = 0                                                                   # Zälvariable
        while i <= num_lines-1:                                                 # so bleibt die Anzahl Lnien im Rage
            line = lines[i]
            output = line[:num_char]
            print(output)
            i += 1


print_file(sherlock_holmes,10,6)


sherlock_holmes.close()