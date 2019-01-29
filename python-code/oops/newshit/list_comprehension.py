# list comprehension


# create a new list containing only elements with 4 characters
numbers = ['Zero', 'One', 'Three', 'Four', 'Five', 'Six',
           'Seven', 'Eight', 'Nine', 'Ten']


numbers_4 = []

for number in numbers:
	if len(number) == 4:
		numbers_4.append(number)


print(numbers_4)



# list comprehension
numbers_all = [number for number in numbers]
print(numbers_all)

numbers_len = [len(number) for number in numbers]
print(numbers_len)


numbers_44 = [number for number in numbers if len(number) == 4]
print(numbers_44)

values = [3, 6, 9, 1, 4, 15, 6, 3]
values_even = [value for value in values if value % 2 == 0] 
print(values_even)

values_odd = [value for value in values if value % 2 != 0] 
print(values_odd)


