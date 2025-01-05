### Prototype Design Pattern - Python Implementation

### Scenario: Icon Design

## for clone operation
import copy

# Base prototype class
class Icon:
    def clone(self):
        return copy.deepcopy(self)

# Concrete prototype class for a specific icon type
class ConcreteIcon(Icon):
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

    def display(self):
        print(f"Icon: {self.name}, Color: {self.color}, Size: {self.size}")

# Client code to demonstrate the Prototype Pattern
def main():
    # Create the base icon prototype
    base_icon = ConcreteIcon("Base Icon", "Blue", "32x32")
    
    # Clone the base icon and modify the clone
    icon_clone1 = base_icon.clone()
    icon_clone1.color = "Red"
    icon_clone1.display()  # Modified clone with a different color

    icon_clone2 = base_icon.clone()
    icon_clone2.size = "64x64"
    icon_clone2.display()  # Modified clone with a different size
    
    # Another clone with different modifications
    icon_clone3 = base_icon.clone()
    icon_clone3.name = "New Icon"
    icon_clone3.color = "Green"
    icon_clone3.size = "48x48"
    icon_clone3.display()  # Modified clone with new name, color, and size

# Run the example
if __name__ == "__main__":
    main()

### Expected Output
# Icon: Base Icon, Color: Red, Size: 32x32
# Icon: Base Icon, Color: Blue, Size: 64x64
# Icon: New Icon, Color: Green, Size: 48x48