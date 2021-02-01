class User:
    """An attempt to represent a user."""
    def __init__(self, first_name, last_name, user_age, user_hair_color):
        """Initialize attribute to describe a user"""
        self.first_name = first_name
        self.last_name = last_name
        self.user_age = user_age
        self.user_hair_color = user_hair_color
    
    def describe_user(self):
        """Print Summary of user info"""
        print(f"\nFirst Name: {self.first_name.title()}")
        print(f"Last Name: {self.last_name.title()}")
        print(f"User's Age: {self.user_age}")
        print(f"User's Hair Color: {self.user_hair_color.title()}")
    
    def greet_user(self):
        """Greet the user."""
        print(f"Greetings {self.first_name.title()}!")

user1 = User('henry', 'thomas', 5, 'blonde')

user1.describe_user()
user1.greet_user()
