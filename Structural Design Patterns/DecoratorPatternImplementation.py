### Decorator Pattern 

### Scenario Used: Customized Coffee Shop Order

# Base class for Coffee
class Coffee:
    def cost(self):
        return 5  # base cost for a simple coffee

# Decorator Class for Milk
class MilkDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee  # Wrapping the base coffee
    
    def cost(self):
        return self._coffee.cost() + 2  # Adding the cost of milk

# Decorator Class for Sugar
class SugarDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee  # Wrapping the base coffee
    
    def cost(self):
        return self._coffee.cost() + 1  # Adding the cost of sugar

# Decorator Class for Whipped Cream
class WhippedCreamDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee  # Wrapping the base coffee
    
    def cost(self):
        return self._coffee.cost() + 3  # Adding the cost of whipped cream

# Decorator Class for Caramel Syrup
class CaramelDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee  # Wrapping the base coffee
    
    def cost(self):
        return self._coffee.cost() + 2  # Adding the cost of caramel syrup

# Client code to demonstrate the Decorator Pattern
if __name__ == "__main__":
    # Start with a basic coffee
    basic_coffee = Coffee()
    print(f"Basic Coffee cost: ${basic_coffee.cost()}")

    # Add milk and sugar to the coffee
    coffee_with_milk_and_sugar = SugarDecorator(MilkDecorator(basic_coffee))
    print(f"Coffee with milk and sugar cost: ${coffee_with_milk_and_sugar.cost()}")

    # Add whipped cream to the previous order
    coffee_with_whipped_cream = WhippedCreamDecorator(coffee_with_milk_and_sugar)
    print(f"Coffee with milk, sugar, and whipped cream cost: ${coffee_with_whipped_cream.cost()}")

    # Add caramel syrup to the previous order
    coffee_with_caramel = CaramelDecorator(coffee_with_whipped_cream)
    print(f"Coffee with milk, sugar, whipped cream, and caramel cost: ${coffee_with_caramel.cost()}")


### Expected Output
# Basic Coffee cost: $5
# Coffee with milk and sugar cost: $8
# Coffee with milk, sugar, and whipped cream cost: $11
# Coffee with milk, sugar, whipped cream, and caramel cost: $13