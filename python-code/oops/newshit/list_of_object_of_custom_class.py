# list of custom class objects

from operator import attrgetter

class Country:

    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area


    def __repr__(self):
        return repr((self.name, self.population, self.area))


countries = [Country('India', 1200, 100),
             Country('China', 1400, 200),
             Country('USA', 120, 300)]

print(countries)

countries.append(Country("Russia", 133, 344))

print(countries)


# countries.sort()
#TypeError: '<' not supported between instances of 'Country' and 'Country'

print(countries)
countries.sort(key = attrgetter('population'))
print(countries)


# reverse = True

countries.sort(key = attrgetter('area'), reverse = True)
print('countries by area reversed', countries)



# find the counry with the biggest population 

print(max(countries, key=attrgetter('population')))

# find the country with the snallest area 

print(min(countries, key = attrgetter('area')))
