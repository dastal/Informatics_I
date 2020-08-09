def strange_exercise(file_name, args):
    name = file_name + '.txt'
    new_file = open(name, 'w')
    i = 0
    while i <= len(args)-1:
        new_file.write(args[i] + "\n")
        i += 1
    new_file.close()


strange_exercise("credentials", ("David", "Stalder", "13-929-872", "Hello Linus, how are you?"))