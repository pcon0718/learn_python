class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over in response to a  command."""
        print(f"{self.name} rolled over!")

mydog = Dog('Henry', 10)
yourdog = Dog('Lucy', 3)

print(f"My dog's name is {mydog.name}.")
print(f"My dog's age is {mydog.age}.")
mydog.sit()
mydog.roll_over()

print(f"My dog's name is {yourdog.name}.")
print(f"My dog's age is {yourdog.age}.")
yourdog.sit()
yourdog.roll_over()