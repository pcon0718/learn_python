number = input("How many people for dinner today? ")
number = int(number)

if number > 8:
    print(f"You will have to wait for a table.")
else:
    print(f"Right this way.")