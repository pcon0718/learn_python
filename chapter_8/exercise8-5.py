def describe_city(city, country = 'united states'):
    print(f"\nThe city of {city.title()} is located in {country.title()}.")

describe_city('san diego')
describe_city('austin')
describe_city(city='paris', country='france')
