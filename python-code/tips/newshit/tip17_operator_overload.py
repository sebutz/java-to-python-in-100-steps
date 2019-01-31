i = 2
j = 2

print(i + j)  # in fact is
print(i.__add__(j))


class Money:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    # we should return a Money object having the correct amount
    # def __add__(self, other):
    #     if self.currency == other.currency:
    #         self.amount += other.amount
    #     return self.amount

    # we should return a Money object having the correct amount
    def __add__(self, other):
        if self.currency == other.currency:
            return Money(self.currency, self.amount + other.amount)
        else:
            raise Exception("Not the same currency")

    def __sub__(self, other):
        if self.currency == other.currency:
            return Money(self.currency, self.amount - other.amount)
        else:
            raise Exception("Not the same currency")

    def __repr__(self):
        return repr((self.currency, self.amount))


money1 = Money('EUR', 10)
money2 = Money('EUR', 20)

# if we are not implementing def __add__(self, other):
# print(money1 + money2)  # TypeError: unsupported operand type(s) for +: 'Money' and 'Money'


# implementing __add__(self, other):

print(f"money1 +  money2={money1 + money2}")  # money1 +  money2=('EUR', 30)

print(f"money1 -  money2={money1 - money2}")  # money1 -  money2=('EUR', -10)

# amount1 + amount2=<__main__.Money object at 0x1085e2c88>
# it looks like we don't have representation

# with representation added
# money1 + money2=('EUR', 30)
money3 = Money('USD', 200)

try:
    money1 + money3
except Exception as exce:
    print(exce)
'''
Not the same currency
'''



