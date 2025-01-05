# Builder Design Pattern

## Scenario: PizzaHut

### Problem Statement
PizzaHut, a popular pizza restaurant, offers a wide variety of customizable pizzas. Customers can select different sauces, toppings, and sizes, allowing them to create a pizza tailored to their preferences. As the combinations grow, PizzaHut aims to provide an intuitive, step-by-step process for customers to build their own pizza. <br>

**As a software architect, what design pattern would you suggest to satisfy this requirement?**

### Motivation for choosing Builder Design Pattern

&nbsp; **1. Complexity of Customization:** <br>
The Builder Pattern helps PizzaHut manage the complexity of creating a pizza by breaking down the process into manageable steps. Each component (such as crust, sauce, toppings, and size) is added one at a time, in a structured manner, making the customization process simpler for both developers and customers. <br>

&nbsp; **2. Avoiding the Telescoping Constructor Problem:**  <br>
Without the Builder Pattern, PizzaHut might need constructors with many parameters (e.g., a constructor that accepts crust, sauce, toppings, size, and special features). This can lead to a telescoping constructor problem where multiple constructors are needed to accommodate various combinations of pizza attributes. The Builder Pattern solves this by allowing method chaining, simplifying the code and making it more flexible. <br>

&nbsp; **3. Easy Validation:** <br>
The Builder can ensure the pizza is correctly assembled with all required components in the correct order. For instance, it prevents creating a pizza without essential components like crust or sauce. Additionally, it can enforce business rules such as "if extra cheese is selected, the pizza must be a certain size" or "only a limited number of toppings can be added." <br>

### Intent
Separate the construction of a complex object from its representation, allowing the same construction process to create different representations of the object.

### Python Implementation
The Python implementation for this pattern can be found in the [BuilderPatternImplementation.py](https://github.com/kavya6697/DesignPatternsNotes/blob/main/Creational%20Design%20Patterns/BuilderPatternImplementation.py).

### Related Patterns
1. Abstract Factory <br>
2. Composite <br>

### Other Real-world Applicable Scenarios

**1. House Costruction:** Building a house involves many components (e.g., walls, roof, windows, doors, floors) and can have various configurations, such as different materials, sizes, and layouts. The Builder Pattern is perfect for this scenario because it allows for step-by-step construction of the house with flexible options while keeping the construction process organized. <br>

### Collaboration & Suggestions 
If you wish to collaborate or suggest any improvements, please feel free to reach out via Mail - ramisetty.kavya06@gmail.com
