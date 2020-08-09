class Employee(object):
    def __init__(self, name, address):
        self.__name = name
        self.__address = address

    def get_name(self):
        return self.__name

    def __str__(self):
        return "Employee: " + self.__name

employee = Employee("John Smith", "Maple Street 21")
print(employee)
# Employee: John Smith

class Manager(Employee):
    def __str__(self):
        return "Manager: " + self.get_name()

class Developer(Employee):
    def __str__(self):
        return "Developer: " + self.get_name()

class UXDesigner(Employee):
    def __str__(self):
        return "UXDesigner: " + self.get_name()

employee = Employee('John Smith', 'Maple Street 25')
manager = Manager('Jane Doe', 'Miller Street 10')
developer = Developer('Kate Black', 'Cambridge Street 5')
uxdesigner = UXDesigner('Lucy White', 'Broadway Street')

print(employee) # calls Employee.__str__
print(manager) # calls Employee.__str__
print(developer) # calls Employee.__str__
print(uxdesigner) # calls Employee.__str__

print(employee.get_name()) # calls Employee.get_name()
print(manager.get_name()) # calls Employee.get_name()
print(developer.get_name()) # calls Employee.get_name()
print(uxdesigner.get_name()) # calls Employee.get_name()