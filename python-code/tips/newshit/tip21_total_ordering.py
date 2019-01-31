from functools import total_ordering


@total_ordering  # you need to implement only __eq__ and one of the big four: gt, lt, ge, le
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

    # def __gt__(self, other):
    #     return (self.currency, self.amount) > (other.currency, other.amount)
    #
    # def __lt__(self, other):
    #     return (self.currency, self.amount) < (other.currency, other.amount)
    #
    # def __ge__(self, other):
    #     return (self.currency, self.amount) >= (other.currency, other.amount)
    #
    # def __le__(self, other):
    #     return (self.currency, self.amount) <= (other.currency, other.amount)

    def __ge__(self, other):
        return (self.currency, self.amount) >= (other.currency, other.amount)

#     return (self.currency, self.amount) >= (other.currency, other.amount)

money1 = Money('EUR', 10)
money2 = Money('EUR', 20)
money3 = Money('EUR', 20)
money4 = Money('USD', 10)

print(f"money1  < money2, {money1 < money2}")
print(f'money1 == money2 ? {money1 == money2}')
print(f'money1 > money2 ? {money1 > money2}')

'''
money1  < money2, True
money1 == money2 ? False
money1 > money2 ? False
'''
