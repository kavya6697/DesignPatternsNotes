# Singleton Design Pattern

## Scenario: Shopping Cart

### Problem Statement
VMart is a static grocery website where users can browse available items in the store. With the rise of e-commerce, VMart now wants to implement an online shopping cart for users to purchase items. A user will have only one cart to add items, and this cart should be accessible by other functionalities like billing. <br>

**As a software architect, what design pattern would you suggest to satisfy this requirement?**

### Motivation for choosing Singleton Design Pattern

&nbsp; **1. Single Instance Per User Session:** <br>
The Singleton pattern helps VMart maintain a unique shopping cart per user session. Only one instance of the cart will be created per session, which can be accessed by other functionalities like adding items, calculating bills, and more. <br>

&nbsp; **2. Centralized Cart Logic:**  <br>
The Singleton pattern ensures centralized control over operations like adding items, updating quantities, calculating totals, and applying discounts. Since all interactions with the cart go through the same instance, it simplifies making and updating cart logic.<br>

&nbsp; **3. Resource Efficiency:** <br>
The Singleton pattern reduces the overhead of creating and destroying multiple instances of the shopping cart. The cart is created once and used throughout the session, making the application more efficient and less resource-heavy. <br>

### Intent

Ensure that a class has only one instance and provide a global point of access to that instance.

### Python Implementation
The Python implementation for this pattern can be found in the [SingletonPatternImplementation.py](https://github.com/kavya6697/DesignPatternsNotes/blob/74dc201c935f99a80cba1d45d0b72c77ea02376b/Creational%20Design%20Patterns/SingletonPatternImplementation.py).

### Related Patterns
1. Abstract Factory <br>
2. Builder <br>
3. Prototype <br>

### Other Real-world Applicable Scenarios

**1. Cache Manager:** A caching system that stores frequently accessed data to improve performance. The cache manager should be a single instance to avoid inconsistent or duplicated data across multiple caches.

### Collaboration & Suggestions 
If you wish to collaborate or suggest any improvements, please feel free to reach out via Mail - ramisetty.kavya06@gmail.com

