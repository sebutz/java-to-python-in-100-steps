# using tuples


def some_function():
    return "aaa", 12, 34.0


print(some_function())
print(type(some_function()))

'''
('aaa', 12, 34.0)
<class 'tuple'>
'''

# access a tuple elements

print(some_function()[0]) # aaa