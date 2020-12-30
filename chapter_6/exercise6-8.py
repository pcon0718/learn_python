pets = []

pet = {
    'kind': 'cat',
    'name': 'travis',
    'owner': 'philippe',
    }

pets.append(pet)

pet = {
    'kind': 'dog',
    'name': 'kegin',
    'owner': 'thomas',
    }

pets.append(pet)

pet = {
    'kind': 'snake',
    'name': 'ace',
    'owner': 'art',
    }

pets.append(pet)

for pet in pets:
    print(f"{pet['name'].title()} is a {pet['kind']}, and is owned by: {pet['owner'].title()}.")