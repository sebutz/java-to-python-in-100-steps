marks = [23, 13, 23]

marks.append(23)
print(len(marks))

# adding elements

# by value (on the last place
print("before adding element to a list: ", marks)
marks.append(23)
print(len(marks))
print("after adding element to a list: ", marks)


# by index and value
marks.insert(0, 10)
print(marks)
marks.insert(0, 12)
print(marks)


# extend : add more elements at once
# basically it's about the content of another list
# which is extending curremt list
# we need to pass as a parameter the list used for extension

print("before extending a list: ", marks)
marks.extend([344, 455, 566])
print("after extending a list: ", marks)

# obs: string can be seen as a list
marks.extend('123')
# the same as marks.extend(['1', '2', '3'])


# same as extent but using + operator
print("before adding to a list: ", marks)
marks = marks + [0, 111]
print("after adding to a list: ", marks)


animals = ['Cat', 'Dog', 'Elephant']
print(animals)
print(len(animals))


# removing elements from a list
# animals.remove('Doggie')  #ValueError: list.remove(x): x not in list

# removing by value
print("before removing by value:", animals)
animals.remove('Dog')
print("after removing by value:", animals)


# removing by index
animals.append('Crocodile')
print("before removing by index:", animals)
del animals[2]
print("after removing by index:", animals)
# del animals[5] # IndexError: list assignment index out of range
