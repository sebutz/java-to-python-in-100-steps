
number1 = 12
number2 = 23

print(type(number1))  # int
print(type(number2))   # int
print(type(number1/ number2))   # always float

# if you want integer

print(number1 // number2)   # 0
print(type(number1 // number2))  # int


#power

print(5 ** 3)
print(pow(5, 3))

# there is no  ++, --

number1 += 1
number1 = number1 -1

print(max(2, 4, 3))
print(round(5.654545, 3))  # 5.655
print(round(5.65))  # 6


# boolean operators: and , or , not and ^ (xor)
# are the short-circuit operators (like &&, ||)
# remember ^ is False when both operands are the same

isDone = True

isGray = False

print(isDone and isGray)

print(not isDone)

print(isDone or isGray)

print(isDone ^ isGray)





