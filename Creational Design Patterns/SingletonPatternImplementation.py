### Singleton Design Pattern - Python Implementation

### Scenario: Shopping Cart - One cart per user 

class ShoppingCart:
    # The class-level dictionary that holds the unique instances based on user ID or session ID
    _instances = {}

    # The __new__ method ensures one instance of the cart per user session
    def __new__(cls, user_id):
        if user_id not in cls._instances:
            cls._instances[user_id] = super(ShoppingCart, cls).__new__(cls)
            cls._instances[user_id].items = []  # Initialize the cart's items list
            cls._instances[user_id].total_price = 0.0  # Initialize total price
        return cls._instances[user_id]

    # Method to add an item to the cart
    def add_item(self, item_name, item_price):
        self.items.append({"name": item_name, "price": item_price})
        self.total_price += item_price

    # Method to get the items in the cart
    def get_items(self):
        return self.items

    # Method to get the total price of the items in the cart
    def get_total(self):
        return self.total_price

    # Method to clear the cart (e.g., after checkout)
    def clear_cart(self):
        self.items.clear()
        self.total_price = 0.0


# Simulating multiple users with different user IDs interacting with their own carts.

# User 1 interacts with their cart
user1_cart = ShoppingCart(user_id=1)
user1_cart.add_item("Apple", 1.0)
user1_cart.add_item("Banana", 1.2)

# User 2 interacts with their own cart (separate instance)
user2_cart = ShoppingCart(user_id=2)
user2_cart.add_item("Orange", 1.5)
user2_cart.add_item("Grapes", 2.0)

# User 1's cart
print("User 1 Cart Items:", user1_cart.get_items())  
print("User 1 Total Price:", user1_cart.get_total())  

# User 2's cart
print("User 2 Cart Items:", user2_cart.get_items())  
print("User 2 Total Price:", user2_cart.get_total())  

# Clearing User 1's cart after checkout
user1_cart.clear_cart()
print("User 1 Cart after clearing:", user1_cart.get_items())  
print("User 1 Total after clearing:", user1_cart.get_total()) 

# Checking User 2's cart, which remains unaffected
print("User 2 Cart after User 1 cleared theirs:", user2_cart.get_items()) 


### Expected Output
# User 1 Cart Items: [{'name': 'Apple', 'price': 1.0}, {'name': 'Banana', 'price': 1.2}]
# User 1 Total Price: 2.2
# User 2 Cart Items: [{'name': 'Orange', 'price': 1.5}, {'name': 'Grapes', 'price': 2.0}]
# User 2 Total Price: 3.5
# User 1 Cart after clearing: []
# User 1 Total after clearing: 0.0
# User 2 Cart after User 1 cleared theirs: [{'name': 'Orange', 'price': 1.5}, {'name': 'Grapes', 'price': 2.0}]