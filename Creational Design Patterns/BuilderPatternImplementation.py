### Builder Design Pattern - Python Implementation

### Scenario: PizzaHut 

# Define the Pizza class (the final product)

class Pizza:
    def __init__(self, crust, sauce, toppings, size, special_features=None):
        self.crust = crust
        self.sauce = sauce
        self.toppings = toppings
        self.size = size
        self.special_features = special_features if special_features else []

    def __str__(self):
        return (f"Pizza with {self.crust} crust, {self.sauce} sauce, "
                f"toppings: {', '.join(self.toppings)}, Size: {self.size}, "
                f"Special Features: {', '.join(self.special_features)}")

# Define the PizzaBuilder class (the Builder)

class PizzaBuilder:
    def __init__(self):
        self.crust = None
        self.sauce = None
        self.toppings = []
        self.size = None
        self.special_features = []

    def set_crust(self, crust):
        self.crust = crust
        return self

    def set_sauce(self, sauce):
        self.sauce = sauce
        return self

    def set_toppings(self, toppings):
        self.toppings = toppings
        return self

    def set_size(self, size):
        self.size = size
        return self

    def add_special_feature(self, feature):
        self.special_features.append(feature)
        return self

    def build(self):
        return Pizza(self.crust, self.sauce, self.toppings, self.size, self.special_features)

# Create a PizzaDirector class (optional) for predefined pizzas

class PizzaDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_margherita(self):
        return (self.builder
                .set_crust("Thin Crust")
                .set_sauce("Tomato Sauce")
                .set_toppings(["Mozzarella", "Basil"])
                .set_size("Medium")
                .add_special_feature("Extra Cheese")
                .build())

    def construct_pepperoni(self):
        return (self.builder
                .set_crust("Thick Crust")
                .set_sauce("Tomato Sauce")
                .set_toppings(["Pepperoni", "Cheese"])
                .set_size("Large")
                .add_special_feature("Spicy")
                .build())

# Using the Builder
if __name__ == "__main__":
    # Build a custom pizza
    builder = PizzaBuilder()
    custom_pizza = builder.set_crust("Stuffed Crust") \
                          .set_sauce("BBQ Sauce") \
                          .set_toppings(["Chicken", "Onions", "Olives"]) \
                          .set_size("Large") \
                          .add_special_feature("Extra Cheese") \
                          .build()

    print("Custom Pizza:")
    print(custom_pizza)
    
    # Use PizzaDirector for a predefined pizza
    director = PizzaDirector(builder)
    margherita = director.construct_margherita()
    pepperoni = director.construct_pepperoni()

    print("\nPredefined Pizza (Margherita):")
    print(margherita)

    print("\nPredefined Pizza (Pepperoni):")
    print(pepperoni)

### Expected Output
# Custom Pizza:
# Pizza with Stuffed Crust crust, BBQ Sauce sauce, toppings: Chicken, Onions, Olives, Size: Large, Special Features: Extra Cheese

# Predefined Pizza (Margherita):
# Pizza with Thin Crust crust, Tomato Sauce sauce, toppings: Mozzarella, Basil, Size: Medium, Special Features: Extra Cheese, Extra Cheese, Spicy

# Predefined Pizza (Pepperoni):
# Pizza with Thick Crust crust, Tomato Sauce sauce, toppings: Pepperoni, Cheese, Size: Large, Special Features: Extra Cheese, Extra Cheese, Spicy