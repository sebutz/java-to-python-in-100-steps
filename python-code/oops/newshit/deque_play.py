
# the most efficient implementation of a stack or a queue


from collections import deque

queue = deque(['Zero', 'One', 'Two'])

#  you can get value from the left or from the right


queue.append('Three')
print(queue)


queue.appendleft("Minus one")
print(queue)


'''
deque(['Zero', 'One', 'Two', 'Three'])
deque(['Minus one', 'Zero', 'One', 'Two', 'Three'])
'''


queue.pop()
print(queue)

queue.popleft()
print(queue)

'''
deque(['Minus one', 'Zero', 'One', 'Two'])
deque(['Zero', 'One', 'Two'])
'''