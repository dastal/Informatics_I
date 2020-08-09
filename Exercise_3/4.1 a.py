def create_acronym(*args):
    acronym = ""
    for string in args:
        acronym = acronym + string[0]
    acronym = acronym.upper()
    print(acronym)

create_acronym("personal", "computer")