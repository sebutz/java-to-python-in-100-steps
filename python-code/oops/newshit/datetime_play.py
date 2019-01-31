# datetime


import datetime

# today
print(datetime.datetime.today())  # 2019-01-30 16:37:37.389552

today_day = datetime.datetime.today()
print(today_day.year)
print(today_day.time())

# create a specific date

some_date = datetime.datetime(2019, 5, 27)  # 2019-05-27 00:00:00
print(some_date)

print("date", some_date.date())


# operations on date
# time delta


day = some_date
print(day + datetime.timedelta(days=19))
print(day + datetime.timedelta(weeks=3))

''''
2019-01-30 16:44:31.697078
2019
16:44:31.697129
2019-05-27 00:00:00
date 2019-05-27
2019-06-15 00:00:00
2019-06-17 00:00:00
'''