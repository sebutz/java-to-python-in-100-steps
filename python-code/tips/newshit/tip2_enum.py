# enum

# Currency - USD, EUR. INR

from enum import Enum


class Currency(Enum):
    USD = 1
    EUR = 2
    INR = 3


print(Currency.EUR)


# iterate
for currency in Currency:
    print(currency)


# create

print(Currency(1)) # Currency.USD

print(Currency.EUR.name)  # EUR
print(Currency(1).name) # USD
print(Currency(1).value)  # 1

'''
Currency.EUR
Currency.USD
Currency.EUR
Currency.INR
Currency.USD
EUR
USD
1
'''