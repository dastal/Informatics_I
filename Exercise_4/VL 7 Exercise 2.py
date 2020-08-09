class DeveloperIntern(Developer):

    def __init__(self, name, address, internship_duration):
        Developer.__init__(self, name, address)
        self.__internship_duration = internship_duration

    def get_internship_duration(self):
        return self.__internship_duration

    def write_code(self):
        return "print('Hello, World!')"

    def __str__(self):
        return "Developer intern: " + self.get_name()

intern = DeveloperIntern("Chris Black", "White Str 21", 6)
print(intern) # Developer intern: Chris Black
print("Internship duration: %d months\n" %
intern.get_internship_duration())