language = input("What is your first language? (answer in English please) ")
print(language)

if (language == 'German') or (language == 'german'):
    print('Hallo!')
elif (language == 'English') or (language == 'english'):
    print('Hello')
elif (language == 'Spanish') or (language == 'spanish'):
    print('¡Hola!')
elif (language == 'French') or (language == 'french'):
    print('Salut!')
elif (language == 'Italian') or (language == 'italian'):
    print('Ciao!')
elif (language == 'Russian') or (language == 'russian'):
    print('привет!')
elif (language == 'Swedish') or (language == 'swedish'):
    print('Hej!')
else:
    print("Sorry I don't speak your language...")