### Abstract Factory Design Pattern - Python Implementation

### Scenario: Apparel Company - Clothing Line Expansion

## Abstract Base Classes (ABC)
from abc import ABC, abstractmethod

## Step 1: Define abstract product interfaces different product like shirts and trousers

class Shirt(ABC):
    @abstractmethod
    def create(self):
        pass

class Trousers(ABC):
    @abstractmethod
    def create(self):
        pass

## Step 2: Define concrete products for each category like casual and formal

class CasualShirt(Shirt):
    def create(self):
        return "Casual Shirt Created"

class CasualTrousers(Trousers):
    def create(self):
        return "Casual Trousers Created"

class FormalShirt(Shirt):
    def create(self):
        return "Formal Shirt Created"

class FormalTrousers(Trousers):
    def create(self):
        return "Formal Trousers Created"

## Step 3: Create an abstract factory with methods for creating each product type

class ApparelFactory(ABC):
    @abstractmethod
    def create_shirt(self):
        pass

    @abstractmethod
    def create_trousers(self):
        pass

## Step 4: Concrete factories will implement abstract factory methods to create specific products for different categories.

class CasualApparelFactory(ApparelFactory):
    def create_shirt(self):
        return CasualShirt()

    def create_trousers(self):
        return CasualTrousers()

class FormalApparelFactory(ApparelFactory):
    def create_shirt(self):
        return FormalShirt()

    def create_trousers(self):
        return FormalTrousers()

## Client Code work with different types of apparel without worrying about their concrete implementations

def client_code(factory: ApparelFactory):
    shirt = factory.create_shirt()
    trousers = factory.create_trousers()

    print(shirt.create())
    print(trousers.create())

# Testing the abstract factory pattern

print("Casual Apparel:")
casual_factory = CasualApparelFactory()
client_code(casual_factory)

print("\nFormal Apparel:")
formal_factory = FormalApparelFactory()
client_code(formal_factory)


### Expected Output
# Casual Apparel:
# Casual Shirt Created
# Casual Trousers Created

# Formal Apparel:
# Formal Shirt Created
# Formal Trousers Created