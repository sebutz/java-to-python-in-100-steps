# methods and arguments
# ARGS IS A TUPLE
# KARGS IS A DICTIONARY


# mandatory parameters, default parameters, variable arguments, keyword variable arguments
def example_method(mandatory_param, default_param="Default", *args, **kwargs):
    print(f""" 
                  mandatory_param = {mandatory_param} {type(mandatory_param)},
                  default_param   = {default_param} {type(default_param)},
                  args = {args} {type(args)},
                  kwargs = {kwargs} {type(kwargs)}
                  """)


# print('mandatory_param = ', mandatory_param)
#     # print('default_param = ', default_param)
#     # print('args = ', args)
#     # print('kwargs= ', kwargs)


# example_method()  # it will fail

example_method(15)
'''
                  mandatory_param = 15,
                  default_param   = Default,
                  args = (),
                  kwargs = {}
'''

# named arguments (or named arguments)
example_method(mandatory_param=15)
'''
                  mandatory_param = 15,
                  default_param   = Default,
                  args = (),
                  kwargs = {}
'''

# does not care about the type if default_parameter
example_method(25, 45)
'''
                  mandatory_param = 25,
                  default_param   = 45,
                  args = (),
                  kwargs = {}
'''

example_method(25, "aloha")
'''
                  mandatory_param = 25,
                  default_param   = aloha,
                  args = (),
                  kwargs = {}
'''

example_method(25, "String 1", "String 2", "String 3")
'''
                  mandatory_param = 25,
                  default_param   = String 1,
                  args = ('String 2', 'String 3'),
                  kwargs = {}
'''


example_method(25, "String 1", "String 2", "String 3", age = 23, name = "soldier", amount= 7400)
'''
                  mandatory_param = 25 <class 'int'>,
                  default_param   = String 1 <class 'str'>,
                  args = ('String 2', 'String 3') <class 'tuple'>,
                  kwargs = {'age': 23, 'name': 'soldier', 'amount': 7400} <class 'dict'>
'''

example_method(25, age = 23, name = "soldier", amount= 7400)
'''
mandatory_param = 25 <class 'int'>,
                  default_param   = Default <class 'str'>,
                  args = () <class 'tuple'>,
                  kwargs = {'age': 23, 'name': 'soldier', 'amount': 7400} <class 'dict'>
'''


# the order is important : the keyword arguments are the last
# before them there are variable arguments
# first are mandatory params and then the default params

# example_method(25, age = 23, name = "soldier", amount= 7400, "String 1")  will give compilation error


