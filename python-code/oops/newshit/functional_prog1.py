# a function is an object
# lambda way (anonymous, simpler definition of a function)


def multiply_by_2(data):
    return data * 2


print(type(multiply_by_2))  # <class 'function'>


def do_something_and_print(func, data):
    print(func(data))


# it's taking the function as arguments
do_something_and_print(multiply_by_2, 12)  # 24

# we can have reference to that function-object
func_example_ref = multiply_by_2
print(func_example_ref(23))  # 46


# we need to define first the method

def multiply_by_3(data):
    return data * 3


do_something_and_print(multiply_by_3, 34)  # 102

# how can we create methods directly : lambda comes as rescue
do_something_and_print(lambda data: data * 3, 124)  # 372

# so you don't need to create first the function


# cube
do_something_and_print(lambda data: data ** 3, 100)  #

# length of data
do_something_and_print(lambda data: len(data), "Tutankamon")  # 10
