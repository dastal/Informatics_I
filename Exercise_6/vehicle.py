import sys

class Vehicle(object):

    vehicle_id = 0
    vehicles_sold = []

    def __init__(self,year,mileage,purchase_price,serial_number):
        self.__year = year
        self.__mileage = mileage
        self.__purchase_price = purchase_price
        self.__serial_number = serial_number
        Vehicle.vehicle_id += 1
        self.vehicle_id = Vehicle.generate_vehicle_id()
        #if not str.isdigit(str(self.__year)):
            #raise ValueError("Invalid int value for year!")
        #if not str.isdigit(str(self.__mileage)):
            #raise ValueError("Invalid int value for mileage!")
        #if not str.isdigit(str(self.__purchase_price)):
            #raise ValueError("Invalid int value for purchase_price")


    def __str__(self):
        return str(self.vehicle_id)

    def get_id(self):
        return self.vehicle_id

    @staticmethod
    def generate_vehicle_id():
        vehicle_id = Vehicle.vehicle_id + 99999
        return vehicle_id


class Car(Vehicle):

    def __init__(self,year,mileage,purchase_price,serial_number,doors):
        Vehicle.__init__(self,year,mileage,purchase_price,serial_number)
        self.year = year
        self.mileage = mileage
        self.purchase_price = purchase_price
        self.serial_number = serial_number
        self.doors = doors
        self.__wheels = 4


class Lorry(Vehicle):

    def __init__(self,year,mileage,purchase_price,serial_number,wheels,doors=2):
        Vehicle.__init__(self,year,mileage,purchase_price,serial_number)
        self.year = year
        self.mileage = mileage
        self.purchase_price = purchase_price
        self.serial_number = serial_number
        self.__wheels = wheels
        self.__doors = doors

        
class Motorcycle(Vehicle):

    classic_count = 0

    def __init__(self,year,mileage,purchase_price,serial_number,classic=False):
        Vehicle.__init__(self,year,mileage,purchase_price,serial_number)
        self.year = year
        self.mileage = mileage
        self.puechase_price = purchase_price
        self.serial_number = serial_number
        self.__classic = classic

        Motorcycle.classic_count += 1

### test cases ###

# initialising vehicle instances

Veh1 = Vehicle(2008,65000,7500,"34567851g4")
Veh2 = Car(2007,125000,5500,"e44653ftu1",4)
Veh3 = Car(2012,45000,8900,"gf5622iguz",doors=2)
Veh4 = Lorry(2005,180000,16000,"hbh997123f",6)
Veh5 = Lorry(2013,30000,35000,"hjbf17jbkh",8,4)
Veh6 = Motorcycle(1975,75500,40000,"bh545664rh",True)

print(Veh1,Veh2,Veh3,Veh4,Veh5,Veh6)
#prints 	100000 	100001 	100002 	100003 	100004 	100005

Veh7 = Motorcycle("year",10000,25000,"bjhgss4rdh",False)
# instance Veh7 generates an exception (ValueError) (uncomment to test)
