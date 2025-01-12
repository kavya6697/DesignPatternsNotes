### Composite Design Pattern

### Scenario: Organization Restructuring

from abc import ABC, abstractmethod

# Component: Employee (Abstract)
class Employee(ABC):
    @abstractmethod
    def get_details(self):
        pass
    
    @abstractmethod
    def add(self, employee):
        pass
    
    @abstractmethod
    def remove(self, employee):
        pass

# Leaf: Employee (Individual Employee)
class IndividualEmployee(Employee):
    def __init__(self, name, role):
        self.name = name
        self.role = role
    
    def get_details(self):
        print(f"Employee: {self.name}, Role: {self.role}")
    
    def add(self, employee):
        print("Cannot add to an individual employee.")
    
    def remove(self, employee):
        print("Cannot remove from an individual employee.")

# Composite: Manager (Manages Employees or Other Managers)
class Manager(Employee):
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.subordinates = []
    
    def get_details(self):
        print(f"Manager: {self.name}, Role: {self.role}")
        for subordinate in self.subordinates:
            subordinate.get_details()
    
    def add(self, employee):
        self.subordinates.append(employee)
    
    def remove(self, employee):
        self.subordinates.remove(employee)

# Creating Employees
developer1 = IndividualEmployee("John", "Developer")
developer2 = IndividualEmployee("Alice", "Developer")
designer = IndividualEmployee("Bob", "Designer")

# Creating Managers
manager1 = Manager("David", "Team Leader")
manager2 = Manager("Eve", "Engineering Manager")
ceo = Manager("Charlie", "CEO")

# Adding employees to managers
manager1.add(developer1)
manager2.add(developer2)
manager2.add(designer)

# CEO managing both managers
ceo.add(manager1)
ceo.add(manager2)

# Displaying the organization hierarchy
print("Organization Hierarchy:")
ceo.get_details()

# Restructuring: Move developer1 from manager1 to manager2
print("\nRestructuring: Moving Developer John to Engineering Manager Eve's team.")
manager1.remove(developer1)
manager2.add(developer1)

# Displaying the updated hierarchy
print("\nUpdated Organization Hierarchy:")
ceo.get_details()

# Restructuring: Promoting Bob (Designer) to Manager
print("\nRestructuring: Promoting Bob to Manager.")
manager3 = Manager("Bob", "Design Manager")
manager3.add(designer)
ceo.add(manager3)

# Displaying the final hierarchy
print("\nFinal Organization Hierarchy after Promotion:")
ceo.get_details()


### Expected Output
# Organization Hierarchy:
# Manager: Charlie, Role: CEO
# Manager: David, Role: Team Leader
# Employee: John, Role: Developer
# Manager: Eve, Role: Engineering Manager
# Employee: Alice, Role: Developer
# Employee: Bob, Role: Designer

# Restructuring: Moving Developer John to Engineering Manager Eve's team.

# Updated Organization Hierarchy:
# Manager: Charlie, Role: CEO
# Manager: David, Role: Team Leader
# Manager: Eve, Role: Engineering Manager
# Employee: Alice, Role: Developer
# Employee: Bob, Role: Designer
# Employee: John, Role: Developer

# Restructuring: Promoting Bob to Manager.

# Final Organization Hierarchy after Promotion:
# Manager: Charlie, Role: CEO
# Manager: David, Role: Team Leader
# Manager: Eve, Role: Engineering Manager
# Employee: Alice, Role: Developer
# Employee: Bob, Role: Designer
# Employee: John, Role: Developer
# Manager: Bob, Role: Design Manager
# Employee: Bob, Role: Designer