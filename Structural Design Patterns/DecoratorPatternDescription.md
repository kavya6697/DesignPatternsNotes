# Decorator Design Pattern

## Scenario: Customized Coffee Shop Order

### Problem Statement
A coffee shop needs a system where customers can order a basic coffee and customize it by adding different ingredients. Each ingredient should add a specific cost to the original coffee price. The system should be flexible enough to easily incorporate new ingredients (e.g., flavors, toppings) without modifying the existing coffee class or other customization options. <br>

**As a software architect, what design pattern would you suggest to satisfy this requirement?**

### Motivation for choosing Decorator Pattern

&nbsp; **1. Dynamic Composition:** <br>
The Decorator Pattern allows the coffee shop to dynamically combine different customizations on top of the base coffee. This is especially beneficial when customers can mix various ingredients in any order (e.g., coffee with milk and sugar or coffee with whipped cream and caramel). Each customization (e.g., milk, sugar, whipped cream) is an independent decorator that wraps the base coffee, allowing for flexible and reusable customization. The customizations can be combined dynamically at runtime without modifying the original coffee class. <br>

&nbsp; **2. Avoids Subclass Explosion:**  <br>
Without the Decorator Pattern, the coffee shop would need to create many subclasses for every combination of customizations, resulting in a combinatorial explosion of subclasses (e.g., EspressoWithMilkAndSugar). The Decorator Pattern eliminates this problem by allowing customizations to be applied dynamically, without needing separate subclasses for every combination of ingredients. <br>

&nbsp; **3. Simplifies Client Code::** <br>
With the Decorator Pattern, the coffee shop staff (clients) can simply interact with the base coffee object and apply any number of decorators as required. They do not need to manage complex combinations of ingredients or worry about the specific customizations for each order. This keeps the client code clean, simple, and focused on applying the customizations, while the pattern handles the complexity of combining and calculating prices. <br>

### Intent
The Decorator Pattern enables to dynamically attach additional responsibilities to an object, allowing for greater customization and flexibility in extending the behavior of an object.

### Python Implementation
The Python implementation for this pattern can be found in the []().

### Related Patterns
1. Adapter <br>
2. Composite <br>
3. Strategy <br>

### Other Real-world Applicable Scenarios

**Coupons in Online Shopping:** In an online shopping system, the items in the cart have a base price. If a coupon is applied, it reduces the base price by a specific discount. The Decorator Pattern can be used to apply different types of discounts (e.g., percentage, fixed amount, or seasonal discount) on top of the base price dynamically, ensuring flexibility and scalability in applying multiple discounts. <br>

### Collaboration & Suggestions 
If you wish to collaborate or suggest any improvements, please feel free to reach out via Mail - ramisetty.kavya06@gmail.com
