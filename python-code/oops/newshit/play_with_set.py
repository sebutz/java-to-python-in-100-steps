
# SETS
# set are not indexed 




# list can contain duplicates
# list is a positional thing

numbers = [1, 2, 3, 1, 3, 6, 7, 1]
print(numbers)



# what if we don't want duplicates
numbers_set = set(numbers)
print(numbers_set)


# even if we add existing elements, they will mnot be added
numbers_set.add(3)
print(numbers_set)


# set does not support indexing!!!

# only some appartenence:

print(2 in numbers_set)

'''
[1, 2, 3, 1, 3, 6, 7, 1]
{1, 2, 3, 6, 7}
{1, 2, 3, 6, 7}
True
'''


# we can have min, max, len
print(min(numbers_set))
print(max(numbers_set))
print(len(numbers_set))

'''
1
3
3
'''



numbers_1_to_5_set = set(range(1, 6)) # [)
print(numbers_1_to_5_set)
numbers_4_to_10_set = set(range(4, 11)) # [)
print(numbers_4_to_10_set)


'''
{1, 2, 3, 4, 5}
{4, 5, 6, 7, 8, 9, 10}
'''


# set OPERATIONS !!!
# union (use pipe | operator)

# numbers_1_to_5_set  + numbers_4_to_10_set 
# TypeError: unsupported operand type(s) for +: 'set' and 'set'

numbers_union = numbers_1_to_5_set | numbers_4_to_10_set
print(numbers_union)
'''
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
'''

# intersection (common elements)
numbers_common = numbers_1_to_5_set & numbers_4_to_10_set
print(numbers_common)
'''
{4, 5}
'''


# what is only in one set and not in the oher   A \ B
numbers_1_to_5_set_only = numbers_1_to_5_set - numbers_4_to_10_set
print(numbers_1_to_5_set_only) # {1, 2, 3}


# B \ A
numbers_4_to_10_set_only = numbers_4_to_10_set - numbers_1_to_5_set
print(numbers_4_to_10_set_only)








