def longest_string(*args):
    longest_string = ""
    length = 0
    for i in args:
        if len(i) > length:
            longest_string = i
            length = len(i)
    print("The longest string was '{0:s}' with {1:d} characters!".format(longest_string, length))

longest_string("Dampf", "Dampfschiff", "Dampfschifffahrt", "Dampfschifffahrtsgesellschaft", "Dampfschifffahrtsgesellschaftsmatrose")