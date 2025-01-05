# Factory Method Design Pattern

## Scenario: Apparel Industry - Expanding Clothing Types
**NOTE: The same industry scenario is used to illustrate both the Factory Pattern and the Abstract Factory Pattern to highlight the differences.**

### Problem Statement
FashionCo, a leading apparel brand, currently produces shirts, trousers, jackets, and shoes. With growing customer demand, the company now plans to expand its product line to include sweaters and hats. Each clothing type requires a distinct production process, packaging, and shipping method. However, FashionCo wants to streamline its production system to handle various clothing types without having to modify existing code when new clothing types are introduced.  <br>

**As a software architect, what design pattern would you suggest to satisfy this requirement?**

### Motivation for choosing Factory Pattern

&nbsp; **1. Decoupling Object Creation from Client Code:** <br>
The Factory Method enables FashionCo to reduce the client's dependence on specific implementations. The client interacts with a common interface and is unaware of the actual product class being instantiated, promoting loose coupling between object creation and client code. <br>

&nbsp; **2. Code Reusability and Maintainability:**  <br>
Using the Factory Method allows FashionCo to update product creation logic for specific items (e.g., T-shirts) with new materials or processes without needing to update all client instances that use the T-shirt class. <br>

&nbsp; **3. Support for Extensibility:** <br>
The Factory Method supports the easy addition of new product types. FashionCo can add new clothing items, such as sweaters or hats, without modifying any existing code, ensuring seamless extensibility.

### Reasons for not choosing Abstract Factory Pattern

&nbsp; **1. No need of grouping:** <br>
In this case, FashionCo is primarily creating individual, unrelated products, and there is no need to group them into families of products. The Factory Method is sufficient for this scenario, without the added complexity of managing product families. <br>

&nbsp; **2. Less complexity:** <br>
The Abstract Factory Pattern introduces unnecessary complexity for this problem. The client code would need to decide which abstract factory to use and deal with multiple product families, even though the products here are unrelated. The Factory Method simplifies this by focusing on individual product creation. <br>

### Intent
The Factory Method serves as an interface for creating objects. Subclasses or concrete implementations decide which class to instantiate based on client input, allowing for flexibility and extensibility in creating objects.

### Python Implementation
The Python implementation for this pattern can be found in the [FactoryMethodPatternImplementation.py](https://github.com/kavya6697/DesignPatternsNotes/blob/main/Creational%20Design%20Patterns/FactoryMethodPatternImplementation.py).

### Related Patterns
1.  Abstract Factory <br>
2.  Prototype <br>

### Other Real-world Applicable Scenarios

**1. Hyundai:** A car manufacturing company that produces various models like SUVs, Sedans, and Hatchbacks can use the Factory Method to handle different car models efficiently, with each model having its own production process.

### Collaboration & Suggestions 
If you wish to collaborate or suggest any improvements, please feel free to reach out via Mail - ramisetty.kavya06@gmail.com

