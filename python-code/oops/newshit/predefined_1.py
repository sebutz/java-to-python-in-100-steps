import math

print(math.cos(90))
# help(math.cos(90))  #it will spill all the help

from math import sqrt

print(sqrt(9))

# not adviced
from math import *
from math import gcd

print(gcd(24, 39))

from decimal import Decimal

print(4.5 - 3.2)
value1 = Decimal('4.5')
value2 = Decimal('3.2')
res = value1 - value2
print(value1 - value2)
print(type(res))  # <class 'decimal.Decimal'>


print(math.pi)

print(math.cos(math.pi*2))  #1.0

print(math.e)


print(math.ceil(5.5))
print(math.ceil(-5.5))
print(math.floor(5.5))
print(math.floor(-5.5))


'''
-0.4480736161291701
3.0
3
1.2999999999999998
1.3
<class 'decimal.Decimal'>
3.141592653589793
1.0
2.718281828459045
6
-5
5
-6
'''
