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

    def __eq__(self, other):
        # comparing tuples
        return (self.currency, self.amount) == (other.currency, other.amount)


# some practice about the comparison of the tuples
print((1, 1) == (1, 1)) # True
print(('1', 2) == ('1', 2))  # True
print((1, 2) == (1, 1)) # False



money1 = Money('EUR', 10)
money2 = Money('EUR', 20)
money3 = Money('EUR', 20)
money4 =Money('USD', 10)

print(f"money1 ={money1}, money2={money2}")
print(f'money1 == money2 ? {money1 == money2}')

'''
money1 =('EUR', 10), money2=('EUR', 20)
money1 == money2 ? True
'''

print(f"money2 ={money2}, money3={money3}")
print(f'money2 == money3 ? {money2 == money3}')
'''
money2 =('EUR', 20), money3=('EUR', 20)
money2 == money3 ? True
'''