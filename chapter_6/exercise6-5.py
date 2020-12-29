rivers = {
    'nile': 'egypt',
    'mississippi': 'united states',
    'thames': 'england',
}

for river, country in rivers.items():
    print(f"The {river.title()} River runs through the country of {country.title()}")
