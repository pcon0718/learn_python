sandwiches = ['club', 'pastrami', 'blt', 'pastrami', 'tuna', 'meatball', 'pastrami']
finished_sandwiches = []

print("There is  no pastrami for sandwiches.")

while 'pastrami' in sandwiches:
    sandwiches.remove('pastrami')

while sandwiches:
    working_sandwich = sandwiches.pop()
    print(f"I made your {working_sandwich} sandwich.")
    finished_sandwiches.append(working_sandwich)

for finished_sandwich in finished_sandwiches:
    print(f"Did you enjoy your {finished_sandwich} sandwich?")