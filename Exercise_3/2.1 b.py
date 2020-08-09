c = 3

def compare_numbers(a,b):
    if a > b:
        print("{0:d} is bigger than {1:d}".format(a,b))
    elif a < b:
        print("{0:d} is smaller than {1:d}".format(a,b))
    else:
        print("{0:d} is equal as {1:0}".format(a,b))

compare_numbers(a=3,b=2)    # compare_numbers(2,a=3) there were too many arguments for a, so I changed the position of the
                            # two arguments and assigned 2 to b
compare_numbers(3,b=2)      # compare_numbers(b=2,3) here a positional argument followes a keyword argument, what must be
                            # exactly vice versa
compare_numbers(2,c)        # comparee_numbers(2,c=3) there was an unexpected keyword argument, so I defined the parameter
                            # c on the top of the program