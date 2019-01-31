import datetime

today = datetime.datetime.today()

# human readable representation
print(today.__str__())  # 2019-01-31 12:48:29.810524

# repr: how can you create an object from that value
print(today.__repr__())  # datetime.datetime(2019, 1, 31, 12, 48, 29, 810524)


# if you are not provide __str__ then __repr__ will be used all around
# for exanple, for datetime.datetime.today() has a string representation
# so when you are using print, the __str__ will be preferred.
print(today) # 2019-01-31 12:51:32.956539


# by default, it is best to implement always __repr__