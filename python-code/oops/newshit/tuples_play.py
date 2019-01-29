

def play_here():
	return "Boom", 123, 23.0

some_tuple = play_here()

print(some_tuple) # ('Boom', 123, 23, 0)
print(type(some_tuple))  # tuple


 # multiple assignments : unpack a tuple

x, y, z = play_here()
print(x);print(y);print(z)

'''
Boom
123
23.0
'''


# tuples got index
print(some_tuple[0]) # Boom


# tuples are immutable
# values in tuples cannot change


#  some_tuple[0] = "AAAA"  # TypeError: 'tuple' object does not support item assignment


# swap with tuples

x = 0
y = 1
x, y = y, x




print(x);print(y)

#it's like 

x =3 ; y = 4
x, y = (y, x) 

print(x);print(y)



# tuple with 1 element
l_tuple = (0, )
ll_tuple = 1, 

print(l_tuple);print(ll_tuple)

'''
(0,)
(1,)
'''


