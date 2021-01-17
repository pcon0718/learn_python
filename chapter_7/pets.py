pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets: # While there are any entries of 'cat' in the pets dictionary...
    pets.remove('cat')

print(pets)
