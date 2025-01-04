# Abstract Factory Design Pattern

## Scenario: Apparel Industry - Clothing Line Expansion
**NOTE: The same industry scenario is used to illustrate both the Factory Pattern and the Abstract Factory Pattern to highlight the differences.**

### Problem Statement
FashionCo is a leading apparel brand known for casual wear. With increasing demand, the company now wants to expand its offerings to include formal wear and sportswear. Each collection will feature shirts, trousers, jackets, and shoes, for men, women, and children, available in various fabrics and colors. Currently, the company is struggling with effective grouping of related product families under one unified structure. <br>

**As a software architect, what design pattern would you suggest to satisfy this requirement?**

### Motivation for choosing Abstract Factory Pattern

&nbsp; **1. Consistency Across Product Families:** <br>
The Abstract Factory pattern ensures that FashionCo can maintain internal consistency across product families. For example, a formal shirt should always be paired with formal pants, not with pants from casual wear. This consistency ensures that related products are always used together, making the system more predictable and easier to manage. <br>

&nbsp; **2. Flexibility for Expansion:**  <br>
The Abstract Factory pattern allows FashionCo to easily add new clothing lines, such as Luxury or Streetwear, by simply creating a new factory for each line. This can be done without disrupting existing lines. Since the client interacts through the main factory, it remains unaware of the specific factories behind each clothing line. This provides flexibility for future growth without requiring changes to the client code. <br>

&nbsp; **3. Separation of Concerns:** <br>
The Abstract Factory pattern helps FashionCo separate the business logic of different clothing lines into individual factories. Each factory is responsible for creating the specific products for one clothing line (e.g., casual, formal, or sportswear). This separation means changes made to one clothing line won't affect  others, making the system more maintainable.<br>

### Reasons for not choosing Factory pattern

&nbsp; **1. Lack of grouping of Product Families:** <br>
Factory pattern is best suitable for creating single type of object (can be either shirt or trouser). It doesn't support creating families of related products. In scenarios where grouping of related objects are required (client needs formal shirt and formal trouser), then abstract factory pattern is best. In scenarios where grouping is not required (client needs formal shirt and casual shirt), then factory pattern is best. <br>

&nbsp; **2. Violation of Open/Close Principle:** <br>
According to Open/Close principle, system should be Open for extension and Close for modification. If factory pattern is used in this scenario, for every new product (for ex: sweaters) introduced, there is a need for modification in existing code. As the scenario is introducing new product families (for ex: streetwear), abstract factory pattern will allow for extension with no modifications required for existing code.

### Intent
The Abstract Factory pattern provides an interface for creating families of related objects without specifying their concrete classes. In this case, FashionCo can create different product families (e.g., formal wear, casual wear) through abstract factories, allowing for easier management of diverse product lines.

### Python Implementation
The Python implementation for this pattern can be found in the [AbstractFactoryPatternImplementation.py](https://github.com/kavya6697/DesignPatternsNotes/blob/f2d8b3729f9ae3c49a74a63e7c66d5617e7a6ff8/Creational%20Design%20Patterns/AbstractFactoryPatternImplementation.py).

### Related Patterns
1. Singleton <br>
2. Prototype <br>
3. Factory Method <br>

### Other Real-world Applicable Scenarios

**BigC Showroom:** A showroom that offers various gadgets from brands like Samsung, Apple, and others. Each brand has different product lines (smartphones, tablets, accessories, etc.) with unique specifications, designs, and features. <br>

### Collaboration & Suggestions 
If you wish to collaborate or suggest any improvements, please feel free to reach out via Mail - ramisetty.kavya06@gmail.com
