class Employee(object):
    num_emplyees = 0

    def __init__(self, name, address):
        self.__name = name
        self.__address = address
        self.__id = Employee.num_emplyees
        Employee.num_emplyees += 1

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def __str__(self):
        return "Employee: " + self.__name

employee_1 = Employee("John Smith", "Maple Street 21")
employee_2 = Employee("Jane Smith", "Miller Street 10")
employee_3 = Employee("Kate Black", "Cambridge Street 5")
print(employee_1.get_id())  # 0
print(employee_2.get_id())  # 1
print(employee_3.get_id())