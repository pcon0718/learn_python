dream_vacations = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    dream_vacation = input("\nIf you could visit one place in the world, where would you go? ")

    # Store the response in the dictionary
    dream_vacations[name] = dream_vacation

    repeat = input("Does anyone else want to answer? (yes/no) ")
    if repeat == 'no':
        polling_active = False
    
print("\n--- Survey Results ---")
for name, dream_vacation in dream_vacations.items():
    print(f"{name.title()} would like to visit {dream_vacation.title()}.")