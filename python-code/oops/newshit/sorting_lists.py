# sorting lists

# recap: reverse in place

numbers = ['Zero', 'One', 'Three', 'Four', 'Five', 'Six',
           'Seven', 'Eight', 'Nine', 'Ten']

print(numbers)

numbers.reverse()

print(numbers)

print(numbers.reverse())  # that will be None
print("back to initial state: ", numbers)


# you want a reverse list but to keep the original state untouched
# reversed list: <list_reverseiterator object at 0x108127a90>
dec_numbers = reversed(numbers)
# that will give an iterator and you can traverse the list with it

for number in reversed(numbers):
    print(number)


print("untouched original list:", numbers)

# sorting lists (in place)
print("before sorting:", numbers)
numbers.sort()
print('after sorting:', numbers)


# sort by a key
print("before sorting:", numbers)
numbers.sort(key = len)
print('after sorting:', numbers)



# reverse = True
print("before sorting:", numbers)
numbers.sort(key = len, reverse = True)
print('after sorting:', numbers)


# access the elements in a sorted way but keep the list as it was

print("back to the original list")
numbers = ['Zero', 'One', 'Three', 'Four', 'Five', 'Six',
           'Seven', 'Eight', 'Nine', 'Ten']

for number in sorted(numbers):
    print(number)       


print("the list remained the same:", numbers)        



# pass a key to be sorted by

for number in sorted(numbers, key=len):
	print(number)


 # reverse the order, based by the key
for number in sorted(number, key=len, reverse=True):
 	print(number)






