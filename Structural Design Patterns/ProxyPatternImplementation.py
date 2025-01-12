### Proxy Design Pattern 

### Scenario: Remote Service Access

from abc import ABC, abstractmethod
import time

# Step 1: Define the RealService class (the remote service).
class RemoteCustomerService:
    def get_customer_data(self, customer_id: str) -> str:
        # Simulate a time-consuming network request to the remote server
        print(f"Fetching data for customer {customer_id} from the remote server...")
        time.sleep(2)  # Simulate network delay
        return f"Customer {customer_id} data from remote server"

# Step 2: Define the Proxy class
class CustomerServiceProxy:
    def __init__(self):
        self._real_service = None
        self._cached_data = None
        self._is_authenticated = False

    def authenticate(self, user_id: str, password: str):
        # Simple authentication check (for demo purposes)
        if user_id == "admin" and password == "password123":
            self._is_authenticated = True
            print("Authentication successful.")
        else:
            self._is_authenticated = False
            print("Authentication failed.")
    
    def get_customer_data(self, customer_id: str) -> str:
        if not self._is_authenticated:
            raise PermissionError("User is not authenticated!")
        
        if self._cached_data is None:
            if not self._real_service:
                self._real_service = RemoteCustomerService()
            # Fetch the data only if it's not cached
            self._cached_data = self._real_service.get_customer_data(customer_id)
        else:
            print("Returning cached data...")
        
        return self._cached_data

# Step 3: Demonstrate the use of Proxy

# Create a proxy object
proxy = CustomerServiceProxy()

# Authenticate user
proxy.authenticate(user_id="admin", password="password123")

# Fetch customer data using the proxy (first request will go to the real service)
print(proxy.get_customer_data("123"))

# Fetch customer data again (this time, it should be served from the cache)
print(proxy.get_customer_data("123"))

# Try fetching data with an unauthenticated user
try:
    proxy.authenticate(user_id="user", password="wrongpassword")
    print(proxy.get_customer_data("456"))
except PermissionError as e:
    print(e)


### Expected Output
# Authentication successful.
# Fetching data for customer 123 from the remote server...
# Customer 123 data from remote server
# Returning cached data...
# Customer 123 data from remote server
# Authentication failed.
# User is not authenticated!