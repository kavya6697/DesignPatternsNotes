**------------------------- WORK IN PROGRESS -----------------------------**
# Introduction to Design Patterns
Design pattern is a general repeatable solution to a commonly occurring problem in software design. It is a template about how to solve a problem; same template can be used in many different situations.
Consistency, clarity, time, and reuse are the pros of using design patters, whereas, anti-patterns, careful while choosing the pattern, negative consequences, subjective dependence on concrete scenarios, different interpretations are the cons in using design patterns.

## 15 Facts about Design Patterns
1. Design patterns are different ways to enforce the fundamental design principles.
2. Design patterns (DP) can speed up the development process by providing tested, proven development paradigms.
3. Reusing DP helps to prevent issues that can cause major problems (extensibility).
4. Improves code readability for coders and architects familiar with the patterns.
5. DP provides general solutions demonstrated in a format that does not require specific tie to a particular problem.
6. Patterns allow developers to communicate using well-known and well-understood names of software interactions.
7. Common DP can be improved over time, making them robust than ad-hoc designs.
8. DP use OO Concepts like decomposition, inheritance, and polymorphism to improve software development process.
9. DP provides a way to get benefit from the experience and knowledge of your predecessors those have worked on the same type of project.
10. Appropriate DP used in development of applications make development fast and easy documented.
11. DP are more sophisticated and advance approaches than basic data structures.
12. None of the DP describes anything about new or unproven design changes. They only include designs applied more than once in different systems.
13. DPs are part of the OO-community or DPs are the elements of some successful OO-systems.
14. DPs should be easy to learn for inexperienced developers.
15. DPs are not dealing with designing user interfaces.

## Gang of Four Design Patterns
Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides written a book titled “Design Patterns: Elements of Reusable Object-Oriented Software” in 1994 which consists of 23 design patterns grouped under three categories. Patterns under each category is again sub-divided into either class scope patterns or object scope patterns. Class scope patterns are to be applied during design time, whereas object scope patterns to be applied during runtime. <br>

**1. Creational DP:** Deals with object creation in a defined systematic manner.
* [Factory Method](https://github.com/kavya6697/DesignPatternsNotes/blob/main/Creational%20Design%20Patterns/FactoryMethodPatternDescription.md)
* [Abstract Factory](https://github.com/kavya6697/DesignPatternsNotes/blob/main/Creational%20Design%20Patterns/AbstractFactoryPatternDescription.md)
* [Singleton](https://github.com/kavya6697/DesignPatternsNotes/blob/main/Creational%20Design%20Patterns/SingletonPatternDescription.md)
* [Prototype](https://github.com/kavya6697/DesignPatternsNotes/blob/main/Creational%20Design%20Patterns/PrototypePatternDescription.md)
* [Builder](https://github.com/kavya6697/DesignPatternsNotes/blob/main/Creational%20Design%20Patterns/PrototypePatternDescription.md)
  
**2. Structural DP:** provides a mechanism to organize the classes and objects for larger structures.  <br>

**3. Behavioural DP:** deals with communication between objects.  <br>

## AntiPatterns
Anti-pattern is the knowledge to prevent and recover from common mistakes. It is to deal with the gap between architectural concepts and real-world implementations. It mainly provide negative solutions - Solution that represents more problems than they address. <br>

**Different Viewpoints:** to avoid bad occurrences and for smooth running. Manager viewpoint, architect viewpoint, and developer viewpoint are three major types. <br>

**Applications:**<br>
*Prototype:* file sharing, OS installation<br>
*Singleton:* shopping cart, ID card, OTP, Barcodes<br>
*Builder:* car parts, building<br>

## Generic Guidelines
•	Study the applications of design.<br>
•	Map your application to the design pattern.<br>
•	Study the patterns which has similar solutions.<br>
•	Reusability if you are going to redesign for another solution.<br>
•	Having a wide knowledge about design patterns provide a structure for given pattern.<br>

## Problem-solving by Design patterns:
•	Finding appropriate object<br>
•	Determining object granularity (object can vary in size and number)<br>
•	Specifying object interfaces<br>

## Assume a scenario is given to you in an interview, and asked to choose the best applicable design pattern and why??

### Tips for choosing best design pattern

1. If the scenario is related to grouping of objects, then go with **Abstract Factory Pattern**
2. If the scenario is related to independent object creation with less dependency with client code, then go with **Factory method pattern**
3. If the scenario is related to seperating the construction process from its representation, then go with **Builder pattern**
4. If the scenario is related to cloning existing and modifying, then go with **Prototype pattern**
5. If the scenario is related to creating only one instance, then go with **Singleton pattern**
6. If the scenario is related to changing one form to another, then go with **Adapter pattern**
7. If the scenario is related to adding additional functionalities to base code, then go with **Decorator**
8. If the scenario is related to hiding the complex process, then go with **Facade pattern**
9. 
