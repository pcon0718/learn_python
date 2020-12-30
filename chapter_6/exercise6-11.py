cities = {
    'san diego': {
        'country': 'united states',
        'population': 1423851,
        'fact': 'produces the most avocados',
    },
    'paris': {
        'country': 'france',
        'population': 2187526,
        'fact': 'has over 470,000 trees',
    },
    'sydney': {
        'country': 'austrailia',
        'population': 5312163,
        'fact': 'has koalas',
    },
    
}

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    fact = city_info['fact']

    print(f"\n{city.title()} is located in {country.title()}.")
    print(f"It has a population of: {population}.")
    print(f"Fun fact: It {fact}.")