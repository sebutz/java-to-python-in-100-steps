''''
 Student(college, year) IS A Person(name, address)
'''


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __repr__(self):
        return repr((self.name, self.address))


# wrong way
# there is no possible way to initialize
# the inner Person
class BadStudent(Person):
    def __init__(self, college, year):
        self.college = college
        self.year = year

    def __repr__(self):
        return repr((super().__repr__(),
                     self.college, self.year))


class GoodStudent(Person):
    def __init__(self, name, address, college, year):
        super().__init__(name, address)
        self.college = college
        self.year = year

    def __repr__(self):
        return repr((super().__repr__(),
                    self.college, self.year))


person = Person("Koko", "15th FLowers")
print(person)
# badStudent = BadStudent("Allambury", 2018)
# print(badStudent)
# print(badStudent.name)
#     print(student.name
#     #AttributeError: 'Student' object has no attribute 'name'

goodStudent = GoodStudent("John", "123 A", "Oxford", 2016)
print(goodStudent)
print(goodStudent.name)
