# Make empty list to store people in
people = []

person_1 = {
    "first_name": 'james',
    'last_name': 'kirk',
    'age': '32',
    'city': 'riverside',
}

people.append(person_1)

person_2 = {
    "first_name": 'montgomery',
    'last_name': 'scott',
    'age': '43',
    'city': 'aberdeen',
}

people.append(person_2)

person_3 = {
    "first_name": 'leonard',
    'last_name': 'mccoy',
    'age': '39',
    'city': 'atlanta',
}

people.append(person_3)

for person in people:
    print(f"Name: {person['first_name'].title()} {person['last_name'].title()}")
    print(f"Age: {person['age']}")
    print(f"City of Residence: {person['city'].title()}\n")
