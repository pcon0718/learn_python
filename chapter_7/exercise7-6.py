x = 1
print("\nConditional Test")
while x <= 5:
    print(x)
    x += 1

print("\nActive variable")
prompt = "\nType something."
prompt += "\nEnter 'quit' to quit. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

print("\nUsing break")
prompt = "\nWhat is your name?"
prompt += "\nEnter 'quit' to quit. "

while True:
    name = input(prompt)
    if name == 'quit':
        break
    else:
        print(f"Hello {name.title()}.")

