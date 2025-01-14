### Chain Of Responsibility

### Scenario: Customer Support System

class SupportHandler:
    """Abstract handler class in the chain of responsibility."""
    
    def __init__(self):
        self.next_handler = None
    
    def set_next_handler(self, handler):
        """Sets the next handler in the chain."""
        self.next_handler = handler
        return handler
    
    def handle_request(self, request):
        """Abstract method to be overridden by concrete handlers."""
        if self.next_handler:
            self.next_handler.handle_request(request)


class FrontDeskHandler(SupportHandler):
    """Handles general inquiries or forwards to the next handler."""
    
    def handle_request(self, request):
        if request.issue_type == "General Inquiry":
            print(f"Front Desk: Handling general inquiry: {request.issue}")
        else:
            print("Front Desk: Cannot handle, passing to next handler.")
            super().handle_request(request)


class BillingHandler(SupportHandler):
    """Handles billing-related issues."""
    
    def handle_request(self, request):
        if request.issue_type == "Billing":
            print(f"Billing Department: Handling billing issue: {request.issue}")
        else:
            print("Billing Department: Cannot handle, passing to next handler.")
            super().handle_request(request)


class TechnicalSupportHandler(SupportHandler):
    """Handles technical issues."""
    
    def handle_request(self, request):
        if request.issue_type == "Technical Support":
            print(f"Technical Support: Handling technical issue: {request.issue}")
        else:
            print("Technical Support: Cannot handle, passing to next handler.")
            super().handle_request(request)


class ManagerHandler(SupportHandler):
    """Handles escalated or complex issues."""
    
    def handle_request(self, request):
        print(f"Manager: Handling escalated issue: {request.issue}")


class SupportRequest:
    """Class representing a customer support request."""
    
    def __init__(self, issue_type, issue):
        self.issue_type = issue_type
        self.issue = issue


# Example usage:

# Create request objects
request1 = SupportRequest("General Inquiry", "What are your working hours?")
request2 = SupportRequest("Billing", "I have a question about my last bill.")
request3 = SupportRequest("Technical Support", "My account is not working.")
request4 = SupportRequest("Billing", "I need a refund for a double charge.")
request5 = SupportRequest("Technical Support", "My device is not syncing.")

# Create handlers
front_desk = FrontDeskHandler()
billing = BillingHandler()
tech_support = TechnicalSupportHandler()
manager = ManagerHandler()

# Set up the chain
front_desk.set_next_handler(billing).set_next_handler(tech_support).set_next_handler(manager)

# Process requests through the chain
print("\nProcessing request 1:")
front_desk.handle_request(request1)

print("\nProcessing request 2:")
front_desk.handle_request(request2)

print("\nProcessing request 3:")
front_desk.handle_request(request3)

print("\nProcessing request 4:")
front_desk.handle_request(request4)

print("\nProcessing request 5:")
front_desk.handle_request(request5)

### Expected Output
# Processing request 1:
# Front Desk: Handling general inquiry: What are your working hours?

# Processing request 2:
# Front Desk: Cannot handle, passing to next handler.
# Billing Department: Handling billing issue: I have a question about my last bill.

# Processing request 3:
# Front Desk: Cannot handle, passing to next handler.
# Billing Department: Cannot handle, passing to next handler.
# Technical Support: Handling technical issue: My account is not working.

# Processing request 4:
# Front Desk: Cannot handle, passing to next handler.
# Billing Department: Handling billing issue: I need a refund for a double charge.

# Processing request 5:
# Front Desk: Cannot handle, passing to next handler.
# Billing Department: Cannot handle, passing to next handler.
# Technical Support: Handling technical issue: My device is not syncing.