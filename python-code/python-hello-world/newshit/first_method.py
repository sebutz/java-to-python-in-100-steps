# first method
# absence of the static keyword
# supports structured programming (invoking outside the class)


def print_hello_world_twice():
    '''
    2 blank lines before the method and after
    :return:
    '''
    print("Hello world1")
    print("Hello world2")
    print("Hello world3")


def print_hello_world_multiple_times(n):
    for i in range(n):
        print("Hello world")


def print_hello_world_multiple_times2(times):
    for i in range(0, times):
        print("Hello world")


print("Hello world4")
print_hello_world_twice()
print_hello_world_multiple_times(7)
print_hello_world_multiple_times2(7)