# Copy a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("MY favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')

# Prove that lists are separate by adding new items to each list individually
print("MY favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)