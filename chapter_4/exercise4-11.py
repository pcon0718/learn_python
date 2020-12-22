pizzas = ['cheese', 'supreme', 'pepperoni']
for pizza in pizzas:
    print(f"I like {pizza} pizza.")

print("Pizza is one of my favorite foods!")
pizzas.append('veggie')

friend_pizzas = pizzas[:]
friend_pizzas.append('sausage')
print("\nMy favorite pizzas are:")
print(pizzas)
print("\nMy friend's favorite pizzas are:")
print(friend_pizzas)
