### Factory Method Design Pattern - Python Implementation

### Scenario: Apparel Company - Expanding Clothing Types

# Abstract class (or interface) that defines the common methods that all clothing types should have.
# The abstract methods inside this interface will not have any implementation. 
# A class that inherits this will do the implementation part.

class Clothing:
    def get_material(self):
        raise NotImplementedError("Subclasses must implement this method")

    def get_size(self):
        raise NotImplementedError("Subclasses must implement this method")

    def get_price(self):
        raise NotImplementedError("Subclasses must implement this method")


# Concrete classes that inherit from Clothing abstract class, and implement abstract methods. 

class Shirt(Clothing):
    def get_material(self):
        return "Cotton"

    def get_size(self):
        return "M"

    def get_price(self):
        return 30


class Trousers(Clothing):
    def get_material(self):
        return "Denim"

    def get_size(self):
        return "L"

    def get_price(self):
        return 40


class Sweater(Clothing):
    def get_material(self):
        return "Wool"

    def get_size(self):
        return "M"

    def get_price(self):
        return 50


# Abstract class with abstract method which will be implemented by concrete classes to create specific products.

class ClothingFactory:
    def create_clothing(self):
        raise NotImplementedError("Subclasses must implement this method")


# Concrete classes inherit abstract class and implement abstract method.

class ShirtFactory(ClothingFactory):
    def create_clothing(self):
        return Shirt()


class TrousersFactory(ClothingFactory):
    def create_clothing(self):
        return Trousers()


class SweaterFactory(ClothingFactory):
    def create_clothing(self):
        return Sweater()


# Client Code
def client_code(factory: ClothingFactory):
    clothing = factory.create_clothing()
    print(f"Clothing Type: {clothing.__class__.__name__}")
    print(f"Material: {clothing.get_material()}")
    print(f"Size: {clothing.get_size()}")
    print(f"Price: ${clothing.get_price()}")
    print()


# Usage of the Factory Method
shirt_factory = ShirtFactory()
trousers_factory = TrousersFactory()
sweater_factory = SweaterFactory()

print("Creating a Shirt:")
client_code(shirt_factory)

print("Creating Trousers:")
client_code(trousers_factory)

print("Creating a Sweater:")
client_code(sweater_factory)


### Expected Output
# Creating a Shirt:
# Clothing Type: Shirt
# Material: Cotton
# Size: M
# Price: $30

# Creating Trousers:
# Clothing Type: Trousers
# Material: Denim
# Size: L
# Price: $40

# Creating a Sweater:
# Clothing Type: Sweater
# Material: Wool
# Size: M
# Price: $50
