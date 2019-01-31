# filter, map and reduce
from functools import reduce

numbers = [3, 7, 8, 15, 24, 35, 46]
res1 = list(filter(lambda x: x % 2 == 0, numbers))
print(res1)

res2 = list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, numbers)))
print(res2)

res3 = sum(map(lambda x: x * x, filter(lambda x: x % 2 == 0, numbers)))
print(res3)

res4 = reduce(lambda x, y: x + y, map(lambda x: x * x, filter(lambda x: x % 2 == 0, numbers)))
print(res4)

months = [('Jan', 31), ('Feb', 28), ('Mar', 31)]

# how to access elements of a tuple
tuple_ex = ('Dec', 31)
print(tuple_ex[0])
print(tuple_ex[1])

# total number of days
res4 = sum(map(lambda x: x[1], months))

res5 = reduce(lambda x, y: x if x[1] < y[1] else y, months)
print(res5)

# directly
res6 = reduce(lambda x, y: x if x[1] < y[1] else y, months)[0]
print(res6)
