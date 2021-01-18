sandwiches = ['club', 'blt', 'tuna', 'meatball']
finished_sandwiches = []

while sandwiches:
    working_sandwich = sandwiches.pop()
    print(f"I made your {working_sandwich} sandwich.")
    finished_sandwiches.append(working_sandwich)

for finished_sandwich in finished_sandwiches:
    print(f"Did you enjoy your {finished_sandwich} sandwich?")