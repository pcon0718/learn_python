number = input("Give me a number, and I will let you know if it is a multiple of 10. ")
number = int(number) # Covert string to integer
result = number % 10
if result == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is NOT a multiple of 10.")
