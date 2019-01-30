# functional programming
# filtering a list
# map method
# reduce


# filter
from functools import reduce

numbers = [1, 89, 54, 35, 2, 200]

filtered_list = list(filter(lambda x: x % 2 == 1, numbers))
print(filtered_list)  # [1, 89, 35]

words = ["Adam", "Ant", "Bernie"]
print(list(filter(lambda x: x.endswith('ie'), words)))  # ['Bernie']

# map
words = ['Apple', 'Ant', 'Bernie']
print(list(map(lambda x: x.upper(), words)))  # ['APPLE', 'ANT', 'BERNIE']

import random

lotto_numbers = list(map(lambda _: round(random.random() * 50), range(1, 7)))
print(lotto_numbers)

# reduce  (from functools import reduce)
print(sum(numbers))  # 381
res = reduce(lambda x, y: x + y, numbers)
print(res)  # 381

print(reduce(lambda x, y: x * y, numbers))

print(reduce(lambda x, y: x if len(x) > len(y) else y, words))  # Bernie
