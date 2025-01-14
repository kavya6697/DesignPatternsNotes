# Chain Of Responsibility Design Pattern

## Scenario: Customer Support System

### Problem Statement
Design a customer support system where incoming requests are automatically passed through a series of handlers (representing different support teams or departments) until an appropriate handler resolves the issue. Each handler in the chain either processes the request or passes it on to the next handler based on its expertise, ensuring no request goes unresolved. <br>

**As a software architect, what design pattern would you suggest to satisfy this requirement?**

### Motivation for choosing Chain Of Responsibility Pattern

&nbsp; **1. Dynamic Request Handling:** <br>
The Chain of Responsibility pattern allows requests to be routed dynamically to the appropriate team or department without needing hardcoded routing logic. <br>

&nbsp; **2. Simplified Request Escalation:**  <br>
This pattern naturally supports escalation by passing the request through the chain until it reaches the appropriate handler or level of authority, ensuring smooth and automatic issue resolution. <br>

&nbsp; **3. Decoupling the Request Sender and Handlers:** <br>
Customers do not need to know which specific team or department will handle their request. They simply submit their inquiry, and the system automatically routes it to the correct handler, creating a seamless user experience and reducing customer effort. <br>

### Intent
The goal is to avoid tightly coupling the sender of the request to its receiver. Multiple handlers are given the chance to process the request, and the request is passed along the chain until an object handles it.  

### Python Implementation
The Python implementation for this pattern can be found in the []().

### Related Patterns
1. Composite <br>

### Other Real-world Applicable Scenarios

**Order Processing System in E-Commerce:** In an e-commerce system, an order can be passed through a chain of handlers, with each handler checking whether it can process the order or whether it should pass the order to the next handler in the chain (e.g., payment processing, inventory check, shipping, etc.). <br>

### Collaboration & Suggestions 
If you wish to collaborate or suggest any improvements, please feel free to reach out via Mail - ramisetty.kavya06@gmail.com
