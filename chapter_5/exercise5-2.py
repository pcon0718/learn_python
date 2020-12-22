## Tests for equality/inequality with strings
car = 'audi'
if car == 'audi':
    print("You have an Audi")
else:
    print("You have another brand of car")

car = 'honda'
if car != 'honda':
    print("You have an unreliable car")
else:
    print("Your car is pretty reliable")

car = 'BMW'
car = car.lower()
if car == 'bmw':
    print("\nYou've got a BMW")

number = 2
if number <= 3:
    print("\nYour number is less than three.")

number = 22
if number > 25 and number < 1000:
    print('You did it')
else:
    print('Your number is pretty low.')

pets = ['dog', 'cat', 'bird', 'fish', 'snake']
if 'lion' in pets:
    print('You have an approved pet')
else:
    print('Your pet is not approved')

pet = 'snake'
if pet not in pets:
    print("Your pet is not approved")
else:
    print("Your pet is welcome here.")

