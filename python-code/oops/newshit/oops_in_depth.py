class Planet:
    def __init__(self, name, distance_from_sun):
        self.name = name
        self.distance_from_sun = distance_from_sun


earth = Planet("Earth", 200)
mars = Planet("Mars", 500)

'''
dynamically add instance attributes 
PARTICULAR TO AN INSTANCE !!!! 
'''
earth.name = "Earth"
print(earth.name)

earth.speed = 10000
print(earth.speed)

# print(mars.speed)
'''
print(mars.speed)
AttributeError: 'Planet' object has no attribute 'speed'
'''

# an object is just a HashMap (dictionary)
# you can add attributes and values





