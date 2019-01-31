

import random

print(random.random())

print(random.randint(1, 49))  # [1 ,..., 49]  all the extremes are reachable


# odd numbers
print(random.randrange(1, 25, 2))

# multiple of 3
print(random.randrange(1, 30, 3))

list = [2, 7, 9, 34, 56]
print(random.choice(list))


print(random.choice("asasdas adasdwgsfg "))

# randomly pick up 2 values
print(random.sample(list, 2))

