str = "This is an awesome occasion. This has never happened before."
squares_first_ten_numbers = [i*i for i in range(1, 11)]

print(type(squares_first_ten_numbers))
squares_first_ten_numbers_set = set(squares_first_ten_numbers)


# set comprehesion !!!
squares_first_ten_numbers_set = {i * i for i in range(1, 11)}
print(squares_first_ten_numbers_set) # {64, 1, 4, 36, 100, 9, 16, 49, 81, 25}

print(type(squares_first_ten_numbers_set)) # <class 'set'>



# dictionary comprehension

squares_first_ten_numbers_dictionary = {i: i * i for i in range(1, 11)}
print(squares_first_ten_numbers_dictionary)
print(type(squares_first_ten_numbers_dictionary))

'''

<class 'list'>
{64, 1, 4, 36, 100, 9, 16, 49, 81, 25}
<class 'set'>
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
<class 'dict'>
'''

print(type({})) # <class 'dict'>
# empty set

print(type(set()))
print(set())


