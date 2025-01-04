# Factory Method Design Pattern

## Scenario: Apparel Industry - Clothing Type Expansion
**NOTE: The same industry scenario is used to illustrate both the Factory Pattern and the Abstract Factory Pattern to highlight the differences.**

### Problem Statement
FashionCo is a leading apparel brand produces shirts, trousers, jackets, and shoes. With increasing demand, the company now wants to expand its offerings to sweaters and hats. Each clothing type requires a different production process, packaging, and shipping method. However, the company wants to streamline its clothing production system, allowing for easy management of various clothing types without the need to modify the existing code when new clothing types are introduced.  <br>

**As a software architect, what design pattern would you suggest to satisfy this requirement?**

### Motivation for choosing Factory Pattern

&nbsp; **1. Decoupling Object Creation from Client Code:** <br>
Factory method allows FashionCo to reduce the client dependency on specific implementations. Client just interacts with common interface, and is completely unaware of what product types are created.  <br>

&nbsp; **2. Code Reusability and Maintainability:**  <br>
Factory method allows FashionCo to update TShirt creation with new fabrics easily without updating to all clients that uses TShirt. <br>

&nbsp; **3. Support Extensibility:** <br>
Factory method allows FashionCo to add new product types with out making any changes to existing code.

### Reasons for not choosing Abstract Factory Pattern

&nbsp; **1. No need of grouping:** <br>
In this scenario, we are simply creating individual unrelated products. <br>

&nbsp; **2. Less complexity:** <br>
Abstract factory unnecessarily addes complexity client code because they should know about product families and decide which  abstract factory to implement. <br>

### Intent
Factory method is like an interface for creating an object. Subclasses decide which class to be instantiated for object creation based on the input from client.


### Python Implementation
The Python implementation for this pattern can be found in the []().

### Related Patterns
1.  Abstract Factory <br>
2.  Prototype <br>

### Other Real-world Applicable Scenarios

**1. Hyndai:** A car manufacturing company produces SUVs, Sedan, and hatchback models.

### Collaboration & Suggestions 
If you wish to collaborate or suggest any improvements, please feel free to reach out via Mail - ramisetty.kavya06@gmail.com

