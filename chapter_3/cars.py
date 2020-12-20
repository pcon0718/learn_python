cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() # Permanently sorts list.
print(cars)
print()

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("Here is the list sorted:")
print(sorted(cars)) # Temporarily sort the list
print("Here is the original list again:")
print(cars)
print()

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
cars.reverse() # Permantently reverse sort the list
print(cars)
print()

length = len(cars)
print(f"There are {length} cars in the list")
