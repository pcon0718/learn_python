class Resturaunt:
    """An attempt to represent a Resturaunt"""

    def __init__(self, resturaunt_name, cuisine_type):
        """Initialize attributes to describe the resturaunt"""
        self.resturaunt_name = resturaunt_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_resturaunt(self):
        """Give the resturaunt name and it's cuisine"""
        print(f"{self.resturaunt_name.title()} serves {self.cuisine_type.title()}.")
    
    def open_resturaunt(self):
        """Simulate opening the resturaunt"""
        print(f"The {self.resturaunt_name} is open for business.")

    def set_number_served(self, number_served):
        """Simulate the number of people in the resturaunt"""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Simulate incrementing the number of people in the resturaunt"""
        self.number_served += additional_served


resturaunt = Resturaunt('Olive Garden', 'Italian')

resturaunt.describe_resturaunt()
print(f"\nNumber Served: {resturaunt.number_served}.")
resturaunt.number_served = 430
print(f"\nNumber Served: {resturaunt.number_served}.")

resturaunt.set_number_served(1257)
print(f"\nNumber Served: {resturaunt.number_served}.")

resturaunt.increment_number_served(239)
print(f"\nNumber Served: {resturaunt.number_served}.")


