# use list as a stack and queue


# STACK : LIFO. : append() + pop
# QUEUE: FIFO


numbers = []

numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
numbers.append(5)


#  []<-[1] <-[1]
#  [1] <- [2] <- [1, 2]

# use pop to extract the last element from a list

print("before pop", numbers)
op_result = numbers.pop()
print("does op return something?", op_result)
print("after pop", numbers)


# look like pop is extracting the last element

print("a list as a stack: LIFO")

# LI : append
print("before append", numbers)
numbers.append(10)
print("after append", numbers)


# FO : pop
print("before pop", numbers)
op_result = numbers.pop()
print("does op return something?", op_result)
print("after pop", numbers)



# QUEUE : FIFO 
# append + pop(0)

numbers = []
numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)


# use pop with index 

print("before pop with index", numbers)
op_result = numbers.pop(0)
print("does op return something?", op_result)
print("after pop with index", numbers)


print("before pop with index", numbers)
op_result = numbers.pop(0)
print("does op return something?", op_result)
print("after pop with index", numbers)




