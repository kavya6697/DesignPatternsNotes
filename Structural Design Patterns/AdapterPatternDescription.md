# Adapter Design Pattern

## Scenario: Image Format Converter

### Problem Statement
Rahul is submitting an online application form and faces an issue with the image format. His image is saved in PNG format, but the application form requires the image to be in JPEG format. He wants the application form to accept images in any format and convert them to the required format (JPEG). <br>

**As a software architect, what design pattern would you suggest to satisfy this requirement?**

### Motivation for choosing Adapter Pattern

&nbsp; **1. Compatibility with Legacy Code:** <br>
The Adapter Pattern helps support multiple image formats without modifying the underlying system code. This ensures that the system can handle new formats (like PNG or other formats) without altering its core logic, maintaining backward compatibility.<br>

&nbsp; **2. Decoupling Interfaces:**  <br>
If the existing system is complex, directly modifying it to support additional features (like handling multiple image formats) could be risky. The Adapter Pattern acts as an intermediary layer, decoupling the new format (e.g., JPEG) from the existing system, which only understands PNG. This reduces the risk of breaking existing functionality and provides a cleaner, more maintainable solution. <br>

&nbsp; **3. Preserving the Open/Closed Principle:** <br>
The Adapter Pattern preserves the Open/Closed Principle: the system is closed for modification (you don't need to change the core image processing code) but open for extension (you can easily introduce new adapters for other formats, like PNG, GIF, etc.). This results in more scalable and flexible code. <br>

### Intent
Convert the interface of a class into another interface that clients expect. The Adapter allows classes to communicate smoothly that otherwise would not due to incompatible interfaces.

### Python Implementation
The Python implementation for this pattern can be found in the [AdapterPatternImplementation.py](https://github.com/kavya6697/DesignPatternsNotes/blob/main/Structural%20Design%20Patterns/AdapterPatternImplementation.py).

### Related Patterns
1. Bridge <br>
2. Decorator <br>
3. Proxy <br>

### Other Real-world Applicable Scenarios

**Laptop Charger:** The adapter in a laptop charger converts the power from the wall socket into the appropriate voltage and current levels that the laptop can use. This allows laptops with different power requirements to be charged using a universal charger.<br>

### Collaboration & Suggestions 
If you wish to collaborate or suggest any improvements, please feel free to reach out via Mail - ramisetty.kavya06@gmail.com
