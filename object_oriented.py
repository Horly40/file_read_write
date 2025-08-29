
class Bahubali:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"{self.name} uses {self.power}!")

class FlyingHero(Bahubali):
    def __init__(self, name, power, flying_speed):
        super().__init__(name, power)
        self.flying_speed = flying_speed

    def attack(self):
        print(f"{self.name} attacks while flying at {self.flying_speed} km/h with {self.power}!")

# Testing
hero1 = Bahubali("Thor", "Thunder")
hero2 = FlyingHero("Bahubali", "Repulsor Blast", 500)

hero1.attack()
hero2.attack()

# Polymorphism with Vehicles

class Car:
    def move(self):
        print("Driving 🚗")

class Plane:
    def move(self):
        print("Flying ✈️")

class Bicycle:
    def move(self):
        print("Pedaling 🚴")

# Create objects
car = Car()
plane = Plane()
bike = Bicycle()

# Call their move() methods
car.move()     # Output: Driving 🚗
plane.move()   # Output: Flying ✈️
bike.move()    # Output: Pedaling 🚴

print("\n--- Polymorphism in a Loop ---")
vehicles = [car, plane, bike]

for v in vehicles:
    v.move()   # Each object responds in its own way!

