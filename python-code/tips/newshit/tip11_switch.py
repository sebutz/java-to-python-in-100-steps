# you can replace a switch (which is not existing in Python) with a dictionary

week_days = { 0: 'Sunday', 1: 'Monday', 2: 'Tuesday'}

print(week_days.get(0))

# you can also pass a default

print(week_days.get(5, "Saturday"))

'''
Sunday
Saturday
'''