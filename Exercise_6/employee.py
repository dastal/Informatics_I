from vehicle import *
from customer import *

class Employee(object):
    emp_id = 0

    def __init__(self, name):
        self.__name = name
        self.__id = Employee.emp_id + 1

    def __str__(self):
        return "Employee: " + self.__name + " is of type " + Employee.get_title(self)

    def get_name(self):
        return self.__name
    
    def get_title(self):
        return "Subordinate"
    
class Manager(Employee):

    def __init__(self,name):
        Employee.__init__(self,name)
        self.name = name

    def get_title(self):
        return "Manager"

    def get_sales_report(self,salesman):
        name = salesman.name
        print(name + "'s current cumulative sales:")
        if name not in salesman.sales:
            raise KeyError("Key is not in in Sales dictionary yet")
        for sale in salesman.sales:
            if sale == name:
                print(salesman.sales[sale])

    def __str__(self):
        return "Employee: " + self.name + " is of type " + Manager.get_title(self)


class Salesman(Employee):

    sales = {}

    def __init__(self,name):
        Employee.__init__(self,name)
        self.name = name

    def sale(self,vehicle,sales_price,customer):
        self.vehicle = vehicle
        self.sales_price = sales_price
        credit_score = customer.credit_score()
        if credit_score == True:
            if self.name in Salesman.sales:
                Salesman.sales[self.name] += self.sales_price
            else:
                Salesman.sales[self.name] = self.sales_price
        else:
            print("The customer doesn't have enough credit score.")


### test cases ###

## initialising employee instances

Eric = Manager("Eric")
Kyle = Employee("Kyle")
Stan = Salesman("Stan")
Kenny = Salesman("Kenny")
Craig = Salesman("Craig")

## printing employee instances

print(Eric) # expected output: Employee: Eric is of type Manager
print(Kyle) # expected output: Employee: Kyle is of type Subordinate
print(Stan) # expected output: Employee: Stan is of type Subordinate
print(Kenny) # expected output: Employee: Kenny is of type Subordinate
print(Craig) # expected output: Employee: Craig is of type Subordinate


## registering sales

Kenny.sale(Veh2,6000,Heidi)

Stan.sale(Veh1,9000,Wendy)


## printing an individual sales report:

Eric.get_sales_report(Kenny)
# expected output:
# Kenny's current cumulative sales:
# 6000