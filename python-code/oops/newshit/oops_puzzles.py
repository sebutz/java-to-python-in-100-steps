'''
-- self is mandatory
you need to have on a constructor
or instance method self
or at least some parameter with the same meaning
'''


class Country:
    '''
    you cannot overload constructors
    there is no such a concept as overloading
    - when the compiler sees the same name
    for a method, removes the old one
    -- the only way 'to emulate' overloading
    is to use default values for parameters
    '''

    # def __init__(self):
    #     print('constructor')

    def __init__(self, name="Default"):
        self.name = name

    def instance_method(self):
        print("instance method")


pakistan = Country()
india = Country("India")

print(india.name)
print(pakistan.name)

india.instance_method()
pakistan.instance_method()


class Country2:
    def __init__(this):
        print('constructor')

    def instance_method(this):
        print("instance method")


romania = Country2()
print(romania)
