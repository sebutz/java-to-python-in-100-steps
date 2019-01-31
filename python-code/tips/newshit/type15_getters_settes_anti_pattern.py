# there are no private, protected variables in Python


class BookEnhanced:
    def __init__(self, name, copies):
        self.name = name
        self.copies = copies

    def __repr__(self):
        return repr((self.name, self.copies))


book1 = BookEnhanced("Catcher in the rye", 1000)
print(book1)
book1.copies = 10

print(book1)

'''
('Catcher in the rye', 1000)
('Catcher in the rye', 10)
'''


# problem of validation of the value for the fields,
# without modifying client code can be done with the help of property decorators

class Bookie:
    def __init__(self, name, copies):
        self.name = name
        self._copies = copies

    # that will be a getter
    @property
    def copies(self):
        print('getter called')
        return self._copies  # just a convention: you should not use this value directly (in fact is possible)

    # that will be some kind of setter
    @copies.setter
    def copies(self, copies):
        print("setter is called")
        if copies >= 0:
            self._copies = copies

    def __repr__(self):
        return repr((self.name, self.copies))


bookie = Bookie("The three knights", 1000)
print("copies:", bookie.copies)
print(f"bookie= {bookie}")

'''
getter called
copies: 1000
getter called
bookie= ('The three knights', 1000)
'''


bookie.copies = 2000  # setter is called
print(f"bookie={bookie}")

'''
setter is called
getter called
bookie=('The three knights', 2000)
'''

#  cannot modify
bookie.copies = -200
print(f"bookie={bookie}")

'''
setter is called
getter called
bookie=('The three knights', 2000)
'''