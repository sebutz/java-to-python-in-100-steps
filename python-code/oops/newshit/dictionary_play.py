
# dictionary

# key-value pairs


{'a': 5, 'b': 6, 'c': 3}

# how to produce it 
occurances = dict(a=5,  b=6, c= 3)
print(occurances)


print(occurances.keys)
for key in occurances.keys():
	print(key)

# access an element
print(occurances['a'])


# access un-safely
# print(occurances['w'])  # KeyError: 'w'

# access safely (type safe)

print(occurances.get('w')) # None
print(occurances.get('a')) # 5

# more, we can provide a default value if we not find the key

print(occurances.get('w', 0)) # 0




# dismember a dictionary into pieces


# items
print(occurances.items()) # dict_items([('a', 5), ('b', 6), ('c', 3)])
print(type(occurances.items())) # <class 'dict_items'>


for item in occurances.items():
	print(item)
	print(type(item))  #  <class 'tuple'>




print(occurances.keys())  # dict_keys(['a', 'b', 'c'])
print(type(occurances.keys()))  # <class 'dict_keys'>



print(occurances.values())   # dict_values([5, 6, 3])
print(type(occurances.values())) # <class 'dict_values'>




# access directly by items (tuples)
for (key, value) in occurances.items():
	print("key:",key, "value:", value) 

'''
key: a value: 5
key: b value: 6
key: c value: 3

'''


# update a dictionary

occurances['a'] = 100
print(occurances.get('a')) # 100
print(occurances)




# delete from dictionary

print('before deleting', occurances)
del occurances['a']
print('after deleting', occurances)

'''
before deleting {'a': 100, 'b': 6, 'c': 3}
after deleting {'b': 6, 'c': 3}

'''

# adding am element
occurances['e'] = 500
print(occurances) # {'b': 6, 'c': 3, 'e': 500}







