

def print_squares_up_to(n):
    for i in range(0, n):
        print('i = ', i + 1 ,  " i*i = ", (i+1)*(i +1))


print_squares_up_to(10)


def print_number_in_reverse(n):
    for i in range(0, n):
        print(n - i)


print_number_in_reverse(10)


def print_squares_of_even_numbers_upto(n):
    for i in range(1, n + 1, 2):  # we can have a step in range
        print('i = ', i + 1, " i*i = ", (i + 1) * (i + 1))


def print_number_in_reverse_v2(n):
    for i in range(n, 0, -1): # you can have decreasing order also
        print(i)


print_squares_of_even_numbers_upto(10)
print_number_in_reverse_v2(10)
