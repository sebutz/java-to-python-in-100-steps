
# lists slicing
numbers = ['Zero', 'One', 'Three', 'Four', 'Five', 'Six',
'Seven', 'Eight', 'Nine', 'Ten']
bak_numbers = numbers

# [:] ----> [ , )

print(numbers[2])
print(numbers[:2]) # from the beginning
print(numbers[2:]) # til the end


print(numbers[2:4])   # aka [numbers[2], numbers[3]]


# stepping
print(numbers[0:10:2]) # step 2 
print(numbers[0:10:3]) # step 3

print(numbers[::3]) # from the beginning til the end with step 3
print(numbers[::]) # all the crap


# how to reverse a list

# 1 in place, affecting the structure of the list
print('before reversing: ', numbers)
numbers.reverse()
print('after reversing: ', numbers)


# 2 
# reverse back 
numbers.reverse()
print("back to normal: ", numbers)
print(numbers[::-1])



# delete with slicing

# delete from 3 until the end
numbers = [ number for number in bak_numbers]
print("some ids: old: ", id(numbers), 'bak:', id(bak_numbers))
print('back to normal again: ', numbers)

print("before delete: ", numbers)
del numbers[3:]
print("after delete", numbers)
print(len(numbers)) # 3
print('the backup is: ', bak_numbers)


# you can even replace values in the list with list slicing
numbers = bak_numbers
print('back to normal:', numbers)
print('before replacing elements in the list:', numbers)
numbers[3:6] = [1001, 1002, 1003]
print('after replacing elements in the list:', numbers)



'''
Three
['Zero', 'One']
['Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
['Three', 'Four']
['Zero', 'Three', 'Five', 'Seven', 'Nine']
['Zero', 'Four', 'Seven', 'Ten']
['Zero', 'Four', 'Seven', 'Ten']
['Zero', 'One', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
before reversing:  ['Zero', 'One', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
after reversing:  ['Ten', 'Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'One', 'Zero']
back to normal:  ['Zero', 'One', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
['Ten', 'Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'One', 'Zero']
some ids: old:  4385139912 bak: 4385136904
back to normal again:  ['Zero', 'One', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
before delete:  ['Zero', 'One', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
after delete ['Zero', 'One', 'Three']
3
the backup is:  ['Zero', 'One', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
back to normal: ['Zero', 'One', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
before replacing elements in the list: ['Zero', 'One', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
after replacing elements in the list: ['Zero', 'One', 'Three', 1001, 1002, 1003, 'Seven', 'Eight', 'Nine', 'Ten']
[Finished in 0.4s]
'''
