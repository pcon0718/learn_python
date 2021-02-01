class Resturaunt:
    """An attempt to represent a Resturaunt"""

    def __init__(self, resturaunt_name, cuisine_type):
        """Initialize attributes to describe the resturaunt"""
        self.resturaunt_name = resturaunt_name
        self.cuisine_type = cuisine_type

    def describe_resturaunt(self):
        """Give the resturaunt name and it's cuisine"""
        print(f"\n{self.resturaunt_name.title()} serves {self.cuisine_type.title()}.")
    
    def open_resturaunt(self):
        """Simulate opening the resturaunt"""
        print(f"The {self.resturaunt_name.title()} is open for business.")

resturaunt1 = Resturaunt('Olive Garden', 'Italian')
resturaunt2 = Resturaunt('sizzler', 'american')
resturaunt3 = Resturaunt('albertos', 'mexican')

resturaunt1.describe_resturaunt()
resturaunt1.open_resturaunt()
resturaunt2.describe_resturaunt()
resturaunt2.open_resturaunt()
resturaunt3.describe_resturaunt()
resturaunt3.open_resturaunt()