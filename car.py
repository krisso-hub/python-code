class Car:
    '''A simple attempt to model a car'''
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

# show the car descriptions
    def get_descriptive_car(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

# displays the car mileage
    def read_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
            print(f"The mileage reads {self.odometer_reading} miles")
        else:
            print("you cant rollback odometer")

# display car mileage update
    def increment_odometer(self, miles):
        self.odometer_reading += miles
        print(f"The mileage right now is {self.odometer_reading} miles")

my_car = Car("toyota", "camry", 2009)
print("the car I'm using now is:\t")
print(my_car.get_descriptive_car())
my_car.read_odometer(20)
my_car.increment_odometer(50)

class ElectricCar(Car):
# represent an aspect of a car, specific to electric vehicle

    def __init__(self, make, model, year):

# initiate the attribute of a parent class
        super().__init__(make, model, year) 
        self.battery_size = 70

# shows the size of the battery
    def describe_battery(self, battery_size):
        self.battery_size = battery_size
        print(f"The size of my car battery is {self.battery_size}-Kwh")
        print("When fully charged I drive it a whole week")


my_tesla = ElectricCar("honda", "accord sport", 2014)
print("\n My second car is: ")
print(my_tesla.get_descriptive_car())
my_tesla.read_odometer(10)
my_tesla.increment_odometer(25)
my_tesla.describe_battery(100)


        


        