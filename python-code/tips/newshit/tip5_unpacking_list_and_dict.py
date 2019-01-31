def example_method(mandatory_param, default_param="Default", *args, **kwargs):
    print(f""" 
                  mandatory_param = {mandatory_param} {type(mandatory_param)},
                  default_param   = {default_param} {type(default_param)},
                  args = {args} {type(args)},
                  kwargs = {kwargs} {type(kwargs)}
                  """)


# want to pass this list as a parameters for the example_method
list_args = [1, 2, 3]

# one way
example_method(list_args[0], list_args[1], list_args[2])
'''
                  mandatory_param = 1 <class 'int'>,
                  default_param   = 2 <class 'int'>,
                  args = (3,) <class 'tuple'>,
                  kwargs = {} <class 'dict'>
                  
'''

# best: unpacking
# pay attention to the * !!!!
example_method(*list_args)
'''
                  mandatory_param = 1 <class 'int'>,
                  default_param   = 2 <class 'int'>,
                  args = (3,) <class 'tuple'>,
                  kwargs = {} <class 'dict'>
'''

# pay attention to the ** !!!
dict_args = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
example_method(*list_args, **dict_args)
'''
                   mandatory_param = 1 <class 'int'>,
                  default_param   = 2 <class 'int'>,
                  args = (3,) <class 'tuple'>,
                  kwargs = {'a': 1, 'b': 2, 'c': 3, 'd': 4} <class 'dict'>
'''

# what if we forgot * and **
example_method(list_args, dict_args)
'''
                  mandatory_param = [1, 2, 3] <class 'list'>,
                  default_param   = {'a': 1, 'b': 2, 'c': 3, 'd': 4} <class 'dict'>,
                  args = () <class 'tuple'>,
                  kwargs = {} <class 'dict'>
'''