# custom exception play


class Amount:

    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def add(self, that):
        if self.currency == that.currency:
            self.amount += that.amount
        else:
            raise Exception("Exception: different currency")

    def add2(self, that):
        if self.currency == that.currency:
            self.amount += that.amount
        else:
            raise CurrencyDoNotMatchException("CurrencyDoNotMatchException: different currency")

    def __repr__(self):
        return repr((self.currency, self.amount))


# define custom exception
class CurrencyDoNotMatchException(Exception):
    def __init__(self, message):
        super().__init__(message)

    def __str__(self):
        return "kuku"   # you can override the print behaviour for the exception


amount1 = Amount("EUR", 35)
amount2 = Amount("EUR", 72)
amount3 = Amount("USD", 23)

amount1.add(amount2)

print(amount1)

try:
    amount1.add(amount3)
except Exception as exception:
    print(exception)
else:
    print(amount1)
finally:
    print("Processing finished")

try:
    print("catching custom exception")
    amount1.add2(amount3)
except CurrencyDoNotMatchException as exception:
    print("catch")
    print(exception)
else:
    print(amount1)
finally:
    print("Processing finished")

'''
('EUR', 107)
Exception: different currency
Processing finished
CurrencyDoNotMatchException: different currency
Processing finished
'''
