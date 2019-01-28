class Book_:
    '''
     some class
    '''
    pass


book1 = Book_()
print(book1)


class Book:
    '''
    this is the constructor for a Book object
    '''

    def __init__(self, name, copies):
        self.name = name
        self.copies = copies

    '''
    this is toString representation of an object
    of type Book
    '''

    def __repr__(self):
        return repr((self.name, self.copies))  # canonical representation


book2 = Book("Also sprache", 1200)
book3 = Book("Mastering masters", 12300)
print(book2)
print(book3)

'''
<__main__.Book_ object at 0x10328e550>
'Also sprache'
'''

