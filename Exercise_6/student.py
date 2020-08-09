from module import *
from moduleElement import *

class Student(object):

    def __init__(self, name):
        self.name = name
        self.modules = []
        self.grades = {}

    def add_module(self,title):
        module = Module.get_title(title)
        self.modules.append(module)
        grade = Module.get_grade(title)
        self.grades[module] = grade

    def get_list_modules(self):
        for module in self.modules:
            print("Modules of student " + self.name + ":")
            print(module)

    def get_grades(self):
        print("Grades of Student " + self.name + ":")
        for grade in self.grades:
            msg = grade + ": " + str(self.grades[grade])
            print(msg)


### test cases ###

me = Student("FirstName LastName")
me.add_module(info1)
me.get_list_modules()
# expected output:
# Modules of Student FirstName LastName:
#	Info 1

me.get_grades()
# expected output:
# Grades of Student FirstName LastName:
#	Info 1: 6
