requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

print()
print("Next exercise:\n")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print(f"Sorry we are out of {requested_topping} right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

print("\nNext exercise:\n")

requested_toppings = [] 
if requested_toppings: # If list has items in it, continue.
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
        print("\nFinished making your pizza!")
else: 
    print("Are you sure you want a plain pizza?")

    