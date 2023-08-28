
def func(city, country, population=0):
    if population != 0:
        return f"{city}, {country} - Population: {population}".title()
    else: 
        return f"{city}, {country}"