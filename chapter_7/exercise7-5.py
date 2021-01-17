prompt = "\nWhat is your age? "
prompt += "Enter 'exit' to exit. e"
while True:
    age = input(prompt)
    if age == 'exit':
        break

    age = int(age) #convert string to int

    if age < 3:
        print("Your admission is free!")
    elif age >= 3 and age < 12:
        print("Your admission is $10.")
    elif age >= 12:
        print("Your admission is $15.")
