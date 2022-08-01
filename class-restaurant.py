# modeling a restarunat
class Restaruant:
# initializes the restaruant name and cuisine
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

# describe the location and kind of cuisine
    def describe_restaruant(self):
        print(f"The {self.name} is on the east side")
        print(f"The {self.name} has a classic {self.cuisine_type}")

# shows the hours of operation
    def open_restaurant(self):
        print(f"The {self.name} is opened from 8am to 10pm")

her_restaruant = Restaruant("Delicious Restarunat", "french cuisine")
print(f"{her_restaruant.name} is a place to visit")
print(f"The restaruant is a {her_restaruant.cuisine_type}")
her_restaruant.describe_restaruant()
her_restaruant.open_restaurant()

his_restaruant = Restaruant("Cheesecake", "Italian cuisine")
print(f"\nI love {his_restaruant.name}")
his_restaruant.open_restaurant()

mexico_restaruant = Restaruant("Qdoba", "mexican cuisine")
print(f"\nThe {mexico_restaruant.name} restaurant is almost every where.")
print(f"The {mexico_restaruant.name} is a {mexico_restaruant.cuisine_type}")
mexico_restaruant.open_restaurant()

class IceCreamStand(Restaruant)
    def __init__(self, name, flavors):

        super().__init__(name, cuisine_type)
        self.flavors = []

        pass