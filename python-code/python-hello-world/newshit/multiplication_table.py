# TypeError: print_multiplication_table() takes 1 positional argument but 3 were given
# # in Python you cannot do overloading
# it takes the last method defined (by name only)

# the way to solve this is by default arguments (or default values for arguments)


def print_multiplication_table(table, start, end):
    for i in range(start, end):
        print("%s x %s  = %s" % (table, i, table * i))


def print_multiplication_table(table):
    '''
    CANNOT DO THAT
    :param table:
    :return:
    '''
    #  print_multiplication_table(table, 1, 10)  # TypeError: print_multiplication_table() takes 1 positional argument but 3 were given
    for i in range(1, 10):
        print("%s x %s  = %s" % (table, i, table * i))


print_multiplication_table(7)
#  print_multiplication_table(7, 31, 40) # TypeError: print_multiplication_table() takes 1 positional argument but 3 were given


def print_multi_with_defaults(table= 5, start=1, end=10):
    for i in range(start, end):
        print("%s x %s  = %s" % (table, i, table * i))


print_multi_with_defaults(6)
print_multi_with_defaults(7, 31, 40)
print_multi_with_defaults()
