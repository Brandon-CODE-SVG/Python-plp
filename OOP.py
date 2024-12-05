# # Assignment 1: Design Your Own Class! 🏗️
# # Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
# # Add attributes and methods to bring the class to life!
# # Use constructors to initialize each object with unique values.
# # Add an inheritance layer to explore polymorphism or encapsulation.
# # Activity 2: Polymorphism Challenge! 🎭

# Base class for a Superhero
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def use_power(self):
        return f"{self.name} uses {self.power} to save the day!"

    def __str__(self):
        return f"{self.name}, the superhero from {self.city} with the power of {self.power}."


# Inherited class for a specific type of Superhero
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, city, flight_speed):
        super().__init__(name, power, city)
        self.flight_speed = flight_speed

    def use_power(self):
        return f"{self.name} flies at {self.flight_speed} mph while using {self.power}!"

    def __str__(self):
        return f"{self.name}, the flying superhero from {self.city} with the power of {self.power} and can fly at {self.flight_speed} mph."


# Inherited class for another specific type of Superhero
class StrengthSuperhero(Superhero):
    def __init__(self, name, power, city, strength_level):
        super().__init__(name, power, city)
        self.strength_level = strength_level

    def use_power(self):
        return f"{self.name} lifts {self.strength_level} tons using {self.power}!"

    def __str__(self):
        return f"{self.name}, the strong superhero from {self.city} with the power of {self.power} and can lift {self.strength_level} tons."


# Creating instances of Superhero classes
hero1 = FlyingSuperhero("Skyhawk", "Wind Manipulation", "Metropolis", 120)
hero2 = StrengthSuperhero("Titan", "Super Strength", "Gotham", 10)

# Demonstrating polymorphism
heroes = [hero1, hero2]
for hero in heroes:
    print(hero)
    print(hero.use_power())


# Create a program that includes animals or vehicles with the same action (like move()). However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).

# Base class for Vehicle
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")


# Class for Car
class Car(Vehicle):
    def move(self):
        return "Driving 🚗"


# Class for Plane
class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"


# Class for Bicycle
class Bicycle(Vehicle):
    def move(self):
        return "Pedaling 🚲"


# Class for Boat
class Boat(Vehicle):
    def move(self):
        return "Sailing ⛵"


# Creating instances of each vehicle
vehicles = [Car(), Plane(), Bicycle(), Boat()]

# Demonstrating polymorphism
for vehicle in vehicles:
    print(vehicle.move())