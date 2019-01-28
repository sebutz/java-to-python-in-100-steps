class Planet:
    pass


earth = Planet()
mars = Planet()

'''
dynamically add instance attributes 
PARTICULAR TO AN INSTANCE !!!! 
'''
earth.name = "Earth"
print(earth.name)

earth.speed = 10000
print(earth.speed)

# print(mars.name)
'''
print(mars.name)
AttributeError: 'Planet' object has no attribute 'name'
'''





