address = str(input('Please enter your e-mail address: '))

string_length = len(address)

if string_length > 30:                                                              #first condition
    print('Invalid e-mail address')

if (address[string_length - 1] != "h") and (address[string_length - 2] != "c"):     #second condition
    print('Invalid e-mail address')

for ch in address:                                                                  #third condition
    if (ch == "*") or (ch == "/") or (ch == "0") or (ch == "=") or (ch == '"'):
        print('Invalid e-mail address')
